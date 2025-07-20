from core.controllers.ConfigurationControllerModel import ConfigurationControllerModel
from core.configurations.AutoQuestConfiguration import AutoQuestConfiguration, DungeonType, ZoneType, DungeonDifficulty
from core.FamiliarData import FamiliarData
from core.constants.GuiData import RARITY_COLORS, AUTO_QUEST_DUNGEONS, AUTO_QUEST_ZONES
from gui.views.AutoQuestTabView import AutoQuestTabView
from gui.widgets.CTkLogger import CTkLogger


class AutoQuestController(ConfigurationControllerModel):

    def __init__(self, model: AutoQuestConfiguration , view: AutoQuestTabView, data: FamiliarData, logger: CTkLogger ):
        self.data = data
        self.model = model
        self.view = view
        self.logger = logger

        super().__init__()

    # ######################
    # Interface methods
    # ######################

    def _apply_configuration(self):
        self.view.set_dungeon_default_selection(AUTO_QUEST_DUNGEONS[self.model.dungeon])
        self.view.set_zone_default_selection(AUTO_QUEST_ZONES[self.model.zone])
        self.view.set_persuade_default_value(self.model.is_persuasion_enabled)
        self.view.set_decline_default_value(self.model.auto_decline_familiar)
        self._populate_familiars_list()
        familiar_indices = self._get_familiar_indices()
        if len(familiar_indices) > 0: 
            self.view.set_familiar_default_selection(familiar_indices)
        self.view.set_difficulty_default_value(self.model.difficulty.value)

        self.view.is_enabled = self.model.is_enabled
        if not self.model.is_persuasion_enabled:
            self.view.set_familiar_enabled(False)
            self.view.set_decline_enabled(False)

    def _bind_callbacks(self):
        self.view.set_persuade_callback(self._on_persuade_checkbox_changed)
        self.view.set_decline_callback(self._on_decline_checkbox_changed)
        self.view.set_dungeon_menu_callback(self.on_dungeon_menu_changed_)
        self.view.set_zone_menu_callback(self._on_zone_menu_changed)
        self.view.set_familiar_menu_callback(self._on_familiar_menu_changed)  
        self.view.set_difficulty_callback(self._on_difficulty_changed)
        self.view.enabled_callback = self._on_enabled_changed

    def is_configuration_ready(self):
        is_zone_ready = self.model.zone != ZoneType.NOT_SET.value
        is_dungeon_ready = self.model.dungeon != DungeonType.NOT_SET.value
        is_familiar_ready = ( self.model.is_persuasion_enabled and len(self.model.familiar_names) > 0) or not self.model.is_persuasion_enabled

        self.view.set_zone_error( not is_zone_ready)
        self.view.set_dungeon_error( not is_dungeon_ready)
        self.view.set_familiar_error( not is_familiar_ready)

        if is_zone_ready and is_dungeon_ready and is_familiar_ready:
            self.view.set_tab_error(False)
            self.logger.print("Auto Quest configuration checks passed ✅")
            return True
        else:
            self.view.set_tab_error(True)
            if not is_zone_ready:
                self.logger.print("Auto Quest configuration error: Zone not selected ❌")
            if not is_dungeon_ready:
                self.logger.print("Auto Quest configuration error: Dungeon not selected ❌")
            if not is_familiar_ready:
                self.logger.print("Auto Quest configuration error: Auto persuasion is enabled but no familiar is selected ❌")
            return False

    def disable_view(self):
        self._disable_view(self.view)

    def restore_view(self):
        self._restore_view(self.view, self.model.is_enabled)
    
    def is_enabled(self) -> bool:
        return self.model.is_enabled
    
    # ######################
    # On Events methods
    # ######################

    def _on_persuade_checkbox_changed(self, value):
        self.model.is_persuasion_enabled = value
        self.view.set_familiar_enabled(value)
        self.view.set_decline_enabled(value)
    
    def _on_decline_checkbox_changed(self, value):
        self.model.auto_decline_familiar = value
    
    def on_dungeon_menu_changed_(self, value):
        if (self.model.dungeon != AUTO_QUEST_DUNGEONS.index(value)):
            self.model.dungeon = AUTO_QUEST_DUNGEONS.index(value)
            self._populate_familiars_list()
            self.model.familiar_names = []

    def _on_zone_menu_changed(self, value):
        if ( self.model.zone != AUTO_QUEST_ZONES.index(value) ):
            self.model.zone = AUTO_QUEST_ZONES.index(value)
            self._populate_familiars_list()
            self.model.familiar_names = []
    
    def _on_familiar_menu_changed(self, values: list[str]):
        if values is not None:
            familiars = self.data.get_familiars_by_name(values)
            if None not in familiars:
                self.model.familiar_names = [familiar.name for familiar in familiars]
            else:
                raise Exception("A familiar has not been found by its name")

    def _on_enabled_changed(self, is_enabled: bool):
        self.model.is_enabled = is_enabled
        self.view.is_enabled = is_enabled
    
    def _on_difficulty_changed(self, value: str):
        self.model.difficulty = DungeonDifficulty[value]
    
    # ######################
    # Private methods
    # ######################

    def _populate_familiars_list(self):
        familiar_names = []
        familiar_text_colors = []
        if self.model.zone > 0 and self.model.dungeon > 0:
            familiars = self.data.familiars_in_dungeon(self.model.zone, self.model.dungeon)
            familiar_names = [familiar.name for familiar in familiars]
            familiar_text_colors = [RARITY_COLORS[familiar.rarity.value] for familiar in familiars]
        self.view.set_familiar_values(familiar_names, familiar_text_colors)
        self.view.set_familiar_enabled(self.model.is_persuasion_enabled and self.model.is_enabled)
            
    
    def _get_familiar_indices(self):
        familiars = self.data.familiars_in_dungeon(self.model.zone, self.model.dungeon)
        familiar_indices = []
        for familiar in familiars:
            if familiar.name in self.model.familiar_names:
                familiar_indices.append(familiars.index(familiar))
        return familiar_indices