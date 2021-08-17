from all_image import *
from button import Button

"""
參數說明:  
cats_but:   當前關卡中能使用的貓咪按鈕
mana_value: 當前關卡所設置用來召喚貓咪的魔力值上限
virus_prob: 用於 enemy group 的 summon enemy 來限制當前關卡能出現病毒的種類機率
virus summon cd: 隨機派兵速度
next level: 紀錄過關後將解鎖的關卡名字
"""


level_setting = {
    'Lv_1': {
        'cats_but': [Button(NORMAL_CAT_BUTTON, "normal", 400, 600),
                     Button(MASK_CAT_BUTTON, "mask", 600, 600),
                     Button(SANI_CAT_BUTTON, "sanitizer", 800, 600)],
        'mana_value': 60,
        'mana_recovery': 8,
        'virus_prob': [2, 1, 0.5, 0, 0],
        'virus summon cd': [150, 160],
        'next level': 'Lv_2'
    },
    'Lv_2': {
        'cats_but': [Button(NORMAL_CAT_BUTTON, "normal", 300, 600),
                     Button(MASK_CAT_BUTTON, "mask", 500, 600),
                     Button(SANI_CAT_BUTTON, "sanitizer", 700, 600),
                     Button(ALCOHOL_CAT_BUTTON, "alcohol", 900, 600)],
        'mana_value': 110,
        'mana_recovery': 7,
        'virus_prob': [1.2, 1.2, 1.7, 0.5, 0],
        'virus summon cd': [170, 180],
        'next level': 'Lv_3',
    },
    'Lv_3': {
        'cats_but': [Button(NORMAL_CAT_BUTTON, "normal", 200, 600),
                     Button(MASK_CAT_BUTTON, "mask", 400, 600),
                     Button(SANI_CAT_BUTTON, "sanitizer", 600, 600),
                     Button(ALCOHOL_CAT_BUTTON, "alcohol", 800, 600),
                     Button(VACCINE_CAT_BUTTON, "vaccine", 1000, 600)],
        'mana_value': 160,
        'mana_recovery': 5,
        'virus_prob': [1, 1, 1.2, 1.7, 1.5],
        'virus summon cd': [100, 140, 160],
        'next level': 'main level night',
    }
}





