import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from glbl import Log, Error
from src.pages.waits import ElementToBeEnabled, ElementsNumberToBe
from src.pages.locator import Locator as L

class Element():
    default_timeout = 20
    enabled_timeout = 5

    def __init__(self, context):
        self.context = context
        self.driver = context.driver
        self.xpath = None

    def __call__(self, xpath):
        self.xpath = xpath
        return self

    def get(self, timeout=None, no_exception=False):
        timeout = self.default_timeout if timeout is None else timeout
        for i in range(2):
            try:
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, self.xpath)))
            except Exception as e:
                page_error = "We encountered an internal error. Please try again."
                if page_error in self.driver.page_source:
                    if i == 0:
                        self.driver.refresh()
                        Log.warning(f"The error '{page_error}' has occured. I will refresh the page and try one more time.")
                        continue
                if no_exception:
                    Log.warning(f"Cannot find element'{self.xpath}'.")
                else:
                    Error.error(f"Cannot find element'{self.xpath}'.\n{e}")

    def get_list(self):
        count = self.count()
        list_of_elements = list()
        for index in range(1, count+1):
            element = Element(self.context)
            xpath = L.get_indexed(self.xpath, index)
            list_of_elements.append(element(xpath))
        return list_of_elements

    def click(self, retries=5):
        selenium_element = self.get()
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(selenium_element).perform()
            WebDriverWait(self.driver, self.default_timeout).until(EC.element_to_be_clickable((By.XPATH, self.xpath)))
        except Exception as e:
            Error.error(f"Element '{self.xpath}' is not clickable.\n{e}")

        while retries:
            try:
                selenium_element.click()
            except Exception as e:
                if retries > 1:
                    retries -= 1
                    Log.warning(f"Cannot click element '{self.xpath}'. Next try in 1 second")
                    time.sleep(1)
                else:
                    Error.error(e)
            else:
                Log.info(f"Element '{self.xpath}' is clicked")
                break

    def enter(self, text, hide_log=None):
        selenium_element = self.get()
        length = len(selenium_element.get_attribute("value"))
        for _ in range(length):
            selenium_element.send_keys(Keys.BACKSPACE)
        try:
            selenium_element.send_keys(text)
        except Exception as e:
            Error.error(f"Cannot enter '{text}' into element '{self.xpath}'.\n{e}")
        else:
            if hide_log:
                text = "***"
            Log.info(f"Data '{text}' entered into element '{self.xpath}'")

    def text(self):
        selenium_element = self.get()
        return selenium_element.text

    def count(self):
        try:
            elements = self.driver.find_elements("xpath", self.xpath)
        except Exception as e:
            Error.error(f"Elements '{self.xpath}' do not found.\n{e}")
        else:
            count = len(elements)
            Log.info(f"There are '{count}' elements '{self.xpath}'")
            return count

    def is_enabled(self):
        selenium_element = self.get()
        return selenium_element.is_enabled()

    def wait_until_enabled(self):
        self.get()
        WebDriverWait(self.driver, self.enabled_timeout).until(ElementToBeEnabled(self.xpath))

    def wait_until_disabled(self):
        self.get()
        WebDriverWait(self.driver, self.enabled_timeout).until_not(ElementToBeEnabled(self.xpath))

    def wait_until_disappeared(self):
        try:
            WebDriverWait(self.driver, self.default_timeout).until_not(EC.presence_of_element_located((By.XPATH, self.xpath)))
        except Exception as e:
            Error.error(f"Element '{self.xpath}' is still present.\n{e}")

    def wait_for_not_appeared(self, timeout=5):
        try:
            self.get(timeout=timeout, no_exception=True)
        except:
            pass
        else:
            Error.error(f"Element '{self.xpath}' is appeared")

    def wait_elements_number(self, number, timeout=None):
        timeout = self.default_timeout if timeout is None else timeout
        try:
            WebDriverWait(self.driver, timeout).until(ElementsNumberToBe(self.xpath, number))
        except Exception as e:
            Error.error(f"Number of elements is incorrect: should be '{number}', now '{self.count()}'.\n{e}")
        else:
            Log.info("Number of elements is correct")
