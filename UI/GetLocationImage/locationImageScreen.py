from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout
)

from GetLocationImage.ScreenCompoments.bottom_buttons import BottomFrame
from GetLocationImage.ScreenCompoments.option_frame import OptionGather

class LocationImage(QWidget):
    def __init__(self, parent = None) -> None:
        super(LocationImage, self).__init__(parent)
        self.setGeometry(600, 600, 350, 500)
        self.setWindowTitle("Location Imaging")
        self.setLayout(self.construct_window())

    def construct_window(self):
        main_frame = QVBoxLayout()
        buttom_creator = BottomFrame()
        option_creator = OptionGather()
        main_frame.addLayout(option_creator.get_frame())
        main_frame.addLayout(buttom_creator.get_frame(self))
        return main_frame