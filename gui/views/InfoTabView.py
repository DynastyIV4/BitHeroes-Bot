from core.constants.GuiData import DISCLAIMER_FONT, INFO_PATH_ICON, INFO_TOOLTIP, AUTO_FRAME_CONTENT_FONT, INFO_TITLE, WIKI_ICON_SIZE, \
                                   GITHUB_ICON_SIZE, DISCORD_ICON_PATH, DISCORD_ICON_SIZE, INFO_LABEL_TITLE, INFO_LABEL_DISCLAIMER, \
                                   DISCLAIMER_FONT, GITHUB_ICON_PATH, WIKI_ICON_PATH, GITHUB_TOOLTIP, DISCORD_TOOLTIP,  WIKI_TOOLTIP, \
                                   TOOLTIP_PARAMETERS
from gui.view_models.TabContentViewModel import TabContentViewModel
from gui.widgets.MyCTkToolTip import MyCTkToolTip

from customtkinter import CTkLabel, CTkButton, CTkImage
from PIL import Image

class InfoTabView(TabContentViewModel):

    # ######################
    # Interface methods
    # ######################

    def _initialize_components(self):
        disclaimer_title = CTkLabel(self, 
                                    text=INFO_LABEL_TITLE, 
                                    font=AUTO_FRAME_CONTENT_FONT)
        
        disclaimer_text = CTkLabel(self, 
                                   text=INFO_LABEL_DISCLAIMER, 
                                   font=DISCLAIMER_FONT, wraplength=250)

        discord_icon = CTkImage(Image.open(DISCORD_ICON_PATH), 
                                size=DISCORD_ICON_SIZE)
        
        self.discord_button = CTkButton(self, 
                                   text="", 
                                   image=discord_icon, 
                                   width=40, 
                                   fg_color=self.cget("fg_color"))
        
        github_icon = CTkImage(Image.open(GITHUB_ICON_PATH), 
                               size=GITHUB_ICON_SIZE)
        
        self.github_button = CTkButton(self, 
                                  text="", 
                                  image=github_icon, 
                                  width=40, 
                                  fg_color=self.cget("fg_color"))
        
        wiki_icon = CTkImage(Image.open(WIKI_ICON_PATH), 
                             size=WIKI_ICON_SIZE)
        
        self.wiki_button = CTkButton(self, 
                                text="", 
                                image=wiki_icon, 
                                width=40, 
                                fg_color=self.cget("fg_color"))

        self.grid_columnconfigure((0, 4), weight=5)
        self.grid_columnconfigure((1,2,3), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        disclaimer_title.grid(row=0, column=0, columnspan=5)
        disclaimer_text.grid(row=1, column=0, columnspan=5, rowspan=3)

        self.discord_button.grid(row=4,column=1, pady=10)
        self.github_button.grid(row=4,column=2, pady=10)
        self.wiki_button.grid(row=4,column=3, pady=10)

        MyCTkToolTip(self.discord_button, DISCORD_TOOLTIP, **TOOLTIP_PARAMETERS)
        MyCTkToolTip(self.github_button, GITHUB_TOOLTIP, **TOOLTIP_PARAMETERS)
        MyCTkToolTip(self.wiki_button, WIKI_TOOLTIP, **TOOLTIP_PARAMETERS)

    def can_enable(self) -> bool:
        return False

    def icon(self) -> CTkImage:
        return CTkImage(light_image=Image.open(INFO_PATH_ICON), size=(35,35))
    
    def tooltip(self) -> str:
        return INFO_TOOLTIP
    
    def title(self) -> str:
        return INFO_TITLE

    def need_scrollbar(self) -> bool:
        return False

    def set_tab_enabled(self, value: bool):
        pass

    # ######################
    # Callback setters
    # ######################

    def set_github_callback(self, callback):
        self.github_button.configure(command=callback)

    def set_discord_callback(self, callback):
        self.discord_button.configure(command=callback)

    def set_wiki_callback(self, callback):
        self.wiki_button.configure(command=callback)