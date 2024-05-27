from Player import Player
from Turn import Turn
class Buff:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def apply_at_turn_start(self, player: Player, turn: Turn):
        # 在回合开始时应用的效果
        return True
    
    def apply_during_turn(self, player: Player, turn: Turn):
        # 在回合中应用的效果
        return True

    def apply_at_turn_end(self, player: Player, turn: Turn):
        # 在回合结束时应用的效果
        return True

    def reduce_duration(self):
        self.duration -= 1

    def is_active(self):
        return self.duration > 0