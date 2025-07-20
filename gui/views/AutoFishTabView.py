from core.constants.GuiData import AUTO_FISH_ICON_PATH, AUTO_FISH_TITLE, AUTO_FISH_ICON_TOOLTIP, INTERNAL_PADDING, \
                                   AUTO_FRAME_CONTENT_TITLE_FONT, AUTO_FRAME_CONTENT_FONT, BUTTON_SELECT_ICON_SIZE, \
                                   ERROR_COLOR
from gui.view_models.TabContentViewModel import TabContentViewModel

from customtkinter import CTkCheckBox, CTkLabel, ThemeManager, CTkImage
from PIL import Image
class AutoFishTabView(TabContentViewModel):

    # ######################
    # Interface methods
    # ######################

    def _initialize_components(self):
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.worm_label = CTkLabel(self, 
                                   text="use worms", 
                                   font=AUTO_FRAME_CONTENT_TITLE_FONT)
        self.common_checkbox = CTkCheckBox(self, 
                                           text="Common", 
                                           font=AUTO_FRAME_CONTENT_FONT)
        
        self.rare_checkbox = CTkCheckBox(self, 
                                         text="Rare", 
                                         font=AUTO_FRAME_CONTENT_FONT)
        
        self.epic_checkbox = CTkCheckBox(self, 
                                         text="Epic", 
                                         font=AUTO_FRAME_CONTENT_FONT)

        self.legendary_checkbox = CTkCheckBox(self, 
                                              text="Legendary", 
                                              font=AUTO_FRAME_CONTENT_FONT)

        self.worm_label.grid(row=0, column=0, columnspan=2)

        # Row 0 
        self.common_checkbox.grid(row=1, column=0, padx=(INTERNAL_PADDING*5, 0),pady=(0, INTERNAL_PADDING), sticky="e")
        self.rare_checkbox.grid(row=1, column=1, pady=(0, INTERNAL_PADDING), sticky="w")

        # Row 1
        self.epic_checkbox.grid(row=2, column=0, padx=(INTERNAL_PADDING*5, 0), pady=(0, INTERNAL_PADDING), sticky="e")
        self.legendary_checkbox.grid(row=2, column=1, pady=(0, INTERNAL_PADDING), sticky="w")
    

    def can_enable(self) -> bool:
        return True

    def icon(self) -> CTkImage:
        return CTkImage(light_image=Image.open(AUTO_FISH_ICON_PATH), size=BUTTON_SELECT_ICON_SIZE)
    
    def tooltip(self) -> str:
        return AUTO_FISH_ICON_TOOLTIP
    
    def title(self) -> str:
        return AUTO_FISH_TITLE
    
    def set_tab_enabled(self, value: bool):
        self.common_checkbox.configure(state="normal" if value else "disabled")
        self.rare_checkbox.configure(state="normal" if value else "disabled")
        self.epic_checkbox.configure(state="normal" if value else "disabled")
        self.legendary_checkbox.configure(state="normal" if value else "disabled")

    def need_scrollbar(self) -> bool:
        return False
    
    # ######################
    # Default values
    # ######################

    def set_default_worm_selection(self, is_common: bool, is_rare: bool, is_epic: bool, is_legendary: bool):
        if is_common: self.common_checkbox.select()
        if is_rare: self.rare_checkbox.select()
        if is_epic: self.epic_checkbox.select()
        if is_legendary: self.legendary_checkbox.select()

    # ######################
    # Error setters
    # ######################

    def set_worms_error(self, is_error: bool):
        color = ERROR_COLOR if is_error else ThemeManager.theme["CTkCheckBox"]["border_color"]
        self.common_checkbox.configure(border_color=color)
        self.rare_checkbox.configure(border_color=color)
        self.epic_checkbox.configure(border_color=color)
        self.legendary_checkbox.configure(border_color=color)

    # ######################
    # Callback setters
    # ######################

    def set_common_worm_callback(self, callback):
        self.common_checkbox.configure(command=lambda: callback(self.common_checkbox.get()))

    def set_rare_worm_callback(self, callback):
        self.rare_checkbox.configure(command=lambda: callback(self.rare_checkbox.get()))

    def set_epic_worm_callback(self, callback):
        self.epic_checkbox.configure(command=lambda: callback(self.epic_checkbox.get()))

    def set_legendary_worm_callback(self, callback):
        self.legendary_checkbox.configure(command=lambda: callback(self.legendary_checkbox.get()))
