class GameNotLaunchedError(Exception):
    """Custom exception raised when a game is not launched."""
    def __init__(self, message="The game has not been launched."):
        super().__init__(message)
    
class AutoPilotStoppedByButtonError(Exception):
    """Custom exception raised when autopilot has been stopped by button."""
    def __init__(self, message="Autopilot has been stopped by button."):
        super().__init__(message)

class InputControllerClickError(Exception):
    """Custom exception raised when a click operation fails."""
    def __init__(self, button_name: str):
        super().__init__(f"Click operation failed multiple times on button: {button_name}")

class NoAutomationAvailableToRefill(Exception):
    """Custom exception raised when there all automations enabled has emptied their ressources and there 
       is no automation enabled that can refill without human interaction"""
    def __init__(self, message="All automations enabled has emptied their ressources and there is no automation enabled that can refill without human interaction."):
        super().__init__(message)

class ConnectionLostToTheGame(Exception):
    """Custom exception raised when connection to the game is lost."""
    def __init__(self, message="Connection to the game has been lost."):
        super().__init__(message)

class FamiliarNameDetectionFailed(Exception):
    """Custom exception raised when Tesseract fails to correctly read the familiar name."""
    def __init__(self, message="Tesseract was unable to correctly read the familiar name."):
        super().__init__(message)

class UnableToFocusError(Exception):
    """Custom exception raised when unable to focus the game window. Most probably, the window is minimized."""
    def __init__(self, window_name:str):
        super().__init__(f"Unable to focus the {window_name} window. The window is most probably minimized.")