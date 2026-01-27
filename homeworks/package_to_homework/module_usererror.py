
class UserError(Exception):
    def __init__(self, message, num=None):
        super().__init__()
        self.message = message
        self.num = num

    def get_exception_message(self):
        return self.message