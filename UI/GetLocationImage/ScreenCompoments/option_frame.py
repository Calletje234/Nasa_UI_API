from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import (
    QCheckBox, QLineEdit, QDateEdit,
    QGridLayout,
)


class OptionGather:
    def create_checkbox(self):
        self.lat_checkbox = QCheckBox(text="Latitude")
        self.lon_checkbox = QCheckBox(text="Longitude")
        self.dimensions_checkbox = QCheckBox(text="Dimensions")
        self.date_checkbox = QCheckBox(text="Date")

    def create_entrie(self):
        self.lat_entrie = QLineEdit()
        self.lon_entrie = QLineEdit()
        self.dimensions_entrie = QLineEdit()
        self.lat_entrie.setEnabled(False)
        self.lon_entrie.setEnabled(False)
        self.dimensions_entrie.setEnabled(False)
    
    def create_agenda_widget(self):
        self.date_dateEntry = QDateEdit(calendarPopup=True, date=QDate.currentDate())
        self.date_dateEntry.setDisplayFormat("yyyy-MM-dd")
        self.date_dateEntry.setEnabled(False)

    def create_frame(self):
        self.grid_layout = QGridLayout()

    def add_items_to_frame(self):
        self.grid_layout.addWidget(self.lat_checkbox, 0, 0)
        self.grid_layout.addWidget(self.lat_entrie, 0, 1)
        self.grid_layout.addWidget(self.lon_checkbox, 1, 0)
        self.grid_layout.addWidget(self.lon_entrie, 1, 1)
        self.grid_layout.addWidget(self.dimensions_checkbox, 2, 0)
        self.grid_layout.addWidget(self.dimensions_entrie, 2, 1)
        self.grid_layout.addWidget(self.date_checkbox, 3, 0)
        self.grid_layout.addWidget(self.date_dateEntry, 3, 1)

    def create_toggle_value(self):
        initial_value = 0
        self.lat = initial_value
        self.lon = initial_value
        self.dimension = initial_value
        self.date = initial_value

    def set_checkbox_functions(self):
        self.lat_checkbox.toggled.connect(lambda: self.set_checkbox_states("lat"))
        self.lon_checkbox.toggled.connect(lambda: self.set_checkbox_states("lon"))
        self.dimensions_checkbox.toggled.connect(lambda: self.set_checkbox_states("dimen"))
        self.date_checkbox.toggled.connect(lambda: self.set_checkbox_states("date"))

    def set_checkbox_states(self, checkbox_type):
        if checkbox_type == "lat":
            if self.lat == 0:
                self.lat_entrie.setEnabled(True)
                self.lat = 1
            else:
                self.lat_entrie.setEnabled(False)
                self.lat_entrie.clear()
                self.lat = 0
        elif checkbox_type == "lon":
            if self.lon == 0:
                self.lon_entrie.setEnabled(True)
                self.lon = 1
            else:
                self.lon_entrie.setEnabled(False)
                self.lon_entrie.clear()
                self.lon = 0
        elif checkbox_type == "dimen":
            if self.dimension == 0:
                self.dimensions_entrie.setEnabled(True)
                self.dimension = 1
            else:
                self.dimension == 1
                self.dimensions_entrie.setEnabled(False)
                self.dimensions_entrie.clear()
                self.dimension = 0
        elif checkbox_type == "date":
            if self.date == 0:
                self.date_dateEntry.setEnabled(True)
                self.date = 1
            else:
                self.date_dateEntry.setEnabled(False)
                self.date = 0

    def get_frame(self):
        self.create_checkbox()
        self.create_entrie()
        self.create_agenda_widget()
        self.create_toggle_value()
        self.create_frame()
        self.add_items_to_frame()
        self.set_checkbox_functions()
        return self.grid_layout