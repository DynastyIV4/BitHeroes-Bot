from core.constants.GuiData import ENABLE_DEBUG_LOGGING_TITLE, ADVANCED_SETTINGS_ICON_PATH, ADVANCED_SETTINGS_TOOLTIP, ENABLE_DEBUG_LOGGING_TOOLTIP, \
                                   AUTO_FRAME_CONTENT_FONT, ENABLE_EXPORT_LOGGING_TITLE, ENABLE_EXPORT_LOGGING_TOOLTIP, TOOLTIP_PARAMETERS, \
                                   ADVANCED_SETTINGS_TITLE, BUTTON_SELECT_ICON_SIZE, BIG_TOOLTIP_PARAMETERS
from gui.view_models.TabContentViewModel import TabContentViewModel
from gui.widgets.MyCTkToolTip import MyCTkToolTip

from customtkinter import  CTkImage, CTkCheckBox
from PIL import Image

class AdvancedSettingsView(TabContentViewModel):

    # ######################
    # Interface methods
    # ######################

    def _initialize_components(self):

        self.enable_debug_logging = CTkCheckBox(self, 
                                                text=ENABLE_DEBUG_LOGGING_TITLE, 
                                                font=AUTO_FRAME_CONTENT_FONT)

        self.enable_export_logging = CTkCheckBox(self, 
                                                 text=ENABLE_EXPORT_LOGGING_TITLE, 
                                                 font=AUTO_FRAME_CONTENT_FONT)
        
        self.enable_debug_logging._text_label.configure(wraplength = 120)
        self.enable_export_logging._text_label.configure(wraplength = 120)
        
        self.enable_debug_logging.grid(row=0, column=0, padx= 40, pady=15)
        self.enable_export_logging.grid(row=0, column=1, pady=15)

        MyCTkToolTip(self.enable_debug_logging, ENABLE_DEBUG_LOGGING_TOOLTIP, **TOOLTIP_PARAMETERS)
        MyCTkToolTip(self.enable_export_logging, ENABLE_EXPORT_LOGGING_TOOLTIP, **BIG_TOOLTIP_PARAMETERS)
    
    def can_enable(self) -> bool:
        return False

    def icon(self) -> CTkImage:
        return CTkImage(light_image=Image.open(ADVANCED_SETTINGS_ICON_PATH), size=BUTTON_SELECT_ICON_SIZE)
    
    def tooltip(self) -> str:
        return ADVANCED_SETTINGS_TOOLTIP
    
    def title(self) -> str:
        return ADVANCED_SETTINGS_TITLE

    def need_scrollbar(self) -> bool:
        return False
    
    def set_tab_enabled(self, is_enabled: bool):
        self.enable_debug_logging.configure(state="normal" if is_enabled else "disabled")
        self.enable_export_logging.configure(state="normal" if is_enabled else "disabled")

    # ######################
    # Default values
    # ######################

    def set_debug_logging_default_selection(self, is_selected: bool):
        if is_selected: self.enable_debug_logging.select()

    def set_export_logging_default_selection(self, is_selected: bool):
        if is_selected: self.enable_export_logging.select()
    
    # ######################
    # Callback setters
    # ######################

    def set_debug_logging_callback(self, callback):
        self.enable_debug_logging.configure(command=lambda: callback(self.enable_debug_logging.get()))

    def set_export_logging_callback(self, callback):
        self.enable_export_logging.configure(command=lambda: callback(self.enable_export_logging.get()))
    