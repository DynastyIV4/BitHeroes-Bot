from core.states.BaseState import BaseState
from core.states.GameLaunchingState import GameLaunchingState
from core.states.HomeState import HomeState
from core.AutomationMachine import AutomationMachine
from core.MemoryReader import MemoryReader
from core.configurations.AutoQuestConfiguration import AutoQuestConfiguration
from core.configurations.AutoFishConfiguration import AutoFishConfiguration
from core.configurations.GeneralSettings import GeneralSettingsConfiguration
from core.WindowHandler import WindowHandler
from core.InputHandler import InputHandler
from core.ScreenshotTool import ScreenshotTool
from core.Errors import AutoPilotStoppedByButtonError, InputControllerClickError, NoAutomationAvailableToRefill, FamiliarNameDetectionFailed, \
                        GameNotLaunchedError, UnableToFocusError
from core.Observer import Subscriber
from core.ZoneData import ZoneData
from core.GameStats import GameStats
from gui.widgets.CTkLogger import CTkLogger

class StateMachine(Subscriber):
    
    def __init__(self, 
                 memory_reader: MemoryReader,  
                 input_handler: InputHandler,
                 auto_quest_config: AutoQuestConfiguration,
                 auto_fish_config: AutoFishConfiguration,
                 general_settings_config: GeneralSettingsConfiguration,
                 game_stats: GameStats,
                 window_handler: WindowHandler,
                 screenshot_tool: ScreenshotTool,
                 zone_data: ZoneData,
                 logger: CTkLogger):
        super().__init__()
        self.input_handler = input_handler
        self.auto_quest_config = auto_quest_config
        self.auto_fish_config = auto_fish_config
        self.general_settings_config = general_settings_config
        self.memory_reader = memory_reader
        self.game_stats = game_stats
        self.window_handler = window_handler
        self.screenshot_tool = screenshot_tool
        self.zone_data = zone_data
        self.logger = logger
        self.automation_machine = AutomationMachine(auto_quest_config, auto_fish_config, logger)
        self._current_state = None
        self.is_stopped = False
        self.input_handler.subscribe(self)
    
    def start(self, initial_state: BaseState):
        self._current_state = initial_state
        self._current_state.enter()

    def change_state(self, new_state: BaseState):
        self.check_if_stopped()
        self._current_state = new_state
        self._current_state.enter()

    def run(self):
        try:
            self.automation_machine.reset_game_ressources()
            while True:
                if not self.memory_reader.is_game_running() or self.screenshot_tool.is_disconnected():
                    self.change_state(GameLaunchingState(self))
                else:
                    self.change_state(HomeState(self))
        except (AutoPilotStoppedByButtonError, InputControllerClickError, NoAutomationAvailableToRefill, FamiliarNameDetectionFailed, 
                GameNotLaunchedError, UnableToFocusError) as e:
            self.logger.print(str(e))
        
        self.is_stopped = True

    def stop(self):
        self.is_stopped = True
    
    def check_if_stopped(self):
        if self.is_stopped:
            raise AutoPilotStoppedByButtonError()
    
    def update(self):
        self.check_if_stopped()