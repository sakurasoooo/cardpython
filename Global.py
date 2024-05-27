from typing import List
from random import shuffle  # 确保导入了 shuffle 函数
from Card import Card
from Turn import Turn

card_can_use: int = 1
card_in_hand: List[Card] = []
card_in_pool: List[Card] = []
card_used: List[Card] = []
card_discard: List[Card] = []

turns: List[Turn] = []

def draw_card():
    global card_in_pool, card_used  # 添加这行来引用全局变量
    if len(card_in_pool) > 0:
        card_in_hand.append(card_in_pool.pop(0))
    else:
        # append card from used to pool and shuffle
        card_in_pool.extend(card_used)  # 使用 extend 而不是直接赋值
        shuffle(card_in_pool)  # shuffle 操作应该是就地操作，不返回新列表
        card_used = []
        if card_in_pool:  # 确保卡池不为空再弹出卡片
            card_in_hand.append(card_in_pool.pop(0))
