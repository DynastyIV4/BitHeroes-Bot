from core.Observer import Subscriber
from core.GameStats import GameStats
from gui.view_models.StatViewModel import StatViewModel

class StatsController(Subscriber):
    def __init__(self, dungeon_stat_view: StatViewModel, familiar_stat_view: StatViewModel, fish_stat_view: StatViewModel, stats_model: GameStats):
        super().__init__()
        self.dungeon_stat_view = dungeon_stat_view
        self.familiar_stat_view = familiar_stat_view
        self.fish_stat_view = fish_stat_view
        self.stats_model = stats_model
        self.stats_model.subscribe(self)

    def update(self):
        self.dungeon_stat_view.set_value(self.stats_model.dungeons_completed)
        self.familiar_stat_view.set_value(self.stats_model.familiars_encountered)
        self.fish_stat_view.set_value(self.stats_model.fish_caught)
    


    

