from abc import ABC, abstractmethod

class CustomException(Exception, ABC):
    """All custom exceptions are caught by the state machine and cause the auto-pilot to turn off."""
    @abstractmethod
    def __init__(self, message):
        super().__init__(message)

class GameNotLaunchedError(CustomException):
    """Custom exception raised when a game is not launched."""
    def __init__(self):
        super().__init__("The game has not been launched.")
    
class GameLaunchedFailError(CustomException):
    """Custom exception raised when the game didnt succeed to launch after 3 attemps"""
    def __init__(self):
        super().__init__("The game failed to launch after 3 attempts.")
    
class AutoPilotStoppedByButtonError(CustomException):
    """Custom exception raised when autopilot has been stopped by button."""
    def __init__(self):
        super().__init__("Autopilot has been stopped by button.")

class InputControllerClickError(CustomException):
    """Custom exception raised when a click operation fails."""
    def __init__(self, button_name: str):
        super().__init__(f"Click operation failed multiple times on button: {button_name}")

class NoAutomationAvailableToRefill(CustomException):
    """Custom exception raised when there all automations enabled has emptied their ressources and there 
       is no automation enabled that can refill without human interaction"""
    def __init__(self):
        super().__init__("All automations enabled has emptied their ressources and there is no automation enabled that can refill without human interaction.")

class ConnectionLostToTheGame(CustomException):
    """Custom exception raised when connection to the game is lost."""
    def __init__(self):
        super().__init__("Connection to the game has been lost.")

class FamiliarNameDetectionFailed(CustomException):
    """Custom exception raised when Tesseract fails to correctly read the familiar name."""
    def __init__(self):
        super().__init__("Tesseract was unable to correctly read the familiar name.")

class UnableToFocusError(CustomException):
    """Custom exception raised when unable to focus the game window. Most probably, the window is minimized."""
    def __init__(self, window_name:str):
        super().__init__(f"Unable to focus the {window_name} window. The window is most probably minimized.")

class UnableToFindWindow(CustomException):
    """Custom exception raised when the required window cannot be found, probably because it is closed."""
    def __init__(self, window_name: str):
        super().__init__(f"Unable to find the window: {window_name}. It is probably closed.")

class EnergyRefillNotHandled(CustomException):
    """Custom exception raised when waiting for energy to refill is not supported."""
    def __init__(self):
        super().__init__("Waiting for energy to refill is currently not supported. Coming soon 🚀")

class PixelColorMismatchError(CustomException):
    """Custom exception raised when the pixel color does not match the expected value."""
    def __init__(self):
        super().__init__("Pixel color mismatch. This may happen if the mouse is hovered over the game.")

class TimeoutStateError(CustomException):
    """Custom exception raised when waiting for a state to end takes too much time."""
    def __init__(self, state: str, waited_seconds: float):
        super().__init__(f"Timeout while waiting for state '{state}' to end. Waited {waited_seconds} seconds.")