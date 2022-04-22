from pages.element import Element

class UI():
    def __init__(self, context):
        self.context = context

    def element(self, xpath):
        return Element(self.context, xpath)