from src.utils.variables import PRIMARY_COLOR, SEC_COLOR, TH_COLOR
import qdarktheme

qss = f"""
    QPushButton[cssClass="SpecialButton"] {{
        color: #fff;
        background: "{PRIMARY_COLOR}";
    }}
    QPushButton[cssClass="SpecialButton"]:hover {{
        color: #fff;
        background: {SEC_COLOR};
    }}
    QPushButton[cssClass="SpecialButton"]:pressed {{
        color: #fff;
        background: {TH_COLOR};
    }}
    
"""


def setup_style():
    qdarktheme.setup_theme(
        theme="dark",
        corner_shape="rounded",
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}"
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}"
            },
        },
        additional_qss=qss
    )
