from PyQt5.QtWidgets import (
    QPushButton, QLabel, QGridLayout
)

from GetLocationImage.locationImageScreen import LocationImage


class OptionFrame:
    def __init__(self) -> None:
        self.buttons_mapping = []
        self.row_counting = 0
        self.column_counting = 0

    def create_buttons(self):
        run_button = QPushButton("Run")
        return run_button

    def create_mapping(self, api_description, button):
        mapping  = {}
        mapping["name"] = api_description
        mapping["button"] = button
        self.buttons_mapping.append(mapping)

    def create_lable(self, option_lable):
        option_lable = QLabel(option_lable)
        return option_lable

    def create_frame(self):
        self.options_frame = QGridLayout()

    def create_options(self):
        self.create_mapping("Get Location Image", self.create_buttons())

    def create_command_per_button(self):
        for items in self.buttons_mapping:
            if items["name"] == "Get Location Image":
                button = items["button"]
                button.clicked.connect(lambda: self.open_location_imager())

    def open_location_imager(self):
        location_screen = LocationImage()
        location_screen.show()
    
    def add_mapping_to_frame(self):
        for items in self.buttons_mapping:
            lable = items["name"]
            button =  items["button"]
            self.options_frame.addWidget(self.create_lable(lable), self.row_counting, self.column_counting)
            self.options_frame.addWidget(button, self.row_counting, self.column_counting+1)
            self.row_counting += 1
    
    def get_frame(self):
        self.create_options()
        self.create_frame()
        self.create_command_per_button()
        self.add_mapping_to_frame()
        return self.options_frame
