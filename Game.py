import Global
from Attribute import Attribute
from Card import Card
from Buff import Buff
from Player import Player
from BuffContainer import BuffContainer
from Turn import Turn
from BuffList import *
from CardList import *
from random import shuffle

def init_game_sense():
    Global.card_can_use = 1
    Global.card_in_hand = []
    Global.card_in_pool = [
        ポーズの基本(),
        ポーズの基本(),
        ポーズの基本(),
        ポーズの基本(),
        ポーズの基本(),
        ポーズの基本(),
        ポーズの基本(),
        ポーズの基本(),
        気分転换(),
        気分転换(),
        気分転换(),
        気分転换(),
        気分転换(),
        気分転换(),
    ]
    Global.card_used = []
    Global.card_discard = []
    Global.turns = [
        Turn(Attribute.VISUAL,1),
        Turn(Attribute.VISUAL,2),
        Turn(Attribute.VISUAL,3),
        Turn(Attribute.VISUAL,4),
        Turn(Attribute.VISUAL,5),
        Turn(Attribute.VISUAL,6),
        Turn(Attribute.VISUAL,7),
        Turn(Attribute.VISUAL,8),
        Turn(Attribute.VISUAL,9),
    ]
    
    shuffle(Global.card_in_pool)
    
def Game():
    init_game_sense()
    my_idol:Player = Player(name="姫崎 莉波",blood_max=30,visual=70,voice=80,dance=65)
    buffs = BuffContainer()
    #while Global.Turn is not Empty:
    while len(Global.turns) > 0:
        turn = Global.turns.pop(0)
        Global.card_can_use = 1
        #turn start
        print(f"=====================")
        print(f"回合 {turn.turn_number}")
        print(f"=====================")
        
        buffs.start_turn_buff(my_idol,turn)
        
        #draw 3 card into hand
        for i in range(3):
            Global.draw_card()
        
        while(Global.card_can_use > 0):
            #print card in hand
            print("手牌:")
            for i in range(len(Global.card_in_hand)):
                print(f"{i+1}. {Global.card_in_hand[i].name}","🃏")
            print("score: ",my_idol.get_score())
            print("❤️:",my_idol.get_blood())
            print("🛡️ :",my_idol.get_defense())
            print("👍 :",my_idol.get_poison())
            print("💪 :",my_idol.get_enhance())
            print("💥 :",my_idol.get_strength())
            
            # check if all card cannt use
            shuffle(Global.card_in_hand)
            chosed_card = None
            for card in Global.card_in_hand:
                if card.can_use(my_idol):
                    chosed_card = card
                    break
            if chosed_card is None:
                #skip
                print(my_idol.name,"累死了，跳过")
                Global.card_can_use -= 1
                my_idol.set_blood(my_idol.get_blood() + 2)
                continue
            Global.card_in_hand.remove(chosed_card)
            chosed_card.use(my_idol,turn)
            Global.card_can_use -= 1
            print(f"Use {chosed_card.name}")
            
            buffs.during_turn_buff(my_idol,turn)
            
            
            if chosed_card.remove_after_use:
                Global.card_discard.append(card)
            else:
                Global.card_used.append(card)
    
        buffs.end_turn_buff(my_idol,turn)
        
        
        my_idol.on_turn_end(turn)
        
        
        #append all card in  hand to used
        Global.card_used.extend(Global.card_in_hand)
        Global.card_in_hand = []
    
    print(f"Final 分数: {my_idol.get_score()}") 
    print(f"Final ❤️: {my_idol.get_blood()}")
    
    print("墓场:")
    for card in Global.card_discard:
        print(card.name)


        
        
if __name__ == "__main__":
    Game()