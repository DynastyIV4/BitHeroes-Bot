from core.constants.GuiData import AUTO_FRAME_MENU_SIZE, AUTO_QUEST_ICON_TOOLTIP, AUTO_QUEST_DIFFICULTY, DIFFICULTY_TOOLTIP, \
                                   AUTO_QUEST_ICON_PATH, AUTO_QUEST_TITLE, INTERNAL_PADDING, AUTO_FRAME_CONTENT_TITLE_FONT, AUTO_FRAME_CONTENT_FONT, \
                                   PERSUADE_TOOLTIP, TOOLTIP_PARAMETERS, DUNGEON_TOOLTIP, ZONE_TOOLTIP, DECLINE_TOOLTIP, FAMILIAR_TOOLTIP, \
                                   BUTTON_SELECT_ICON_SIZE, FAMILIAR_LISTBOX_WIDTH, ERROR_COLOR
from gui.view_models.TabContentViewModel import TabContentViewModel
from gui.widgets.MyCTkListbox import MyCTkListbox
from gui.widgets.MyCTkToolTip import MyCTkToolTip

from customtkinter import CTkOptionMenu, CTkCheckBox, CTkLabel, ThemeManager, CTkImage, CTkSegmentedButton
from PIL import Image

class AutoQuestTabView(TabContentViewModel):
    
    # ######################
    # Interface methods
    # ######################
    
    def _initialize_components(self):

        self.zone_label = CTkLabel(self, 
                                   text="Zone", 
                                   font=AUTO_FRAME_CONTENT_TITLE_FONT)

        self.dungeon_menu = CTkOptionMenu(self, 
                                          font=AUTO_FRAME_CONTENT_FONT, 
                                          dropdown_font=AUTO_FRAME_CONTENT_FONT, 
                                          width=AUTO_FRAME_MENU_SIZE[0], 
                                          height=AUTO_FRAME_MENU_SIZE[1])

        self.zone_menu = CTkOptionMenu(self, 
                                       font=AUTO_FRAME_CONTENT_FONT, 
                                       dropdown_font=AUTO_FRAME_CONTENT_FONT, 
                                       width=AUTO_FRAME_MENU_SIZE[0], 
                                       height=AUTO_FRAME_MENU_SIZE[1])
        
        self.difficulty_label = CTkLabel(self, 
                                       text="Difficulty", 
                                       font=AUTO_FRAME_CONTENT_TITLE_FONT)
        
        self.difficulty_menu = CTkSegmentedButton(self, 
                                                    font=AUTO_FRAME_CONTENT_FONT, 
                                                    width=AUTO_FRAME_MENU_SIZE[0], 
                                                    height=AUTO_FRAME_MENU_SIZE[1], 
                                                    values=AUTO_QUEST_DIFFICULTY)
        
        self.familiar_label = CTkLabel(self, 
                                       text="Familiar", 
                                       font=AUTO_FRAME_CONTENT_TITLE_FONT)
        
        self.familiar_list = MyCTkListbox(self, 
                                          font=AUTO_FRAME_CONTENT_FONT, 
                                          width=FAMILIAR_LISTBOX_WIDTH, 
                                          height=AUTO_FRAME_MENU_SIZE[1]*2, 
                                          multiple_selection=True,
                                          button_height=AUTO_FRAME_CONTENT_FONT[1])
        
        self.persuade_checkbox = CTkCheckBox(self, 
                                             text="Auto Persuade", 
                                             font=AUTO_FRAME_CONTENT_FONT, 
                                             width=self.dungeon_menu._current_width)
        
        self.decline_checkbox = CTkCheckBox(self, 
                                            text="Auto Decline", 
                                            font=AUTO_FRAME_CONTENT_FONT, 
                                            width=self.dungeon_menu._current_width)
        
        self.zone_menu._text_label.configure(wraplength=AUTO_FRAME_MENU_SIZE[0])
        self.dungeon_menu._text_label.configure(wraplength=AUTO_FRAME_MENU_SIZE[0])

        self.zone_label.grid(row=0, column=0, columnspan=2)
        self.zone_menu.grid(row=1, column=0, padx=INTERNAL_PADDING, pady=(0, INTERNAL_PADDING))
        self.dungeon_menu.grid(row=1, column=1, padx=INTERNAL_PADDING, pady=(0, INTERNAL_PADDING), sticky="w")
        self.difficulty_label.grid(row=2, column=0, columnspan=2)
        self.difficulty_menu.grid(row=3, column=0, columnspan=2, padx=INTERNAL_PADDING, pady=(0, INTERNAL_PADDING))

        self.familiar_label.grid(row=4, column=0, columnspan=2)
        self.familiar_list.grid(row=5, column=0, rowspan = 2)
        self.persuade_checkbox.grid(row=5, column=1, pady=(0, INTERNAL_PADDING))
        self.decline_checkbox.grid(row=6, column=1, pady=(0, INTERNAL_PADDING))

        MyCTkToolTip(self.dungeon_menu, DUNGEON_TOOLTIP, **TOOLTIP_PARAMETERS)
        MyCTkToolTip(self.zone_menu, ZONE_TOOLTIP, **TOOLTIP_PARAMETERS)
        MyCTkToolTip(self.persuade_checkbox, PERSUADE_TOOLTIP, **TOOLTIP_PARAMETERS)
        MyCTkToolTip(self.decline_checkbox, DECLINE_TOOLTIP, **TOOLTIP_PARAMETERS)
        MyCTkToolTip(self.familiar_list, FAMILIAR_TOOLTIP, **TOOLTIP_PARAMETERS)
        MyCTkToolTip(self.difficulty_menu, DIFFICULTY_TOOLTIP, **TOOLTIP_PARAMETERS)

    def can_enable(self) -> bool:
        return True

    def icon(self) -> CTkImage:
        return CTkImage(light_image=Image.open(AUTO_QUEST_ICON_PATH), size=BUTTON_SELECT_ICON_SIZE)
    
    def tooltip(self) -> str:
        return AUTO_QUEST_ICON_TOOLTIP
    
    def title(self) -> str:
        return AUTO_QUEST_TITLE
    
    def set_tab_enabled(self, is_enabled: bool):
        self.dungeon_menu.configure(state="normal" if is_enabled else "disabled")
        self.zone_menu.configure(state="normal" if is_enabled else "disabled")
        self.persuade_checkbox.configure(state="normal" if is_enabled else "disabled")
        self.decline_checkbox.configure(state="normal" if is_enabled else "disabled")
        self.familiar_list.configure(state="normal" if is_enabled else "disabled")
        self.difficulty_menu.configure(state="normal" if is_enabled else "disabled")

    def need_scrollbar(self) -> bool:
        return True
    
    # ######################
    # Default values
    # ######################

    def set_zone_default_values(self, values: list[str]):
        self.zone_menu.configure(values = values)

    def set_zone_default_selection(self, zone_index: int):
        self.zone_menu.set(self.zone_menu.cget("values")[zone_index])

    def set_dungeon_default_values(self, values: list[str]):
        self.dungeon_menu.configure(values = values)

    def set_dungeon_default_selection(self, dungeon_index: int):
        self.dungeon_menu.set(self.dungeon_menu.cget("values")[dungeon_index])
    
    def set_persuade_default_value(self, value: bool):
        if value: self.persuade_checkbox.select()
    
    def set_decline_default_value(self, value: bool):
        if value: self.decline_checkbox.select()
    
    def set_familiar_default_selection(self, value):
        self.familiar_list.multiple_select(value)

    def set_familiar_values(self, familiars_name: list[str], familiars_text_color: list[str]):
        self.familiar_list.delete("all")
        for familiar_name, color in zip(familiars_name, familiars_text_color):
            self.familiar_list.insert("end", familiar_name, custom_text_color=color)
    
    def set_difficulty_default_value(self, value):
        self.difficulty_menu.set(value)
    
    # ######################
    # Enabled setters
    # ######################

    def set_familiar_enabled(self, is_enabled: bool):
        self.familiar_list.configure(state="normal" if is_enabled else "disabled")
    
    def set_decline_enabled(self, is_enabled: bool):
        self.decline_checkbox.configure(state="normal" if is_enabled else "disabled")

    # ######################
    # Error setters
    # ######################

    def set_zone_error(self, is_error: bool):
        self.zone_menu.configure(button_color=ERROR_COLOR if is_error else ThemeManager.theme["CTkOptionMenu"]["button_color"])

    def set_dungeon_error(self, is_error: bool):
        self.dungeon_menu.configure(button_color=ERROR_COLOR if is_error else ThemeManager.theme["CTkOptionMenu"]["button_color"])

    def set_familiar_error(self, is_error: bool):
        self.familiar_list.configure(border_color=ERROR_COLOR if is_error else ThemeManager.theme["CTkFrame"]["border_color"])

    # ######################
    # Callback setters
    # ######################

    def set_persuade_callback(self, callback):
        self.persuade_checkbox.configure(command=lambda: callback(self.persuade_checkbox.get()))    
        
    def set_decline_callback(self, callback):
        self.decline_checkbox.configure(command=lambda: callback(self.decline_checkbox.get()))

    def set_dungeon_menu_callback(self, callback):
        self.dungeon_menu.configure(command=lambda value: callback(self.dungeon_menu.cget("values").index(value)))    

    def set_zone_menu_callback(self, callback):
        self.zone_menu.configure(command=lambda value: callback(self.zone_menu.cget("values").index(value)))

    def set_familiar_menu_callback(self, callback):
        self.familiar_list.configure(command=lambda value: callback(value))    
    
    def set_difficulty_callback(self, callback):
        self.difficulty_menu.configure(command=lambda value: callback(value))    

