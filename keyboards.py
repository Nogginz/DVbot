import json

class KeyBoard:

    def __init__(self, buttons=None):
        self.buttons = []
        if not (buttons is None):
            for button in buttons:
                self.add_button(button)
        self.base = {"one_time": True,
                     "buttons": self.buttons
                     }
        self.keyboard = json.dumps(self.base)

    def add_button(self, text, colour="negative"):
        self.buttons.append([{"action": {"type": "text",
                                         "label": text
                                         },
                              "color": colour}])

    def create_keyboard(self):
        self.keyboard = json.dumps(self.base)
        return self.keyboard

    def get_keyboard(self):
        return self.keyboard
