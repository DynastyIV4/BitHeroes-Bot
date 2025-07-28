from core.constants.GuiData import AUTO_FRAME_MENU_SIZE, GENERAL_SETTINGS_ICON_PATH, GENERAL_SETTINGS_TOOLTIP, INTERNAL_PADDING, \
                                   AUTO_FRAME_CONTENT_TITLE_FONT, AUTO_FRAME_CONTENT_FONT, APPEARANCE_MODE, TOOLTIP_PARAMETERS, \
                                   APPEARANCE_MODE_TITLE, GENERAL_SETTINGS_TITLE, APPEARANCE_MODE_TOOLTIP, BUTTON_SELECT_ICON_SIZE, \
                                   GAME_PATH_CONTAINER_CORNER_RADIUS, GAME_PATH_CONTAINER_WIDTH, GAME_PATH_CONTAINER_HEIGHT, \
                                   GAME_PATH_CONTAINER_DARK_COLOR, GAME_PATH_CONTAINER_LIGHT_COLOR, GAME_PATH_ICON, GAME_PATH_LABEL_TITLE, \
                                   GAME_PATH_FONT, ERROR_COLOR, GAME_PATH_TOOLTIP, ALWAYS_ON_TOP_TOOLTIP
from gui.view_models.TabContentViewModel import TabContentViewModel
from gui.widgets.MyCTkToolTip import MyCTkToolTip

from customtkinter import CTkOptionMenu, CTkLabel, CTkButton, CTkImage, CTkFrame, CTkCheckBox, ThemeManager
from PIL import Image

class GeneralSettingsView(TabContentViewModel):

    # ######################
    # Interface methods
    # ######################

    def _initialize_components(self):

        self.apperance_mode_label = CTkLabel(self, 
                                             text=APPEARANCE_MODE_TITLE, 
                                             font=AUTO_FRAME_CONTENT_TITLE_FONT)
        
        self.apperance_mode_menu = CTkOptionMenu(self, 
                                                 font=AUTO_FRAME_CONTENT_FONT, 
                                                 dropdown_font=AUTO_FRAME_CONTENT_FONT, 
                                                 width = AUTO_FRAME_MENU_SIZE[0], 
                                                 height = AUTO_FRAME_MENU_SIZE[1], 
                                                 values = APPEARANCE_MODE)
        
        self.game_path_label = CTkLabel(self, 
                                        text=GAME_PATH_LABEL_TITLE, 
                                        font=AUTO_FRAME_CONTENT_TITLE_FONT)
        
        self.game_path_container = CTkFrame(self, 
                                            corner_radius=GAME_PATH_CONTAINER_CORNER_RADIUS, 
                                            width=GAME_PATH_CONTAINER_WIDTH,  
                                            height=GAME_PATH_CONTAINER_HEIGHT, 
                                            fg_color=(GAME_PATH_CONTAINER_LIGHT_COLOR, GAME_PATH_CONTAINER_DARK_COLOR))
        
        self.game_path_image = CTkImage(Image.open(GAME_PATH_ICON), 
                                        size=(31,25))
        
        self.game_path_button = CTkButton(self.game_path_container, 
                                          text="", image=self.game_path_image, 
                                          width = 30, 
                                          corner_radius= 10,
                                          fg_color=self.game_path_container.cget("fg_color"))
        
        self.text_frame = CTkFrame(self.game_path_container, 
                                   fg_color=ThemeManager.theme["CTkTextbox"]["fg_color"], 
                                   corner_radius=10)
        
        self.text_label = CTkLabel(self.text_frame, font=GAME_PATH_FONT, wraplength=280)

        self.keep_pinned_check_box = CTkCheckBox(self, 
                                                 text="Always on top", 
                                                 font=AUTO_FRAME_CONTENT_TITLE_FONT)
        
        self.apperance_mode_menu._text_label.configure(wraplength=100)

        # Hidden until it's working again
        #self.apperance_mode_label.grid(row=2, column=0, padx=INTERNAL_PADDING, pady=INTERNAL_PADDING)
        #self.apperance_mode_menu.grid(row=2, column=1, padx=INTERNAL_PADDING, pady=INTERNAL_PADDING)
        self.game_path_label.grid(row=0, column=0, columnspan=3)
        self.game_path_container.grid(row=1, column=0, columnspan=3)
        self.game_path_container.pack_propagate(False)
        self.game_path_button.pack(side="left", padx= (5,0))
        self.text_frame.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        self.text_label.pack(side="left", padx=15 )
        self.keep_pinned_check_box.grid(row=3, column=0, columnspan=3, padx=INTERNAL_PADDING, pady=20)

        MyCTkToolTip(self.apperance_mode_menu, APPEARANCE_MODE_TOOLTIP, **TOOLTIP_PARAMETERS)
        MyCTkToolTip(self.game_path_button, GAME_PATH_TOOLTIP, **TOOLTIP_PARAMETERS)
        MyCTkToolTip(self.keep_pinned_check_box, ALWAYS_ON_TOP_TOOLTIP, **TOOLTIP_PARAMETERS)
    
    def can_enable(self) -> bool:
        return False

    def icon(self) -> CTkImage:
        return CTkImage(light_image=Image.open(GENERAL_SETTINGS_ICON_PATH), size=BUTTON_SELECT_ICON_SIZE)
    
    def tooltip(self) -> str:
        return GENERAL_SETTINGS_TOOLTIP
    
    def title(self) -> str:
        return GENERAL_SETTINGS_TITLE

    def need_scrollbar(self) -> bool:
        return False
    
    def set_tab_enabled(self, is_enabled: bool):
        self.game_path_button.configure(state="normal" if is_enabled else "disabled")

    # ######################
    # Default values
    # ######################

    def set_appearance_default_selection(self, value):
        self.apperance_mode_menu.set(value)

    def set_game_path_value(self, value: str):
        self.text_label.configure(text=value)
    
    # ######################
    # Error setters
    # ######################

    def set_game_path_error(self, is_error: bool):
        self.game_path_button.configure(border_color=ERROR_COLOR if is_error else ThemeManager.theme["CTkButton"]["border_color"], border_width=2 if is_error else 0)
    
    # ######################
    # Callback setters
    # ######################

    def set_appearance_mode_callback(self, callback):
        self.apperance_mode_menu.configure(command=lambda value: callback(value))

    def set_game_path_callback(self, callback):
        self.game_path_button.configure(command=callback)
    
    def set_always_on_top_callback(self, callback):
        self.keep_pinned_check_box.configure(command=lambda: callback(self.keep_pinned_check_box.get()))    

    
    
    
