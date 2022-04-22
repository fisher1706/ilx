class ElementToBeEnabled(): #pylint: disable=C0103
    def __init__(self, xpath):
        self.xpath = xpath

    def __call__(self, driver):
        element = driver.find_element_by_xpath(self.xpath)
        if element.is_enabled():
            return True
        return False
