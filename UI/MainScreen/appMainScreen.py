from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout
)

from MainScreen.screencomponents.bott_frame import BottumFrame
from MainScreen.screencomponents.options_frame import OptionFrame

class MainScreen(QWidget):
    def __init__(self, parent = None) -> None:
        super(MainScreen, self).__init__(parent)
        self.setWindowTitle("NASA Info")
        self.setGeometry(800, 800, 650, 650)
        self.setLayout(self.construct_window())
        
    def construct_window(self):
        main_frame = QVBoxLayout()
        button_creator = BottumFrame()
        option_creator = OptionFrame()
        main_frame.addLayout(option_creator.get_frame())
        main_frame.addLayout(button_creator.get_frame(self))
        return main_frame
