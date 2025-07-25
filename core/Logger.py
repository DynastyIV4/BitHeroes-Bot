from core.Observer import Publisher

class Logger(Publisher):

    def __init__(self):
        super().__init__()
        self.last_line_printed: str = ""

    def print(self, text: str):
        self.last_line_printed = text
        self.notify()
    