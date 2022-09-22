from PyQt5.QtWidgets import (
    QPushButton, QHBoxLayout
)


class BottomFrame:
    def create_buttons(self):
        self.cancel_button = QPushButton("Cancel")
        self.run_button = QPushButton("Run")

    def create_frame(self):
        self.button_frame = QHBoxLayout()

    def create_command_button(self, main, options_object):
        self.cancel_button.clicked.connect(lambda: self.close_app(main))
        self.run_button.clicked.connect(lambda: self.set_options(options_object))

    def close_app(self, main):
        main.close()

    def set_options(self, options_object):
        self.options_list = []
        latitude = options_object.get_lat_entrie()
        longtitude = options_object.get_lon_entrie()
        dimensions = options_object.get_dimensions_entrie()
        date = options_object.get_date_entrie()
        self.options_list.append(latitude)
        self.options_list.append(longtitude)
        self.options_list.append(dimensions)
        self.options_list.append(date)

    def get_options(self):
        return self.options_list
    
    def add_buttons_to_frame(self):
        self.button_frame.addWidget(self.run_button)
        self.button_frame.addWidget(self.cancel_button)

    def get_frame(self, main, options_object):
        self.create_buttons()
        self.create_frame()
        self.create_command_button(main, options_object)
        self.add_buttons_to_frame()
        return self.button_frame
