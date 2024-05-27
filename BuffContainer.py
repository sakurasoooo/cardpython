from Buff import Buff

class BuffContainer:
    def __init__(self, buffs = []):
        self.buffs = buffs
    
    def add_buff(self, buff: Buff):
        self.buffs.append(buff)
    
    def start_turn_buff(self,player, turn):
        for buff in self.buffs:
            if buff.apply_at_turn_start(player, turn):
                print(f"Buff {buff.name} end at turn start.")
    
    def end_turn_buff(self,player, turn):
        for buff in self.buffs:
            if buff.apply_at_turn_end(self, turn):
                print(f"Buff {buff.name} end at turn end.")
    
    def during_turn_buff(self,player, turn):
        for buff in self.buffs:
            buff.apply_during_turn(player, turn)
