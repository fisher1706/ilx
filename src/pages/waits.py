class ElementToBeEnabled():
    def __init__(self, xpath):
        self.xpath = xpath

    def __call__(self, driver):
        element = driver.find_element_by_xpath(self.xpath)
        if element.is_enabled():
            return True
        return False

class PageUrlToBe():
    def __init__(self, url):
        self.url = url

    def __call__(self, driver):
        if driver.current_url == self.url:
            return True
        return False

class ElementsNumberToBe():
    def __init__(self, xpath, number):
        self.number = number
        self.xpath = xpath

    def __call__(self, driver):
        elements = driver.find_elements_by_xpath(self.xpath)
        count = len(elements)
        if count == self.number:
            return True
        return False

class TextToBeEmpty():
    def __init__(self, xpath):
        self.xpath = xpath

    def __call__(self, driver):
        text = driver.find_element_by_xpath(self.xpath).text
        if text == "":
            return True
        return False
