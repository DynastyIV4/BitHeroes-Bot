from core.constants.GuiData import ON_BUTTON_PATH, OFF_BUTTON_PATH, ON_DARK_BUTTON_PATH, OFF_DARK_BUTTON_PATH, ON_OFF_SIZE, ON_OFF_TOOLTIP, TOOLTIP_PARAMETERS
from gui.widgets.CTkImagePressedButton import CTkImagePressedButton
from gui.widgets.MyCTkToolTip import MyCTkToolTip


class OnOffButtonView(CTkImagePressedButton):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, OFF_BUTTON_PATH, OFF_DARK_BUTTON_PATH, ON_BUTTON_PATH, ON_DARK_BUTTON_PATH, ON_OFF_SIZE  ,*args, **kwargs)
        MyCTkToolTip(self, ON_OFF_TOOLTIP, **TOOLTIP_PARAMETERS)

    def set_callback(self, callback):
        self.configure(command=callback)