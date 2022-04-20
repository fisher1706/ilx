class UI():
    def __init__(self, context):
        self.context = context
        self.driver = context.driver
        self.url = self.context.session_context.url
        self.logger = context.logger
        self.data = context.data