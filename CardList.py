from Card import Card
from Player import Player
from Turn import Turn
class アピールの基本(Card):
    def __init__(self):
        super().__init__(
            name="アピールの基本",
            attack=9,
            cost=4,
        )
    
class ポーズの基本(Card):
    def __init__(self):
        super().__init__(
            name="ポーズの基本",
            defense=2,
            cost=3,
        )
        
class 挑戦(Card):
    def __init__(self):
        super().__init__(
            name="挑戦",
            attack=32,
            cost=7,
            remove_after_use=True,
        )
        
class 試行錯誤(Card):
    def __init__(self):
        super().__init__(
            name="試行錯誤",
            attack=8,
            cost=7,
            remove_after_use=True,
        )
    
    def extra_effect(self, player: Player, turn: Turn):
        self.apply_score(self.attack, player, turn)
        
class 可愛い仕草(Card):
    def __init__(self):
        super().__init__(
            name="可愛い仕草",
            poison=3,
            cost=5,
        )
        
    def extra_effect(self, player: Player, turn: Turn):
        p_attack = player.get_poison() * 1
        self.apply_score(p_attack, player, turn)

class 気分転换(Card):
    def __init__(self):
        super().__init__(
            name="気分転换",
            blood_cost=5,
            remove_after_use=True,
        )
        
    def extra_effect(self, player: Player, turn: Turn):
        p_attack = player.get_defense() * 1
        self.apply_score(p_attack, player, turn)
        
class 表現の基本(Card):
    def __init__(self):
        super().__init__(
            name="表現の基本",
            defense=4,
            cost=0,
            remove_after_use=True,
        )
        
class 振る舞いの基本(Card):
    def __init__(self):
        super().__init__(
            name="振る舞いの基本",
            defense=1,
            cost=1,
            enhance=2,
        )
        
class 表情の基本(Card):
    def __init__(self):
        super().__init__(
            name="表情の基本",
            defense=1,
            cost=1,
            strength=2,
        )
        
class 目線の基本(Card):
    def __init__(self):
        super().__init__(
            name="目線の基本",
            defense=1,
            cost=2,
            poison=2,
        )
        
class 意識の基本(Card):
    def __init__(self):
        super().__init__(
            name="意識の基本",
            defense=1,
            cost=2,
            agility=2,
        )
        
class 眠気(Card):
    def __init__(self):
        super().__init__(
            name="眠気",
            remove_after_use=True,
        )