class Textbox:
    def __init__(self, textbox_element):
        self.element = textbox_element

    def send_keys(self, text):
        self.element.send_keys(text)

    def is_enabled(self):
        self.element.is_enabled()