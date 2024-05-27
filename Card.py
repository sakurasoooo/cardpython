from Player import Player
from Turn import Turn
class Card:
    def __init__(self, name = "错误卡", attack = 0, defense = 0, poison = 0, strength = 0, agility = 0, enhance = 0, super_enhance = 0, cost = 0, blood_cost = 0, remove_after_use = False, blood_recover = 0):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.poison = poison
        self.strength = strength
        self.agility = agility
        self.enhance = enhance
        self.super_enhance = super_enhance
        self.cost = cost
        self.blood_cost = blood_cost
        self.blood_recover = 0
        self.remove_after_use = remove_after_use

    def use(self, player: Player, turn: Turn):
        self.apply_cost(player, turn)
        self.apply_score(self.attack,player, turn)
        self.extra_effect(player, turn)
        self.apply_buff(player, turn)
    
    def apply_score(self, attack, player: Player, turn: Turn):
        # 在这里定义卡牌对玩家分数的影响
        enhance_rate = 1 if player.get_enhance() == 0 else 1.5
        p_attack = (attack + player.get_strength()) * enhance_rate
        score = p_attack * player.calculate_score_rate(turn.attribute)
        player.set_score(player.get_score() + score)
    
    def apply_buff(self, player: Player, turn: Turn):
        # 在这里定义卡牌对玩家属性的影响
        player.set_defense(player.get_defense() + self.defense + player.get_agility())
        player.set_poison(player.get_poison() + self.poison)
        player.set_strength(player.get_strength() + self.strength)
        player.set_agility(player.get_agility() + self.agility)
        player.set_enhance(player.get_enhance() + self.enhance)
        player.set_super_enhance(player.get_super_enhance() + self.super_enhance)
        
    def extra_effect(self, player: Player, turn: Turn):
        # 在这里定义卡牌的额外效果
        pass
    
    def apply_cost(self, player: Player, turn: Turn):
        # cost player defence first then blood
        half = 1 if player.get_cost_half() == 0 else 0.5
        cost = self.cost * half - player.get_cost_reduction()
        blood_cost = self.blood_cost * half - player.get_cost_reduction()
        cost = max(0, cost)
        blood_cost = max(0, blood_cost)
        if player.get_defense() >= cost:
            player.set_defense(player.get_defense() - cost)
        else:
            player.set_blood(player.get_blood() - cost)
            player.set_defense(0)
        
        player.set_blood(player.get_blood() - blood_cost)
    
    def can_use(self, player: Player) -> bool:
        half = 1 if player.get_cost_half() == 0 else 0.5
        return player.get_blood() + player.get_defense() >= (self.blood_cost + self.cost) * half - player.get_cost_reduction()
