from core.models.Coordinates import Coordinates

class ColorCoordinates(Coordinates):
    def __init__(self, x: int, y: int, red: int, green: int, blue: int):
        super().__init__(x, y)
        self.color = Color(red, green, blue)
    
    def __repr__(self):
        return f"ColorCoordinates({self.x}, {self.y}, {self.color.red}, {self.color.green}, {self.color.blue})"

class Color:
    def __init__(self, red: int, green: int, blue: int):
        self.red: int = red
        self.green: int = green
        self.blue: int = blue