from core.Observer import Publisher

class GameStats(Publisher):

    def __init__(self):
        super().__init__()
        self.dungeons_completed = 0
        self.familiars_encountered = 0
        self.fish_caught = 0

    def increment_dungeons_completed(self):
        self.dungeons_completed += 1
        self.notify()
    
    def increment_familiar_encountered(self):
        self.familiars_encountered += 1
        self.notify()
    
    def increment_fish_caught(self):
        self.fish_caught += 1
        self.notify()
    

