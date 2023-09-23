from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout)


class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # setting the default window
        self.cw = QWidget()
        self.layout = QVBoxLayout()
        self.cw.setLayout(self.layout)
        self.setCentralWidget(self.cw)
        self.setWindowTitle('Calculadora')

    def set_default_parameters(self) -> None:
        # fixes the size
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def add_widget(self, widget: QWidget):
        self.layout.addWidget(widget)

    def add_layout(self, layout):
        self.layout.addLayout(layout)
