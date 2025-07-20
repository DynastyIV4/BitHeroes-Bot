from core.controllers.ConfigurationControllerModel import ConfigurationControllerModel
from gui.views.AutoFishTabView import AutoFishTabView
from core.configurations.AutoFishConfiguration import AutoFishConfiguration
from gui.widgets.CTkLogger import CTkLogger

class AutoFishController(ConfigurationControllerModel):

    def __init__(self, model: AutoFishConfiguration , view: AutoFishTabView, logger: CTkLogger ):
        self.model = model
        self.view = view
        self.logger = logger

        super().__init__()

    # ######################
    # Interface methods
    # ######################

    def _apply_configuration(self):
        self.view.set_default_worm_selection(
            is_common=self.model.is_common,
            is_rare=self.model.is_rare,
            is_epic=self.model.is_epic,
            is_legendary=self.model.is_legendary
        )

        self.view.is_enabled = self.model.is_enabled
    
    def _bind_callbacks(self):
        self.view.set_common_worm_callback(self._on_common_worm_changed)
        self.view.set_rare_worm_callback(self._on_rare_worm_changed)
        self.view.set_epic_worm_callback(self._on_epic_worm_changed)
        self.view.set_legendary_worm_callback(self._on_legendary_worm_changed)
        self.view.enabled_callback = self._on_enabled_changed

    def is_configuration_ready(self):
        are_worms_ready = self.model.is_common or self.model.is_rare or self.model.is_epic or self.model.is_legendary

        self.view.set_worms_error(not are_worms_ready)
 
        if are_worms_ready:
            self.view.set_tab_error(False)
            self.logger.print("Auto Fish configuration checks passed ✅")
            return True
        else:
            self.view.set_tab_error(True)
            self.logger.print("Auto Fish configuration checks failed. Select at least one worm. ❌")
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

    def _on_common_worm_changed(self, is_common: bool):
        self.model.is_common = is_common
    
    def _on_rare_worm_changed(self, is_rare: bool):
        self.model.is_rare = is_rare
    
    def _on_epic_worm_changed(self, is_epic: bool):
        self.model.is_epic = is_epic
    
    def _on_legendary_worm_changed(self, is_legendary: bool):
        self.model.is_legendary = is_legendary
    
    def _on_enabled_changed(self, is_enabled: bool):
        self.model.is_enabled = is_enabled
        self.view.is_enabled = is_enabled