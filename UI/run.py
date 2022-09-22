from PyQt5.QtWidgets import QApplication
from MainScreen.appMainScreen import MainScreen


if __name__ == "__main__":
    app = QApplication([])
    window = MainScreen()
    window.show()
    app.exec_()