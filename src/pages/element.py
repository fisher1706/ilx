import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from glbl import Log, Error

class Element():
    def __init__(self, context):
        self.timeout = 20
        self.context = context
        self.driver = context.driver

    def __call__(self, xpath):
        self.xpath = xpath
        return self

    def get(self):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.XPATH, self.xpath)))

    def click(self, retries=5):
        selenium_element = self.get()
        while(retries):
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(selenium_element).perform()
                WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.XPATH, self.xpath)))
                selenium_element.click()
            except Exception as e:
                if retries > 0:
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
        try:
            selenium_element.send_keys(text)
        except Exception as e:
            Error.error(f"Cannot enter '{text}' into element '{self.xpath}'.\n{e}")
        else:
            if hide_log:
                text = "***"
            Log.info(f"Data '{text}' entered into element '{self.xpath}'")

    def clear(self):
        selenium_element = self.get()
        length = len(selenium_element.get_attribute("value"))
        for _ in range(length):
            selenium_element.send_keys(Keys.BACKSPACE)

    def text(self):
        selenium_element = self.get()
        return selenium_element.text

    def count(self):
        try:
            elements = self.driver.find_elements_by_xpath(self.xpath)
        except Exception as e:
            Error.error(f"Elements '{self.xpath}' do not found.\n{e}")
        else:
            count = len(elements)
            Log.info(f"There are '{count}' elements '{self.xpath}'")
            return count

    def is_enabled(self):
        selenium_element = self.get()
        return selenium_element.is_enabled()

