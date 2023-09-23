from src.windows.main_window import MainWindow
from src.components.display import Display
from src.components.info import Info
from PySide6.QtWidgets import QApplication
from src.components.variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
from src.components.styles import setup_style
import sys


if __name__ == '__main__':

    app = QApplication(sys.argv)
    setup_style()
    window = MainWindow()

    # define the icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # info
    info = Info('25.53 ^ 5')
    window.add_widget(info)

    # display
    display = Display()
    window.add_widget(display)

    # executes the app
    window.set_default_parameters()
    window.show()
    app.exec()
