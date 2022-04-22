import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from glbl import LOG, ERROR, DRIVER

class Element():
    def __init__(self, xpath):
        self.timeout = 20
        self.xpath = xpath

    def get(self):
        return WebDriverWait(DRIVER, self.timeout).until(EC.presence_of_element_located((By.XPATH, self.xpath)))

    def click(self, retries=5):
        selenium_element = self.get()
        while(retries):
            try:
                actions = ActionChains(DRIVER)
                actions.move_to_element(selenium_element).perform()
                WebDriverWait(DRIVER, self.timeout).until(EC.element_to_be_clickable((By.XPATH, self.xpath)))
                selenium_element.click()
            except Exception as e:
                if retries > 0:
                    retries -= 1
                    LOG.warning(f"Cannot click element '{self.xpath}'. Next try in 1 second")
                    time.sleep(1)
                else:
                    ERROR(e)
            else:
                LOG.info(f"Element '{self.xpath}' is clicked")
                break
