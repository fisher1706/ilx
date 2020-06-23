from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from src.waits.dialog_is_not_present import dialog_is_not_present
from src.waits.elements_count_should_be import elements_count_should_be
from src.waits.is_page_loading import is_page_loading
from src.waits.is_progress_bar_loading import is_progress_bar_loading
from src.waits.last_page import last_page
from src.waits.new_element_in_table import new_element_in_table
from src.waits.page_url_is import page_url_is
from src.waits.wait_until_disabled import wait_until_disabled
from src.waits.wait_until_dropdown_list_loaded import wait_until_dropdown_list_loaded
from src.resources.locator import Locator
import csv
import os
import pytest

class BasePage():
    def __init__(self, context):
        self.context = context
        self.driver = context.driver
        self.url = self.context.session_context.url
        self.logger = context.logger
        self.data = context.data

    def follow_url(self, url, hide_intercom=False):
        try:
            self.driver.get(url)
        except:
            self.logger.error(f"Error during try to follow URL = '{url}'")
        else:
            self.logger.info(f"URL = '{url}' is followed")
            if (hide_intercom == True):
                self.hide_intercom()

    def hide_intercom(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, Locator.id_intercom_container)))
            self.driver.execute_script("document.getElementById('intercom-container').style.display = 'None';")
        except:
            try:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'intercom-lightweight-app')))
                self.driver.execute_script("document.getElementsByClassName('intercom-lightweight-app')[0].style.display = 'None';")
            except:
                self.logger.error("Intercom cannot be hide")
            else:
                self.logger.info("Intercom is hidden")
        else:
            self.logger.info("Intercom is hidden")

    def get_element_by_xpath(self, xpath):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
        except:
            self.logger.error(f"Element with XPATH = '{xpath}' not found")
        else:
            return element

    def get_element_by_id(self, id):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, id)))
        except:
            self.logger.error(f"Element with ID = '{id}' not found")
        else:
            return element

    def get_element_count(self, xpath):
        try:
            elements = self.driver.find_elements_by_xpath(xpath)
        except:
            self.logger.error(f"Elements with XPATH = '{xpath}' do not found")
        else:
            count = len(elements)
            self.logger.info(f"There are '{count}' elements with XPATH = '{xpath}'")
            return count

    def get_element_text(self, xpath):
        element = self.get_element_by_xpath(xpath)
        return element.text

    def click_id(self, id, timeout=20):
        self.get_element_by_id(id)
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.ID, id))).click()
        except:
            self.logger.error(f"Element with ID = '{id}' is not clickable")
        else:
            self.logger.info(f"Element with ID = '{id}' is clicked")

    def click_xpath(self, xpath, timeout=20):
        self.get_element_by_xpath(xpath)
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        except:
            self.logger.error(f"Element with XPATH = '{xpath}' is not clickable")
        else:
            self.logger.info(f"Element with XPATH = '{xpath}' is clicked")

    def input_data_id(self, data, id):
        self.clear_id(id)
        element = self.get_element_by_id(id)
        element.send_keys(data)
        self.logger.info(f"Data '{data}' inputed into element with ID = '{id}'")

    def input_data_xpath(self, data, xpath):
        self.clear_xpath(xpath)
        element = self.get_element_by_xpath(xpath)
        element.send_keys(data)
        self.logger.info(f"Data '{data}' inputed into element with XPATH = '{xpath}'")

    def should_be_disabled_id(self, id):
        element = self.get_element_by_id(id)
        assert not element.is_enabled(), f"Element with ID = '{id}' is enabled, but should be disabled"

    def should_be_disabled_xpath(self, xpath):
        element = self.get_element_by_xpath(xpath)
        assert not element.is_enabled(), f"Element with XPATH = '{xpath}' is enabled, but should be disabled"

    def should_be_enabled_id(self, id):
        element = self.get_element_by_id(id)
        assert element.is_enabled(), f"Element with ID = '{id}' is disabled, but should be enabled"

    def should_be_enabled_xpath(self, xpath):
        element = self.get_element_by_xpath(xpath)
        assert element.is_enabled(), f"Element with XPATH = '{xpath}' is disabled, but should be enabled"

    def get_authorization_token(self):
        cookies = self.driver.get_cookies()
        token = None
        for cookies_dict in cookies:
            name = cookies_dict["name"].split(".")[-1]
            if (name == "idToken"):
                token = cookies_dict["value"]
                break
        return token

    def url_should_be(self, url):
        try:
            WebDriverWait(self.driver, 15).until(page_url_is(url))
        except:
            self.logger.error("Incorrect page url")
        else:
            self.logger.info("Page url is correct")
    
    def url_should_contain(self, text):
        current_url = self.driver.current_url
        result = f"{text}" in current_url
        if (result is True): 
            self.logger.info(f"URL contains text '{text}'")
        else: 
            self.logger.error(f"URL does not contain '{text}'")

    def input_by_name(self, name, data):
        if (data is not None):
            self.input_data_xpath(data, f"//input[@name='{name}']")

    def clear_id(self, id):
        element = self.get_element_by_id(id)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)

    def clear_xpath(self, xpath):
        element = self.get_element_by_xpath(xpath)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)

    def select_in_dropdown(self, xpath, name):
        if (name is not None):
            self.click_xpath(xpath)
            self.logger.info(f"Dropdown list with XPATH = '{xpath}' is opened")
            self.click_xpath(f"{xpath}/..//div[text()='{name}']")

    def manage_shipto(self, shiptos, prefix_path=""):
        if (shiptos is not None):
            self.click_xpath(Locator.xpath_button_by_name("Manage"))
            for shipto in shiptos:
                for row in range(1, self.get_element_count(prefix_path+Locator.xpath_table_row)+1):
                    if (shipto == self.driver.find_element_by_xpath(Locator.xpath_table_item_in_dialog(row, 1)).text):
                        self.click_xpath(f"{Locator.xpath_table_item_in_dialog(row, 5)}//button")
                        break
                else:
                    self.logger.error(f"There is no ShipTo '{shipto}'")
            self.click_xpath(f"{Locator.xpath_dialog}{Locator.xpath_submit_button}//span[text()='Save']")

    def dialog_should_not_be_visible(self):
        try:
            WebDriverWait(self.driver, 15).until(dialog_is_not_present())
        except:
            self.logger.error("Dialog is not closed")
        else:
            self.logger.info("Dialog is closed")

    def dialog_should_be_visible(self):
        try:
            WebDriverWait(self.driver, 15).until_not(dialog_is_not_present())
        except:
            self.logger.error("Dialog is not opened")
        else:
            self.logger.info("Dialog is opened")

    def elements_count_should_be(self, xpath, number, time=15):
        try:
            WebDriverWait(self.driver, time).until(elements_count_should_be(xpath, number))
        except:
            self.logger.error(f"Count of elements is incorrect: should be '{number}', now '{self.get_element_count(xpath)}'")
        else:
            self.logger.info("Count of elements is correct")

    def wait_until_page_loaded(self, time=3):
        try:
            WebDriverWait(self.driver, time).until(is_page_loading())
        except:
            pass
        WebDriverWait(self.driver, 15).until_not(is_page_loading())

    def open_last_page(self):
        pagination_buttons = self.driver.find_elements_by_xpath(f"{Locator.xpath_pagination_bottom}//button")
        if (len(pagination_buttons) > 3):
            if(pagination_buttons[-2].is_enabled() == True):
                self.wait_until_page_loaded()
                pagination_buttons[-2].click()
                self.should_be_last_page()
                self.wait_until_page_loaded()
    
    def should_be_last_page(self):
        try:
            WebDriverWait(self.driver, 15).until(last_page())
        except:
            self.logger.error("Last page is not opened")
        else:
            self.logger.info("Last page is opened")

    def get_table_rows_number(self):
        return self.get_element_count(Locator.xpath_table_row)

    def get_header_column(self, header):
        headers = self.driver.find_elements_by_xpath(Locator.xpath_table_header_column)
        for index, item in enumerate(headers):
            if (item.text == header):
                return index+1
        else:
            return False

    def get_table_item_text_by_indexes(self, row, column):
        xpath = Locator.xpath_table_item(row, column)
        return self.get_element_text(xpath)

    def check_last_table_item_by_header(self, header, expected_text):
        self.check_table_item_by_header(self.get_table_rows_number(), header, expected_text)

    def get_last_table_item_text_by_header(self, header):
        return self.get_table_item_text_by_header(header, self.get_table_rows_number())

    def get_table_item_text_by_header(self, header, row):
        column = self.get_header_column(header)
        if (column):
            return self.get_table_item_text_by_indexes(row, column)
        else:
            self.logger.error(f"There is no header '{header}'")

    def check_table_item_by_header(self, row, header, expected_text):
        if (expected_text is not None):
            column = self.get_header_column(header)
            current_text = None
            if (column):
                current_text = self.get_table_item_text_by_indexes(row, column)
            else:
                self.logger.error(f"There is no header '{header}'")
            if isinstance(expected_text, list):
                correctness = True
                for element in expected_text:
                    if (element is not None):
                        if (element not in current_text):
                            self.logger.error(f"{row} element in '{header}' column is incorrect")
                            correctness = False
                            break
                if (correctness == True):
                    self.logger.info(f"{row} element in '{header}' column is correct")
            else:
                if (current_text == expected_text):
                    self.logger.info(f"{row} element in '{header}' column is correct")
                else:
                    self.logger.error(f"{row} element in '{header}' column is '{current_text}', but should be '{expected_text}'")

    def delete_dialog_should_be_about(self, expected_text):
        self.wait_until_page_loaded(1)
        current_text = str(self.delete_dialog_about())
        if (current_text == expected_text):
            self.logger.info(f"Delete dialog about '{current_text}'")
        else:
            self.logger.error(f"Delete dialog about '{current_text}', but should be about '{expected_text}'")

    def delete_dialog_about(self):
        xpath = Locator.xpath_dialog+"//b"
        try:
            element = self.get_element_by_xpath(xpath)
        except:
            self.logger.error(f"Element with XPATH = '{xpath}' not found")
        else:
            return element.text

    def title_should_be(self, title):
        try:
            element = WebDriverWait(self.driver, 15).until(EC.title_is(title))
        except:
            self.logger.error(f"Title should be '{title}', but now it is '{self.driver.title}'")
        else:
            self.logger.info(f"Title is '{title}'")

    def select_checkbox(self, xpath):
        element = self.get_element_by_xpath(xpath)
        checked = element.get_attribute("checked")
        if (checked == 'true'):
            self.logger.info(f"Checkbox with XPATH = '{xpath}' has been already checked")
        elif (checked is None):
            element.click()
            self.logger.info(f"Checkbox with XPATH = '{xpath}' is checked")

    def unselect_checkbox(self, xpath):
        element = self.get_element_by_xpath(xpath)
        checked = element.get_attribute("checked")
        if (checked == 'true'):
            element.click()
            self.logger.info(f"Checkbox with XPATH = '{xpath}' is unchecked")
        elif (checked is None):
            self.logger.info(f"Checkbox with XPATH = '{xpath}' has been already unchecked")

    def select_checkbox_in_dialog_by_name(self, name):
        self.select_checkbox(Locator.xpath_checkbox_in_dialog_by_name(name))
    
    def unselect_checkbox_in_dialog_by_name(self, name):
        self.unselect_checkbox(Locator.xpath_checkbox_in_dialog_by_name(name))

    def clear_all_checkboxes_in_dialog(self):
        try:
            checkboxes = self.driver.find_elements_by_xpath(Locator.xpath_dialog+Locator.xpath_checkbox)
        except:
            self.logger.error("Checkboxes in dialog not found")
        else:
            for element in checkboxes:
                checked = element.get_attribute("checked")
                if (checked == 'true'):
                    element.click()

    def checkbox_should_be(self, xpath, condition):
        element = self.get_element_by_xpath(xpath)
        checked = element.get_attribute("checked")
        if (condition == True):
            if (checked == 'true'):
                self.logger.info(f"Checkbox with XPATH = '{xpath}' is checked")
            elif (checked is None):
                self.logger.error(f"Checkbox with XPATH = '{xpath}' should be checked")
        elif (condition == False):
            if (checked is None):
                self.logger.info(f"Checkbox with XPATH = '{xpath}' is unchecked")
            elif (checked == 'true'):
                self.logger.error(f"Checkbox with XPATH = '{xpath}' should be unchecked")
        else:
            self.logger.error("Incorrect checkbox condition")

    def scan_table(self, scan_by, column_header, body=None, pagination=True):
        column = self.get_header_column(column_header)
        if (pagination == True):
            pagination_buttons = self.driver.find_elements_by_xpath(Locator.xpath_pagination_bottom+"//button")
        if (column):
            is_break = False
            while True:
                for row in range(1, self.get_table_rows_number()+1):
                    cell_value = self.get_table_item_text_by_indexes(row, column)
                    if (cell_value == scan_by):
                        self.logger.info(f"Text '{scan_by}' is found in the table")
                        if (body is None):
                            return row
                        else:
                            for cell in body.keys():
                                self.check_table_item_by_header(row, cell, body[cell])
                            return row
                if (is_break):
                    break
                if (pagination == True):
                    if (len(pagination_buttons) > 3 and pagination_buttons[-2].is_enabled() == True):
                            pagination_buttons[-1].click()
                            self.wait_until_page_loaded()
                    else:
                        self.logger.error(f"There is no value '{scan_by}' in the '{column}' column")
                        break
                else:
                    self.logger.error(f"There is no value '{scan_by}' in the '{column}' column")
                    break
        else:
            self.logger.error(f"There is no header '{column_header}'")

    def import_csv(self, id, filename):
        folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        folder += "/output/"+filename
        self.get_element_by_id(id).send_keys(folder)
        self.dialog_should_be_visible()
        self.click_xpath(Locator.xpath_continue_import)
        self.dialog_should_not_be_visible()

    def click_tab_by_name(self, tab_name):
        self.click_xpath(Locator.xpath_button_tab_by_name(tab_name))
        self.wait_until_progress_bar_loaded()

    def wait_until_progress_bar_loaded(self, time=4):
        try:
            WebDriverWait(self.driver, time).until(is_progress_bar_loading())
        except:
            pass
        WebDriverWait(self.driver, 15).until_not(is_progress_bar_loading())
        
    def get_row_of_table_item_by_column(self, scan_by, column, prefix_path=""):
        for index, row in enumerate(range(1, self.get_element_count(prefix_path+Locator.xpath_table_row)+1)):
            if (scan_by == self.driver.find_element_by_xpath(prefix_path+Locator.xpath_table_item(row, column)).text):
                return index+1

    def click_table_title(self, title, row):
        self.click_xpath(Locator.xpath_by_count(Locator.xpath_table_row, row)+title)

    def set_slider(self, xpath, condition):
        if (condition is not None):
            element = self.get_element_by_xpath(xpath)
            if (element.get_attribute("value") != condition):
                element.click()
                self.logger.info(f"Value of slider with XPATH = '{xpath}' is changed")
            else:
                self.logger.info(f"Slider with XPATH = '{xpath}' already has necessary value")

    def page_refresh(self):
        self.driver.refresh()

    def get_row_of_table_item_by_header(self, scan_by, column_header, prefix_path=""):
        column = self.get_header_column(column_header)
        for index, row in enumerate(range(1, self.get_element_count(prefix_path+Locator.xpath_table_row)+1)):
            if (scan_by == self.get_element_by_xpath(prefix_path+Locator.xpath_table_item(row, column)).text):
                return index+1
    
    def wait_until_dropdown_list_loaded(self, count):
        try:
            WebDriverWait(self.driver, 15).until(wait_until_dropdown_list_loaded(count))
        except:
            self.logger.error("Dropdown list is not loaded")
        else:
            self.logger.info("Dropdown list is loaded")

    def check_found_dropdown_list_item(self, item_xpath, expected_text):
        item_text = self.get_element_text(item_xpath)
        number = self.get_element_count(item_xpath)
        if (number == 1):
            if (item_text == expected_text):
                self.logger.info("Dropdown list element has been found")
            else:
                self.logger.error(f"The text of dropdown list element is '{item_text}'")
        else:
            self.logger.error(f"The number of dropdown list elements = '{number}'")

    def select_in_dropdown_via_input(self, xpath, name):
        if (name is not None):
            self.click_xpath(xpath)
            self.logger.info(f"Dropdown list with XPATH = '{xpath}' is opened")
            self.input_data_xpath(name, f"{xpath}//input")
            self.get_element_by_xpath(f"{xpath}//input").send_keys(Keys.ENTER)

    def input_inline_xpath(self, data, xpath):
        if (data is not None):
            self.click_xpath(xpath)
            self.click_xpath(xpath)
            element = self.get_element_by_xpath(f"{xpath}//input")
            self.driver.execute_script("arguments[0].value = arguments[1]", element, "")
            self.input_data_xpath(data, f"{xpath}//input")
            element.send_keys(Keys.ENTER)

    def select_customer_shipto(self, customer_xpath=None, customer_name=None, shipto_xpath=None, shipto_name=None):
        if (customer_xpath is None):
            customer_xpath=Locator.xpath_by_count(Locator.xpath_select_box, 1)
        if (shipto_xpath is None):
            shipto_xpath=Locator.xpath_by_count(Locator.xpath_select_box, 2)
        self.wait_until_page_loaded()
        self.select_in_dropdown(customer_xpath, customer_name)
        self.wait_until_page_loaded()
        self.select_in_dropdown(shipto_xpath, shipto_name)
        self.wait_until_page_loaded()