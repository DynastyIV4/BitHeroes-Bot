from core.controllers.ConfigurationControllerModel import ConfigurationControllerModel
from core.configurations.GeneralSettings import GeneralSettingsConfiguration, AppearanceMode
from core.constants.GuiData import APPEARANCE_MODE
from gui.views.SettingsTabView import SettingsTabView
from gui.widgets.CTkLogger import CTkLogger
from gui.BotHeroesGui import BotHeroesGui

from customtkinter import set_appearance_mode, filedialog
import os

class GeneralSettingsController(ConfigurationControllerModel):

    def __init__(self, model: GeneralSettingsConfiguration , view: SettingsTabView, bot_heroes_gui: BotHeroesGui, logger: CTkLogger ):
        self.model = model
        self.view = view
        self.bot_heroes_gui = bot_heroes_gui
        self.logger = logger

        super().__init__()

    # ######################
    # Interface methods
    # ######################

    def _apply_configuration(self):
        self.view.set_appearance_default_selection(APPEARANCE_MODE[1]) # Forced to dark until Light is working
        self.view.set_game_path_value(self.model.game_path)
        self._apply_appearance_mode(APPEARANCE_MODE[self.model.appearance_mode])
        self.bot_heroes_gui.set_always_on_top(self.model.is_always_on_top)

    
    def _bind_callbacks(self):
        self.view.set_appearance_mode_callback(self._on_appearance_mode_changed)
        self.view.set_game_path_callback(self._on_game_path_clicked)
        self.view.set_always_on_top_callback(self._on_always_on_top_changed)

    def is_configuration_ready(self):
        is_game_path_ready: bool = self._valid_game_path(self.model.game_path)

        self.view.set_game_path_error(not is_game_path_ready)
 
        if is_game_path_ready:
            self.view.set_tab_error(False)
            self.logger.print("General Settings configuration checks passed ✅")
            return True
        else:
            self.view.set_tab_error(True)
            self.logger.print("General Settings configuration checks failed. Select a valid game path. ❌")
            return False

    def disable_view(self):
        self._disable_view(self.view)

    def restore_view(self):
        self._restore_view(self.view, True)
    
    def is_enabled(self):
        return self.view.is_enabled
    
    # ######################
    # On Events methods
    # ######################

    def _on_appearance_mode_changed(self, value: str):
        self.model.appearance_mode = APPEARANCE_MODE.index(value)
        self._apply_appearance_mode(value)

    def _on_game_path_clicked(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.model.game_path = filename
            self.view.set_game_path_value(filename)
    
    def _on_always_on_top_changed(self, value: bool):
        self.model.is_always_on_top = value
        self.bot_heroes_gui.set_always_on_top(value)
    
    # ######################
    # Logic methods
    # ######################

    def _apply_appearance_mode(self, appearance_mode: str):
        if appearance_mode == AppearanceMode.SYSTEM.value:
            set_appearance_mode("system")
        elif appearance_mode == AppearanceMode.DARK.value:
            set_appearance_mode("dark")
        elif appearance_mode == AppearanceMode.LIGHT.value:
            set_appearance_mode("light")

    def _valid_game_path(self, path: str) -> bool:
        return path.endswith("Bit Heroes.exe") and os.path.isfile(path)
