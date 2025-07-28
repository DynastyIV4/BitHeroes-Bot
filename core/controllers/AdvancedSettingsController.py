from core.controllers.ConfigurationControllerModel import ConfigurationControllerModel
from core.configurations.AdvancedSettingsConfiguration import AdvancedSettingsConfiguration
from gui.views.AdvancedSettingsView import AdvancedSettingsView

class AdvancedSettingsController(ConfigurationControllerModel):

    def __init__(self, 
                 configuration: AdvancedSettingsConfiguration, 
                 view: AdvancedSettingsView):
        self._configuration = configuration
        self._view = view

        super().__init__()

    # ######################
    # Interface methods
    # ######################

    def _apply_configuration(self):
        self._view.set_debug_logging_default_selection(self._configuration.enable_debug_logging)
        self._view.set_export_logging_default_selection(self._configuration.enable_export_logging)

    
    def _bind_callbacks(self):
        self._view.set_debug_logging_callback(self._on_debug_logging_changed)
        self._view.set_export_logging_callback(self._on_export_logging_changed)

    def is_configuration_ready(self):
        return True

    def disable_view(self):
        self._disable_view(self._view)

    def restore_view(self):
        self._restore_view(self._view, True)
    
    def is_enabled(self):
        return self._view.is_enabled
    
    # ######################
    # On Events methods
    # ######################

    def _on_debug_logging_changed(self, is_selected: bool):
        self._configuration.enable_debug_logging = is_selected

    def _on_export_logging_changed(self, is_selected: bool):
        self._configuration.enable_export_logging = is_selected
    