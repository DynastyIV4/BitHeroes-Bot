from abc import ABC, abstractmethod
from gui.view_models.TabContentViewModel import TabContentViewModel

class ConfigurationControllerModel(ABC):

    def __init__(self):
        self._apply_configuration()
        self._bind_callbacks()

    def _disable_view(self, view: TabContentViewModel):
        view.set_switch_enabled(False)
        view.is_enabled = False
    
    def _restore_view(self, view: TabContentViewModel, is_enabled: bool):
        view.set_switch_enabled(True)
        view.is_enabled = is_enabled

    @abstractmethod
    def disable_view(self):
        pass

    @abstractmethod
    def restore_view(self):
        pass

    @abstractmethod
    def _apply_configuration(self):
        pass

    @abstractmethod
    def _bind_callbacks(self):
        pass

    @abstractmethod
    def is_configuration_ready(self):
        pass

    @abstractmethod
    def is_enabled(self):
        pass
