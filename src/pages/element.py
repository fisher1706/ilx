import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from glbl import LOG, ERROR

class Element():
    def __init__(self, context, xpath):
        self.context = context
        self.driver = context.driver
        self.timeout = 20
        self.xpath = xpath

    def get(self):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.XPATH, self.xpath)))

    def click(self, retries=5):
        element = self.get()
        while(retries):
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
                WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable((By.XPATH, self.xpath)))
                element.click()
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
