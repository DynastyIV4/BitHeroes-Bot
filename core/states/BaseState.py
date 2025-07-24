from abc import ABC, abstractmethod

class BaseState(ABC):
    
    def __init__(self, state_machine):
        from core.StateMachine import StateMachine
        from core.AutomationMachine import AutomationMachine
        from core.GameInterface import GameInterface
        from core.configurations.AutoFishConfiguration import AutoFishConfiguration
        from core.configurations.AutoQuestConfiguration import AutoQuestConfiguration
        from core.configurations.GeneralSettings import GeneralSettingsConfiguration
        from core.GameStats import GameStats
        from core.ZoneData import ZoneData
        from core.WindowHandler import WindowHandler
        from gui.widgets.CTkLogger import CTkLogger

        self.state_machine: StateMachine = state_machine
        self.automation_machine: AutomationMachine = self.state_machine.automation_machine
        self.game_interface: GameInterface = self.state_machine.game_interface
        self.logger: CTkLogger = self.state_machine.logger
        self.auto_quest_config: AutoQuestConfiguration = self.state_machine.auto_quest_config
        self.auto_fish_config: AutoFishConfiguration = self.state_machine.auto_fish_config
        self.general_settings_config: GeneralSettingsConfiguration = self.state_machine.general_settings_config
        self.window_handler: WindowHandler = self.state_machine.window_handler
        self.game_stats: GameStats = self.state_machine.game_stats
        self.zone_data: ZoneData = self.state_machine.zone_data

    @abstractmethod
    def enter(self):
        pass
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def exit(self):
        pass
