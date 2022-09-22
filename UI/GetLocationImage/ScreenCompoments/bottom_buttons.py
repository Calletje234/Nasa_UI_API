from PyQt5.QtWidgets import (
    QPushButton, QHBoxLayout
)


class BottomFrame:
    def create_buttons(self):
        self.cancel_button = QPushButton("Cancel")
        self.run_button = QPushButton("Run")

    def create_frame(self):
        self.button_frame = QHBoxLayout()

    def create_command_button(self, main):
        self.cancel_button.clicked.connect(lambda: self.close_app(main))

    def close_app(self, main):
        main.close()
    
    def add_buttons_to_frame(self):
        self.button_frame.addWidget(self.run_button)
        self.button_frame.addWidget(self.cancel_button)

    def get_frame(self, main):
        self.create_buttons()
        self.create_frame()
        self.create_command_button(main)
        self.add_buttons_to_frame()
        return self.button_frame
