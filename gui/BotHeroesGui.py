from gui.views.DungeonStatView import DungeonStatView
from gui.views.FamiliarStatView import FamiliarStatView
from gui.views.FishStatView import FishStatView
from gui.views.AutoQuestTabView import AutoQuestTabView
from gui.views.AutoFishTabView import AutoFishTabView
from gui.views.SettingsTabView import SettingsTabView
from gui.views.InfoTabView import InfoTabView
from gui.widgets.CTkTab import CTkTab
from gui.widgets.CTkLogger import CTkLogger
from gui.views.OnOffButtonView import OnOffButtonView
from gui.views.AutoQuestTabView import AutoQuestTabView

from core.constants.GuiData import APPLICATION_NAME, WINDOW_SIZE, GAME_FRAME_SIZE, FRAME_CORNER_RADIUS, GAME_FRAME_PADDING, CONTAINER_FRAME_SIZE, \
    STAT_FRAME_PADDING, AUTO_FRAME_HEADER_FONT, AUTO_FRAME_SIZE, AUTO_FRAME_PADDING, AUTO_FRAME_CORNER_RADIUS, \
    LOG_FONT, LOG_SIZE, LOG_CORNER_RADIUS, LOG_PADDING, ON_BUTTON_PADDING, ROW_FRAME_WIDTH, APPLICATION_ICON, \
    CONTAINER_FRAME_RADIUS, GAME_FRAME_INTERNAL_PADDING, LOGGER_TOOLTIP, TOOLTIP_PARAMETERS

from customtkinter import CTk, CTkFrame

class BotHeroesGui(CTk):
    def __init__(self):
        super().__init__()
        self.resizable(True, False) 
        self.title(APPLICATION_NAME)
        self.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")
        self.iconbitmap(APPLICATION_ICON)
        self.minsize(width=GAME_FRAME_PADDING*2+GAME_FRAME_SIZE[0], height=1)
        self.maxsize(width=WINDOW_SIZE[0], height=WINDOW_SIZE[1])

        # Left Frame --------------------------------------------------------------------------------------------------------------
        game_frame = CTkFrame(self, 
                              width=GAME_FRAME_SIZE[0], 
                              height=GAME_FRAME_SIZE[1], 
                              corner_radius=FRAME_CORNER_RADIUS)
        
        self.game_container_frame = CTkFrame(game_frame, 
                                             corner_radius=CONTAINER_FRAME_RADIUS)
        
        game_frame.pack(padx=GAME_FRAME_PADDING, pady=GAME_FRAME_PADDING, side="left")
        game_frame.pack_propagate(False)

        self.game_container_frame.pack(fill="both", expand = True, padx = GAME_FRAME_INTERNAL_PADDING, pady= GAME_FRAME_INTERNAL_PADDING)
        # Right Frame -------------------------------------------------------------------------------------------------------------
        container_frame = CTkFrame(self, 
                                   width=CONTAINER_FRAME_SIZE[0], 
                                   height=CONTAINER_FRAME_SIZE[1], 
                                   fg_color=self.cget("fg_color"))
        
        container_first_row = CTkFrame(container_frame, fg_color=self.cget("fg_color"))
        self.dungeon_stat_frame = DungeonStatView(container_first_row)
        self.familiar_encountered_stat_frame = FamiliarStatView(container_first_row)
        self.fish_stat_frame = FishStatView(container_first_row)

        container_second_row = CTkFrame(container_frame, 
                                        corner_radius=AUTO_FRAME_CORNER_RADIUS, 
                                        fg_color=self.cget("fg_color"))
        
        self.game_automations_tab = CTkTab(container_second_row, 
                                           [AutoQuestTabView, AutoFishTabView],
                                           font=AUTO_FRAME_HEADER_FONT, 
                                           width=AUTO_FRAME_SIZE[0], 
                                           height=AUTO_FRAME_SIZE[1], 
                                           corner_radius=AUTO_FRAME_CORNER_RADIUS)
        
        self.software_configuration_tab = CTkTab(container_second_row, 
                                             [SettingsTabView, InfoTabView],
                                             font=AUTO_FRAME_HEADER_FONT, 
                                             width=AUTO_FRAME_SIZE[0], 
                                             height=AUTO_FRAME_SIZE[1], 
                                             corner_radius=AUTO_FRAME_CORNER_RADIUS)
            
        container_third_row = CTkFrame(container_frame, 
                                       corner_radius=FRAME_CORNER_RADIUS, 
                                       width=ROW_FRAME_WIDTH)

        self.logger = CTkLogger(container_third_row, 
                                tooltip=LOGGER_TOOLTIP,
                                tooltip_parameters=TOOLTIP_PARAMETERS,
                                font= LOG_FONT, 
                                width=LOG_SIZE[0], 
                                height=LOG_SIZE[1], 
                                corner_radius=LOG_CORNER_RADIUS)
        
        self.on_off_button = OnOffButtonView(container_third_row)


        container_frame.pack(side="left", padx=(0, GAME_FRAME_PADDING), pady = GAME_FRAME_PADDING, fill="x")
        container_frame.pack_propagate(False)
        container_first_row.pack(fill = "x")
        self.dungeon_stat_frame.pack(side="left" ,padx=(0, STAT_FRAME_PADDING))
        self.familiar_encountered_stat_frame.pack(side="left", padx=(0, STAT_FRAME_PADDING))
        self.fish_stat_frame.pack(side="left")
        container_second_row.pack(fill = "x", pady=(AUTO_FRAME_PADDING, 0))

        self.game_automations_tab.pack(side = "left", padx = (0, 5))
        self.software_configuration_tab.pack(side = "left")

        # Row 2: Log & On/Off
        container_third_row.pack(pady=(AUTO_FRAME_PADDING, 0), anchor = "w")
        container_third_row.pack_propagate(False)

        self.logger.pack(side="left", padx= LOG_PADDING, pady= LOG_PADDING)
        self.on_off_button.pack(side="left", padx= (ON_BUTTON_PADDING, 0))

    def get_ctk_logger(self) -> CTkLogger:
        return self.logger
    
    def get_auto_quest_tab(self) -> AutoQuestTabView:
        return self.game_automations_tab.tab_content_list[0]
    
    def get_auto_fish_tab(self) -> AutoFishTabView:
        return self.game_automations_tab.tab_content_list[1]
    
    def get_settings_tab(self) -> SettingsTabView:
        return self.software_configuration_tab.tab_content_list[0]

    def get_info_tab(self) -> InfoTabView:
        return self.software_configuration_tab.tab_content_list[1]
    
    def get_button_on_off(self) -> OnOffButtonView:
        return self.on_off_button

    def get_dungeon_stat(self) -> DungeonStatView:
        return self.dungeon_stat_frame
    
    def get_familiar_stat(self) -> FamiliarStatView:
        return self.familiar_encountered_stat_frame

    def get_fish_stat(self) -> FishStatView:
        return self.fish_stat_frame
    
    def get_game_container_frame_id(self) -> CTkFrame:
        return self.game_container_frame.winfo_id()

    def apply_tab_configurations(self):
        self.game_automations_tab._apply_configuration()
        self.software_configuration_tab._apply_configuration()
    
    def set_always_on_top(self, is_awlays_on_top: bool):
        self.attributes('-topmost', is_awlays_on_top)