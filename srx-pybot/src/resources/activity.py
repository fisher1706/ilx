from src.resources.locators import Locators
from src.resources.logger import Logger
from src.resources.url import URL
from src.resources.variables import Variables
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys
import argparse

class Activity():
    def __init__(self):
        self.arg_browser, self.arg_environment = self.get_args()
        self.locators = Locators()
        self.logger = Logger()
        self.variables = Variables(self.arg_environment)
        self.url = URL(self.arg_environment)
        self.logger.expected_error_series = self.variables.expected_error_series
        self.browser_config(self.arg_browser)

    def get_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--browser", "-b", help="Set browser: "+
                            "[ff] - Firefox; "+
                            "[ffhl] - Firefox headless")
        parser.add_argument("--environment", "-e", help="Set environment : [dev]; [staging]")
        args = parser.parse_args()
        return args.browser, args.environment

    def browser_config(self, browser):
        if (browser == 'ff' or browser == None):
            self.driver = webdriver.Firefox()
        elif (browser == 'ffhl'):
            options = Options()
            options.headless = True
            self.driver = webdriver.Firefox(options=options)
        else:
            pass
        self.driver.implicitly_wait(self.variables.default_wait)

    def finish_activity(self):
        self.driver.close()