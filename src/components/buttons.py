from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from src.utils.variables import MEDIUM_FONT_SIZE
from src.utils.utils import is_num_or_dot, is_empty
from src.components.display import Display


class Button(QPushButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()

    def config_style(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):

    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]

        self.display = display

        self._make_grid()

    def _make_grid(self):
        for i, line in enumerate(self._grid_mask):
            for j, btn in enumerate(line):
                button = Button(btn)

                if not is_num_or_dot(btn) and not is_empty(btn):
                    button.setProperty('cssClass', 'SpecialButton')

                self.addWidget(button, i, j)
                slot = self._make_btn_display_slot(
                    self._insert_button_text,
                    button
                )
                button.clicked.connect(slot)

    def _make_btn_display_slot(self, func, *args, **kwargs):
        @Slot(bool)
        def real_slot(checked):
            func(checked, *args, **kwargs)
        return real_slot

    def _insert_button_text(self, checked, button):
        btn_txt = button.text()
        self.display.insert(btn_txt)
