from abc import ABC, abstractmethod

class BaseIdentifier(ABC):
    @staticmethod
    @abstractmethod
    def identify(text):
        """
        Abstract static method to identify text.
        Must be implemented by subclasses.
        """
        pass