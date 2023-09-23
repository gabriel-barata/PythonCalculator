from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt
from src.utils.variables import SMALL_FONT_SIZE


class Info(QLabel):

    def __init__(self, text: str, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(text, parent, *args, **kwargs)
        self.config_style()

    def config_style(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
