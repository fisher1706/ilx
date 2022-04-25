import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from src.waits import wait_until_dropdown_list_loaded, wait_until_dropdown_is_not_empty
from src.pages.locator import Locator as L
from src.pages.element import Element
from src.pages.waits import ElementToBeEnabled, PageUrlToBe
from glbl import Log, Error

class BasePage():
    def __init__(self, context):
        self.context = context
        self.url = self.context.session_context.url
        self.driver = context.driver
        self.element = Element(context)

    def follow_url(self, url, expected_url=None):
        try:
            self.driver.get(url)
        except Exception as e:
            expected_url = url if expected_url is None else expected_url
            current_url = self.driver.current_url
            if current_url != expected_url:
                Error.error(f"Error during try to follow URL = '{url}'. Current: {current_url}; Expected: {expected_url}.\n{e}")
            else:
                Log.info(f"URL '{url}' is followed")
        else:
            Log.info(f"URL '{url}' is followed")
            self.wait_for_complete_ready_state()

    def url_should_be(self, url):
        try:
            WebDriverWait(self.driver, 20).until(PageUrlToBe(url)) #pylint: disable=E1102
        except Exception as e:
            Error.error(f"Incorrect page url.\n{e}")
        else:
            Log.info("Page url is correct")

    def url_should_contain(self, text):
        current_url = self.driver.current_url
        if f"{text}" in current_url:
            Log.info(f"URL contains text '{text}'")
        else:
            Error.error(f"URL does not contain '{text}'")

    def get_authorization_token(self):
        cookies = self.driver.get_cookies()
        token = None
        for cookies_dict in cookies:
            name = cookies_dict["name"].split(".")[-1]
            if name == "idToken":
                token = cookies_dict["value"]
                break
        return token

    def input_by_name(self, name, data):
        if data is not None:
            self.element(f"//input[@name='{name}']").enter(data)

    def select_in_dropdown(self, xpath, name):
        if name is not None:
            self.element(xpath).click()
            Log.info(f"Dropdown list with XPATH = '{xpath}' is opened")
            self.element(f"{xpath}/..//div[text()='{name}' and @tabindex='-1']").click()

    def manage_shipto(self, shiptos, prefix_path=""):
        if shiptos is not None:
            self.element(L.get_button_by_name("Manage")).click()
            self.element(L.select_button).get()
            for shipto_name in shiptos:
                self.element(f"{L.dialog}//span[text()='{shipto_name}']").get()
            for shipto in shiptos:
                for row in range(1, self.element(prefix_path+L.table_row).count()+1):
                    if shipto == self.element(L.get_table_item_in_dialog(row, 1)).text():
                        self.element(f"{L.get_table_item_in_dialog(row, 5)}//button").click()
                        break
                else:
                    Error.error(f"There is no ShipTo '{shipto}'")
            self.element(f"{L.dialog}{L.submit_button}//span[text()='Save']").click()

    def wait_for_complete_ready_state(self, incomplete_before=False):
        if incomplete_before:
            WebDriverWait(self.driver, 15).until_not(lambda x: x.execute_script("return document.readyState === 'complete'"))
        WebDriverWait(self.driver, 15).until(lambda x: x.execute_script("return document.readyState === 'complete'"))

    def open_last_page(self):
        pagination_buttons = self.driver.find_elements_by_xpath(f"{L.pagination_bottom}//button")
        if len(pagination_buttons) > 3:
            if pagination_buttons[-2].is_enabled():
                pagination_buttons[-2].click()
                self.should_be_last_page()

    def last_page(self, pagination=None, wait=True):
        self.select_pagination(pagination)
        self.wait_for_the_first_element_in_table()
        if wait:
            try:
                WebDriverWait(self.driver, 7).until_not(ElementToBeEnabled(L.button_last_page)) #pylint: disable=E1102
            except:
                pass
        if self.element(L.button_last_page).is_enabled():
            self.element(L.button_last_page)
            self.wait_for_the_first_element_in_table()

    def wait_for_the_first_element_in_table(self):
        self.element(L.get_table_item(2, 1)).get()

    def select_pagination(self, number_of_elements):
        if number_of_elements is not None:
            self.element(L.listbox).click()
            self.element(L.get_select_pagination(number_of_elements)).click()

    def should_be_last_page(self):
        try:
            WebDriverWait(self.driver, 15).until(lambda x: x.find_elements_by_xpath("//div[@class='pagination-bottom']//button")[-2].get_attribute("disabled") == "true") #pylint: disable=E1102
        except Exception as e:
            Error.error(f"Last page is not opened.\n{e}")
        else:
            Log.info("Last page is opened")

    def get_table_rows_number(self):
        return self.element(L.table_row).count()

    def get_header_column(self, header):
        self.element(L.table_header_column).get() #wait for the headers appear
        elements = self.element(L.table_header_column).get_list()
        for index, element in enumerate(elements):
            if element.text() == header:
                return index+1
        return False

    def get_table_item_text_by_indexes(self, row, column):
        xpath = L.get_table_item(row, column)
        return self.element(xpath).text()

    def check_last_table_item_by_header(self, header, expected_text):
        self.check_table_item_by_header(self.get_table_rows_number(), header, expected_text)

    def get_last_table_item_text_by_header(self, header):
        return self.get_table_item_text_by_header(header, self.get_table_rows_number())

    def get_table_item_text_by_header(self, header, row):
        column = self.get_header_column(header)
        if column:
            return self.get_table_item_text_by_indexes(row, column)
        Error.error(f"There is no header '{header}'")

    def check_table_item_by_header(self, row, header, expected_text):
        if expected_text is not None:
            column = self.get_header_column(header)
            current_text = None
            if column:
                current_text = self.get_table_item_text_by_indexes(row, column)
            else:
                Error.error(f"There is no header '{header}'")
            if isinstance(expected_text, list):
                correctness = True
                for element in expected_text:
                    if element is not None:
                        if element not in current_text:
                            Error.error(f"{row} element in '{header}' column is incorrect")
                if correctness:
                    Log.info(f"{row} element in '{header}' column is correct")
            else:
                self.element_should_have_text(L.xpath_table_item(row, column), expected_text)

    def check_table_item(self, expected_text, cell=None, header=None, row=None, last=None):
        if expected_text is not None:
            if (cell is None and header is None) or (cell is not None and header is not None):
                Error.error("Either 'cell' or 'header' parameter should be defined")
            column = cell if header is None else self.get_header_column(header)

            if isinstance(expected_text, list):
                if last is not None:
                    current_text = self.get_element_text(L.xpath_get_last_table_item(column))
                elif row is not None:
                    current_text = self.get_element_text(L.xpath_get_table_item(row, column))
                else:
                    Error.error("Either 'row' or 'last' parameter should be defined")
                correctness = True
                for element in expected_text:
                    if element is not None:
                        if element not in current_text:
                            Error.error(f"{row} element in '{header}' column is incorrect")
                if correctness:
                    Log.info(f"{row} element in '{header}' column is correct")
            else:
                if last is not None:
                    self.element_should_have_text(L.xpath_get_last_table_item(column), expected_text)
                elif row is not None:
                    self.element_should_have_text(L.xpath_get_table_item(row, column), expected_text)
                else:
                    Error.error("Either 'row' or 'last' parameter should be defined")

    def delete_dialog_should_be_about(self, expected_text):
        current_text = str(self.delete_dialog_about())
        if current_text == expected_text:
            Log.info(f"Delete dialog about '{current_text}'")
        else:
            Error.error(f"Delete dialog about '{current_text}', but should be about '{expected_text}'")

    def delete_dialog_about(self):
        xpath = L.dialog+"//b"
        try:
            text = self.element(xpath).text()
        except Exception as e:
            Error.error(f"Element with XPATH = '{xpath}' not found.\n{e}")
        else:
            return text

    def title_should_be(self, title):
        try:
            WebDriverWait(self.driver, 20).until(EC.title_is(title))
        except Exception as e:
            Error.error(f"Title should be '{title}', but now it is '{self.driver.title}'.\n{e}")
        else:
            Log.info(f"Title is '{title}'")

    def select_checkbox(self, xpath):
        checked = self.element(xpath).get().get_attribute("checked")
        if checked == 'true':
            Log.info(f"Checkbox with XPATH = '{xpath}' has been already checked")
        elif checked is None:
            self.element(xpath).click()
            Log.info(f"Checkbox with XPATH = '{xpath}' is checked")

    def unselect_checkbox(self, xpath):
        checked = self.element(xpath).get().get_attribute("checked")
        if checked == 'true':
            self.element(xpath).click()
            Log.info(f"Checkbox with XPATH = '{xpath}' is unchecked")
        elif checked is None:
            Log.info(f"Checkbox with XPATH = '{xpath}' has been already unchecked")

    def select_checkbox_in_dialog_by_name(self, name):
        self.select_checkbox(L.xpath_checkbox_in_dialog_by_name(name))

    def unselect_checkbox_in_dialog_by_name(self, name):
        self.unselect_checkbox(L.xpath_checkbox_in_dialog_by_name(name))

    def set_checkbox_value_in_dialog_by_name(self, name, value):
        if value:
            self.select_checkbox(L.xpath_checkbox_in_dialog_by_name(name))
        else:
            self.unselect_checkbox(L.xpath_checkbox_in_dialog_by_name(name))

    def clear_all_checkboxes_in_dialog(self):
        try:
            checkboxes = self.element(L.dialog+L.checkbox).get_list()
        except Exception as e:
            Error.error(f"Checkboxes in dialog not found.\n{e}")
        else:
            for element in checkboxes:
                checked = element.get().get_attribute("checked")
                if checked == 'true':
                    element.click()

    def checkbox_should_be(self, xpath, condition):
        checked = self.element(xpath).get().get_attribute("checked")
        if condition:
            if checked == 'true':
                Log.info(f"Checkbox with XPATH = '{xpath}' is checked")
            elif checked is None:
                Error.error(f"Checkbox with XPATH = '{xpath}' should be checked")
        elif not condition:
            if checked is None:
                Log.info(f"Checkbox with XPATH = '{xpath}' is unchecked")
            elif checked == 'true':
                Error.error(f"Checkbox with XPATH = '{xpath}' should be unchecked")
        else:
            Error.error("Incorrect checkbox condition")

    def scan_table(self, scan_by, column_header, body=None, pagination=True):
        column = self.get_header_column(column_header)
        if pagination:
            pagination_buttons = self.element(L.pagination_bottom+"//button").get_list()
        if column:
            is_break = False
            while True:
                for row in range(1, self.get_table_rows_number()+1):
                    cell_value = self.get_table_item_text_by_indexes(row, column)
                    if cell_value == scan_by:
                        Log.info(f"Text '{scan_by}' is found in the table")
                        if body is None:
                            return row
                        for cell in body.keys():
                            self.check_table_item_by_header(row, cell, body[cell])
                        return row
                if is_break:
                    break
                if pagination:
                    if (len(pagination_buttons) > 3 and pagination_buttons[-2].is_enabled()):
                        pagination_buttons[-1].click()
                    else:
                        Error.error(f"There is no value '{scan_by}' in the '{column}' column")
                else:
                    Error.error(f"There is no value '{scan_by}' in the '{column}' column")
        else:
            Error.error(f"There is no header '{column_header}'")

    def import_csv(self, element_id, filename):
        folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        folder += "/output/"+filename
        self.element(element_id).get().send_keys(folder)
        self.element(L.dialog).get()
        self.click_xpath(L.xpath_continue_import)
        self.element(L.dialog).wait_until_disappeared()

    def click_tab_by_name(self, tab_name):
        self.element(L.xpath_button_tab_by_name(tab_name)).click

    def get_row_of_table_item_by_column(self, scan_by, column, prefix_path=""):
        for index, row in enumerate(range(1, self.element(prefix_path+L.table_row).count()+1)):
            if scan_by == self.element(prefix_path+L.get_table_item_outdated(row, column)).text():
                return index+1

    def set_slider(self, xpath, condition):
        if condition is not None:
            if self.element(xpath).get().get_attribute("value") != condition:
                self.element(xpath).get().click()
                Log.info(f"Value of slider with XPATH = '{xpath}' is changed")
            else:
                Log.info(f"Slider with XPATH = '{xpath}' already has necessary value")

    def page_refresh(self):
        self.driver.refresh()


    #=========================NOT REFACTORED========================
    def get_row_of_table_item_by_header(self, scan_by, column_header, prefix_path=""):
        column = self.get_header_column(column_header)
        for index, row in enumerate(range(1, self.get_element_count(prefix_path+L.xpath_table_row)+1)):
            if scan_by == self.get_element_by_xpath(prefix_path+L.xpath_table_item(row, column)).text:
                return index+1

    def wait_until_dropdown_list_loaded(self, count):
        try:
            WebDriverWait(self.driver, 15).until(wait_until_dropdown_list_loaded(count)) #pylint: disable=E1102
        except:
            Error.error("Dropdown list is not loaded")
        else:
            Log.info("Dropdown list is loaded")

    def check_found_dropdown_list_item(self, item_xpath, expected_text):
        item_text = self.get_element_text(item_xpath)
        number = self.get_element_count(item_xpath)
        if number == 1:
            if item_text == expected_text:
                Log.info("Dropdown list element has been found")
            else:
                Error.error(f"The text of dropdown list element is '{item_text}'")
        else:
            Error.error(f"The number of dropdown list elements = '{number}'")

    def select_in_dropdown_via_input(self, xpath, name, span=None):
        if name is not None:
            self.click_xpath(xpath)
            Log.info(f"Dropdown list with XPATH = '{xpath}' is opened")
            self.input_data_xpath(name, f"{xpath}//input")
            #self.get_element_by_xpath(f"{xpath}//input").send_keys(Keys.ENTER)
            if span:
                self.click_xpath(f"{xpath}/..//div[@tabindex='-1']//span[text()='{name}']")
            else:
                self.click_xpath(f"{xpath}/..//div[text()='{name}' and @tabindex='-1']")

    def input_inline_xpath(self, data, xpath):
        if data is not None:
            self.click_xpath(xpath)
            self.click_xpath(xpath)
            element = self.get_element_by_xpath(f"{xpath}//input")
            self.driver.execute_script("arguments[0].value = arguments[1]", element, "")
            self.input_data_xpath(data, f"{xpath}//input")
            element.send_keys(Keys.ENTER)

    def select_customer_shipto(self, customer_xpath=None, customer_name=None, shipto_xpath=None, shipto_name=None):
        if customer_xpath is None:
            customer_xpath = L.xpath_by_count(L.xpath_select_box, 1)
        if shipto_xpath is None:
            shipto_xpath = L.xpath_by_count(L.xpath_select_box, 2)
        self.wait_until_page_loaded()
        self.select_in_dropdown(customer_xpath, customer_name)
        self.wait_until_page_loaded()
        self.select_in_dropdown(shipto_xpath, shipto_name)
        self.wait_until_page_loaded()

    def element_should_have_text(self, xpath, text):
        self.get_element_by_xpath(xpath)
        try:
            WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element((By.XPATH, xpath), text))
        except:
            Error.error(f"Element with XPATH = '{xpath}' was found but text is different: '{self.get_element_text(xpath)}' != '{text}'")
        else:
            Log.info(f"Element with XPATH = '{xpath}' contains correct text")

    def element_should_have_text_id(self, element_id, text):
        self.get_element_by_id(element_id)
        try:
            WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element((By.ID, element_id), text))
        except:
            Error.error(f"Element with XPATH = '{element_id}' was found but text is different")
        else:
            Log.info(f"Element with XPATH = '{element_id}' contains correct text")

    def element_text_should_be_empty(self, xpath):
        text = self.get_element_text(xpath)
        assert text is None or text == "", f"Element {xpath} contains text: {text}"

    def wait_untill_dropdown_not_empty(self, xpath):
        try:
            WebDriverWait(self.driver, 15).until(wait_until_dropdown_is_not_empty(By.XPATH, xpath)) #pylint: disable=E1102
        except:
            pass

    def select_shipto_sku(self, shipto=None, sku=None):
        if shipto is not None:
            self.select_in_dropdown_via_input(L.xpath_dropdown_in_dialog(1), shipto)
            self.wait_until_page_loaded()
        if sku is not None:
            self.select_in_dropdown(L.xpath_dropdown_in_dialog(2), sku)
            self.wait_until_page_loaded()
