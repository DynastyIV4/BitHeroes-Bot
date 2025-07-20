from core.controllers.ConfigurationControllerModel import ConfigurationControllerModel
from core.constants.ConfigData import GITHUB_URL, DISCORD_URL, WIKI_URL
from gui.views.InfoTabView import InfoTabView
from gui.widgets.CTkLogger import CTkLogger

import webbrowser

class InfoController(ConfigurationControllerModel):

    def __init__(self, view: InfoTabView, logger: CTkLogger ):
        self.view = view
        self.logger = logger

        super().__init__()

    # ######################
    # Interface methods
    # ######################

    def _apply_configuration(self):
        pass
    
    def _bind_callbacks(self):
        self.view.set_github_callback(self._on_github_button_clicked)
        self.view.set_discord_callback(self._on_discord_button_clicked)
        self.view.set_wiki_callback(self._on_wiki_button_clicked)

    def is_configuration_ready(self):
        return True
    
    def disable_view(self):
        pass

    def restore_view(self):
        pass

    def is_enabled(self):
        return True

    # ######################
    # On Events methods
    # ######################

    def _on_github_button_clicked(self):
        webbrowser.open(GITHUB_URL)
    
    def _on_discord_button_clicked(self):
        webbrowser.open(DISCORD_URL)
    
    def _on_wiki_button_clicked(self):
        webbrowser.open(WIKI_URL)
    