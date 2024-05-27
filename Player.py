from Attribute import Attribute
from Turn import Turn
from math import floor, ceil
class Player:
    def __init__(self, name, defense = 0, poison = 0, strength = 0, agility = 0, enhance = 0, super_enhance = 0, visual = 0, voice = 0, dance = 0, score = 0, cost_reduction = 0, cost_half = 0, blood_max = 0):
        self.name = name
        self.blood_max = blood_max
        self.blood = self.blood_max
        self.defense = defense
        self.poison = poison
        self.strength = strength
        self.agility = agility
        self.enhance = enhance
        self.super_enhance = super_enhance
        self.visual = visual
        self.voice = voice
        self.dance = dance
        self.current_health = 100
        self.current_shield = 0
        self.score = 0
        self.cost_reduction = 0
        self.cost_half = 0

    def visual_rate(self):
        #TODO: Implement this 缺少数据
        return 1

    def voice_rate(self):
        #TODO: Implement this 缺少数据
        return 1

    def dance_rate(self):
        #TODO: Implement this 缺少数据
        return 1

    def calculate_score_rate(self, attribute: Attribute):
        if attribute == Attribute.VISUAL:
            return self.visual_rate()
        elif attribute == Attribute.VOICE:
            return self.voice_rate()
        elif attribute == Attribute.DANCE:
            return self.dance_rate()

    def on_turn_start(self, turn: Turn):
        pass
    
    def on_turn_end(self, turn: Turn):
        
        self.apply_poison_score(turn)
        
        self.set_poison(self.get_poison() - 1)
        self.set_super_enhance(self.get_super_enhance() - 1)
        self.set_enhance(self.get_enhance() - 1)
        
    def apply_poison_score(self, turn: Turn):
        score = self.get_poison() * self.calculate_score_rate(turn.attribute)
        self.set_score(self.get_score() + score)
        
    
    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = ceil(score)
    
    
    def set_blood(self, blood):
        self.blood = ceil(max(0, min(blood, self.blood_max)))
        
    def get_blood(self):
        return self.blood

    def set_defense(self, defense):
        self.defense = ceil(max(0, defense))
    
    def get_defense(self):
        return self.defense
    
    def set_poison(self, poison):
        self.poison = poison
        
    def get_poison(self):
        return max(0, self.poison)
    
    def set_strength(self, strength):
        self.strength = strength
        
    def get_strength(self):
        return self.strength
    
    def set_agility(self, agility):
        self.agility = agility
    
    def get_agility(self):
        return self.agility
    
    def set_enhance(self, enhance):
        self.enhance = max(0, enhance)
    
    def get_enhance(self):
        return self.enhance
    
    def set_super_enhance(self, super_enhance):
        self.super_enhance = max(0, super_enhance)
    
    def get_super_enhance(self):
        return self.super_enhance
    
    def get_cost_reduction(self):
        return self.cost_reduction
    
    def set_cost_reduction(self, cost_reduction):
        self.cost_reduction = cost_reduction
        
    def get_cost_half(self):
        return self.cost_half
    
    def set_cost_half(self, cost_half):
        self.cost_half = cost_half
    
