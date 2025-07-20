from core.constants.GuiData import TOOLTIP_FONT, ERROR_COLOR
from gui.widgets.MyCTkToolTip import MyCTkToolTip

from abc import abstractmethod, ABC
from customtkinter import CTkScrollableFrame, CTkImage, CTkBaseClass, CTkSwitch, CTkButton, ThemeManager

class TabContentViewModel(ABC, CTkScrollableFrame):

    def __init__(self, master: CTkBaseClass, toggle_switch: CTkSwitch, *args, **kwargs):
        super().__init__(master, fg_color=master.cget("fg_color"),*args, **kwargs)
        self.toggle_switch = toggle_switch
        self.button: CTkButton = None
        self.enabled_callback = None
        self._is_enabled: bool = False
        self._initialize_components()
        
    def set_tab_error(self, is_error: bool):
        color = ERROR_COLOR if is_error else ThemeManager.theme["CTkFrame"]["border_color"]
        border_width = 2 if is_error else 0
        self.button.configure(border_width=border_width, border_color=color)

    def attach_button(self, button: CTkButton):
        self.button = button
        MyCTkToolTip(button, self.tooltip(), font=TOOLTIP_FONT)

    @property
    def is_enabled(self) -> bool:
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self, is_enabled: bool):
        self._is_enabled = is_enabled
        self.set_tab_enabled(is_enabled)
    
    def set_switch_enabled(self, is_enabled: bool):
        self.toggle_switch.configure(state="disabled" if not is_enabled else "normal")

    @abstractmethod
    def _initialize_components(self):
        pass

    @abstractmethod
    def can_enable(self) -> bool:
        pass

    @abstractmethod
    def icon(self) -> CTkImage:
        pass

    @abstractmethod
    def tooltip(self) -> str:
        pass

    @abstractmethod
    def title(self) -> str:
        pass
    
    @abstractmethod
    def need_scrollbar(self) -> bool:
        pass

    @abstractmethod
    def set_tab_enabled(self, value: bool):
        pass