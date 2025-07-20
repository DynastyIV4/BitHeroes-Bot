from core.constants.GuiData import BUTTON_SELECT_BAR_WIDTH, BUTTON_SELECT_BAR_HEIGHT, AUTO_FRAME_CORNER_RADIUS, TOOLTIP_FONT, \
                                   BUTTON_HEIGHT, BUTTON_WIDTH, SELECT_BAR_PADDING, BUTTON_CORNER_RADIUS, SELECT_BAR_DARK_COLOR, \
                                   AUTO_FRAME_HEIGHT, BUTTON_PADDING, SELECT_BAR_CORNER_RADIUS, SELECT_BAR_LIGHT_COLOR, \
                                   ENABLE_SWITCH_TOOLTIP, TOOLTIP_PARAMETERS
from gui.widgets.CTkIconButton import CTkIconButton
from gui.view_models.TabContentViewModel import TabContentViewModel
from gui.widgets.MyCTkToolTip import MyCTkToolTip

from customtkinter import CTkFrame, CTkLabel, CTkSwitch, CTkBaseClass

class CTkTab(CTkFrame):

    def __init__(self, 
                 parent: CTkBaseClass, 
                 tab_content_list: list[TabContentViewModel], 
                 font: tuple[str, int], 
                 *args, 
                 **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.current_page = 0
        self.font = font
        self.button_list = []
        self.tab_content_list = tab_content_list
        self._initialize_components()

    def _initialize_components(self):
        self.pack_propagate(False)
        container_frame = CTkFrame(self, 
                                   height=self.font[1], 
                                   fg_color=self.cget("fg_color"))
        
        self.info_label = CTkLabel(container_frame, 
                                   font=self.font)
        
        self.toggle_switch = CTkSwitch(container_frame, 
                                       text="", 
                                       width=0)
        
        separator = CTkFrame(self, 
                             height=2)
        
        content_frame = CTkFrame(self, 
                                 fg_color=self.cget("fg_color"), 
                                 height=AUTO_FRAME_HEIGHT)

        bottom_frame = CTkFrame(self, 
                                width=BUTTON_SELECT_BAR_WIDTH, 
                                height=BUTTON_SELECT_BAR_HEIGHT, 
                                fg_color= (SELECT_BAR_LIGHT_COLOR, SELECT_BAR_DARK_COLOR), 
                                corner_radius=SELECT_BAR_CORNER_RADIUS)
        
        MyCTkToolTip(self.toggle_switch, ENABLE_SWITCH_TOOLTIP, **TOOLTIP_PARAMETERS)
        
        container_frame.pack(padx=(AUTO_FRAME_CORNER_RADIUS, AUTO_FRAME_CORNER_RADIUS/3), 
                             pady=(AUTO_FRAME_CORNER_RADIUS/4, 0), 
                             fill="x")
        
        self.info_label.pack(side="left", anchor="w")
        self.toggle_switch.pack(side="right", anchor="e")
        separator.pack(fill="x")
        content_frame.pack_propagate(False)
        content_frame.pack(fill="x")

        for i, tab in enumerate(self.tab_content_list):
            self.tab_content_list[i] = tab(content_frame, self.toggle_switch)

        self.current_tab = self.tab_content_list[self.current_page]

        bottom_frame.pack(fill= "x", 
                          side = "bottom", 
                          pady= (0, AUTO_FRAME_CORNER_RADIUS / 1.2), 
                          padx = SELECT_BAR_PADDING)
        
        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(len(self.tab_content_list) + 1, weight=1)

        for i, tab in enumerate(self.tab_content_list):
            button = CTkIconButton(bottom_frame, image=tab.icon(), width=BUTTON_WIDTH, height=BUTTON_HEIGHT, corner_radius=BUTTON_CORNER_RADIUS, 
                                   command=lambda t=tab: self._page_changed_event(self.tab_content_list.index(t)))
            tab.attach_button(button)
            button.grid(row=0, column=i + 1, padx=BUTTON_PADDING, pady=2)
            self.button_list.append(button)

    def _apply_configuration(self):
        self._page_changed_event(self.current_page)

    def _page_changed_event(self, page: int):
        new_title = self.tab_content_list[page].title()
        can_enable = self.tab_content_list[page].can_enable()

        self.current_tab.pack_forget()
        self.current_tab = self.tab_content_list[page]
        self.current_tab.pack(fill="both", expand=True)

        for button in self.button_list:
            button.deselect()
        self.button_list[page].select()

        self.info_label.configure(text=new_title)

        if can_enable:
            self.toggle_switch.pack()
            self.toggle_switch.select() if self.current_tab.is_enabled else self.toggle_switch.deselect()
            self.toggle_switch.configure(command=lambda: self.current_tab.enabled_callback(self.toggle_switch.get()))
        else:
            self.toggle_switch.pack_forget()

        if not self.current_tab.need_scrollbar():
            self.current_tab._scrollbar.grid_forget()