import os
from settings import *

"""
白天遊戲裡的圖片在最下面
"""

# background image
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "background.jpg")), (WIN_WIDTH, WIN_HEIGHT))
BACKGROUND_NIGHT = pygame.transform.scale(pygame.image.load(os.path.join("images", "night background.jpeg")), (WIN_WIDTH, WIN_HEIGHT))
MENU_BG_DAY = pygame.transform.scale(pygame.image.load(os.path.join("images", "menu background.jpeg")), (WIN_WIDTH, WIN_HEIGHT))
MENU_BG_NIGHT = pygame.transform.scale(pygame.image.load(os.path.join("images", "bg_night.jpg")), (WIN_WIDTH, WIN_HEIGHT))
MENU_SCENE_DAY = pygame.transform.scale(pygame.image.load(os.path.join("images", "menu_scene_day.jpg")), (WIN_WIDTH, WIN_HEIGHT))
MENU_SCENE_NIGHT = pygame.transform.scale(pygame.image.load(os.path.join("images", "menu_scene_night.jpg")), (WIN_WIDTH, WIN_HEIGHT))
MENU_SCENE_DAY_STORY = pygame.transform.scale(pygame.image.load(os.path.join("images", "menu_scene_day_story.png")), (WIN_WIDTH, WIN_HEIGHT))
MENU_SCENE_NIGHT_STORY = pygame.transform.scale(pygame.image.load(os.path.join("images", "menu_scene_night_story.png")), (WIN_WIDTH, WIN_HEIGHT))

# LOGO image
LOGO_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "LOGO1.png")), (726, 280))
LOGO_IMAGE_small = pygame.transform.scale(pygame.image.load(os.path.join("images", "LOGO_small.png")), (183, 69))

# button for volume choose
VOLUME_BG = pygame.transform.scale(pygame.image.load(os.path.join("images", "menu_scene_opening.png")), (WIN_WIDTH, WIN_HEIGHT))
VOLUME_COMPUTER = pygame.transform.scale(pygame.image.load(os.path.join("images", "volume_computer.png")), (250, 250))
VOLUME_EARPHONE = pygame.transform.scale(pygame.image.load(os.path.join("images", "volume_earphone.png")), (250, 250))

# button for main menu
LEVEL_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "LV_but_day.png")), (300, 135))
INTRO_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "introduction_button.png")), (300, 135))
LEVEL_BTN_NIGHT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "LV_but_night.png")), (300, 135))
INTRO_BTN_NIGHT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "introduction_button_night.png")), (300, 135))
TIME_CHANGE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "day-and-night.png")), (80, 80))

# button for introduction menu
RETURN_BLACK_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "arrow.png")), (120, 70))
RETURN_WHITE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "arrow_night.png")), (120, 70))

# introduce page
INTRODUCE01 = pygame.transform.scale(pygame.image.load(os.path.join("images", "introduce01.jpg")), (WIN_WIDTH, WIN_HEIGHT))
INTRODUCE02 = pygame.transform.scale(pygame.image.load(os.path.join("images", "introduce02.jpg")), (WIN_WIDTH, WIN_HEIGHT))
INTRODUCE03 = pygame.transform.scale(pygame.image.load(os.path.join("images", "introduce03.jpg")), (WIN_WIDTH, WIN_HEIGHT))
INTRODUCE04 = pygame.transform.scale(pygame.image.load(os.path.join("images", "introduce04.jpg")), (WIN_WIDTH, WIN_HEIGHT))
INTRODUCE05 = pygame.transform.scale(pygame.image.load(os.path.join("images", "introduce05.jpg")), (WIN_WIDTH, WIN_HEIGHT))
INTRODUCE06 = pygame.transform.scale(pygame.image.load(os.path.join("images", "introduce06.jpg")), (WIN_WIDTH, WIN_HEIGHT))
INTRODUCE07 = pygame.transform.scale(pygame.image.load(os.path.join("images", "introduce07.jpg")), (WIN_WIDTH, WIN_HEIGHT))
INTRODUCE08 = pygame.transform.scale(pygame.image.load(os.path.join("images", "introduce08.jpg")), (WIN_WIDTH, WIN_HEIGHT))
INTRODUCE09 = pygame.transform.scale(pygame.image.load(os.path.join("images", "introduce09.jpg")), (WIN_WIDTH, WIN_HEIGHT))
# -------------------------------------------------------------------------------------------------------------

# user guide and button (day / night)
NAVIGATION_NEXT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "navigation_next.png")), (125, 62))
NAVIGATION_PREV_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "navigation_prev.png")), (125, 62))

USER_GUIDE_DAY_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "user_guide_day_1.png")), (WIN_WIDTH, WIN_HEIGHT))
USER_GUIDE_DAY_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "user_guide_day_2.png")), (WIN_WIDTH, WIN_HEIGHT))
USER_GUIDE_DAY_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "user_guide_day_3.png")), (WIN_WIDTH, WIN_HEIGHT))
USER_GUIDE_DAY_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "user_guide_day_4.png")), (WIN_WIDTH, WIN_HEIGHT))
USER_GUIDE_DAY_5 = pygame.transform.scale(pygame.image.load(os.path.join("images", "user_guide_day_5.png")), (WIN_WIDTH, WIN_HEIGHT))

USER_GUIDE_NIGHT_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "user_guide_night_1.png")), (WIN_WIDTH, WIN_HEIGHT))
USER_GUIDE_NIGHT_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "user_guide_night_2.png")), (WIN_WIDTH, WIN_HEIGHT))
USER_GUIDE_NIGHT_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "user_guide_night_3.png")), (WIN_WIDTH, WIN_HEIGHT))
USER_GUIDE_NIGHT_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "user_guide_night_4.png")), (WIN_WIDTH, WIN_HEIGHT))
# -------------------------------------------------------------------------------------------------------------

# button for sound / music
MUTE_BTN = pygame.transform.scale(pygame.image.load(os.path.join("images", "no-sound.png")), (50, 50))
PLAY_BTN = pygame.transform.scale(pygame.image.load(os.path.join("images", "sound.png")), (50, 50))

# button for level menu (open / close)
LV1_OP_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv1.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))
LV2_OP_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv2.png")), (LV_BTN_WIDTH+5, LV_BTN_HEIGHT))
LV3_OP_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv3.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))
LV1_OP_NIGHT_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv1_NIGHT.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))
LV2_OP_NIGHT_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv2_NIGHT.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))
LV3_OP_NIGHT_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv3_NIGHT.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))

LV2_CL_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv2_CL.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))
LV3_CL_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv3_CL.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))
LV2_CL_NIGHT_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv2_CL_NIGHT.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))
LV3_CL_NIGHT_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv3_CL_NIGHT.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))

# game over image
WIN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "win.png")), (768, 317))
LOSE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "lose.png")), (812, 312))
BTN_W, BTN_H = 364, 135
NEXT_BTN = pygame.transform.scale(pygame.image.load(os.path.join("images", "next_level.png")), (BTN_W, BTN_H))
BACK_BTN = pygame.transform.scale(pygame.image.load(os.path.join("images", "back_to_menu.png")), (BTN_W, BTN_H))
NIGHT_WIN_ENDING_BTN = pygame.transform.scale(pygame.image.load(os.path.join("images", "ending_button_night.png")), (790, 135))
# -------------------------------------------------------------------------------------------------------------

# cat image for night game
NORMAL_CAT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "cat.png")), (60, 65))
MASK_CAT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "mask_cat.png")), (60, 65))
SANI_CAT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "sanitizer_cat.png")), (75, 75))
VACCINE_CAT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "vaccine_cat.png")), (75, 80))
ALCOHOL_CAT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "alcohol_cat.png")), (80, 75))

NORMAL_CAT_ATTACK_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "cat_attack.png")), (63, 66))
MASK_CAT_ATTACK_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "mask_cat_attack.png")), (60, 65))
SANI_CAT_ATTACK_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "sanitizer_cat_attack.png")), (75, 75))
VACCINE_CAT_ATTACK_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "vaccine_cat_attack.png")), (75, 80))
ALCOHOL_CAT_ATTACK_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "alcohol_cat_attack.png")), (80, 75))


# cat button image
NORMAL_CAT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "cat_button.png")), (150, 150))
MASK_CAT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "mask_cat_button.png")), (150, 150))
SANI_CAT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "sanitizer_cat_button.png")), (150, 150))
VACCINE_CAT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "vaccine_cat_button.png")), (150, 150))
ALCOHOL_CAT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "alcohol_cat_button.png")), (150, 150))


# virus image
BLUE_VIRUS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus.png")), (50, 50))
RED_VIRUS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_red.png")), (70, 70))
YELLOW_VIRUS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_yellow.png")), (80, 80))
BLACK_VIRUS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_black.png")), (100, 100))
ORANGE_VIRUS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_orange.png")), (100, 100))

BLUE_VIRUS_behitted_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_be_hitted.png")), (50, 50))
RED_VIRUS_behitted_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_red_be_hitted.png")), (70, 70))
YELLOW_VIRUS_behitted_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_yellow_be_hitted.png")), (80, 80))
BLACK_VIRUS_behitted_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_black_be_hitted.png")), (100, 100))
ORANGE_VIRUS_behitted_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_orange_be_hitted.png")), (100, 100))

# tower image
TOWER_IMG_PL = pygame.transform.scale(pygame.image.load(os.path.join("images", "tower.png")), (TOWER_WIDTH, TOWER_HEIGHT))
TOWER_IMG_CP = pygame.transform.scale(pygame.image.load(os.path.join("images", "tower 2.png")), (TOWER_WIDTH, TOWER_HEIGHT))

PAUSE_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "game pause.png")), (60, 60))
CONTINUE_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "game continue.png")), (120, 120))

# -------------------------------------------------------------------------------------------------------------
# cat image for day game
NORMAL_CAT_IMAGE_D = pygame.transform.scale(pygame.image.load(os.path.join("images", "cat.png")), (80, 85))
MASK_CAT_IMAGE_D = pygame.transform.scale(pygame.image.load(os.path.join("images", "mask_cat.png")), (80, 85))
SANI_CAT_IMAGE_D = pygame.transform.scale(pygame.image.load(os.path.join("images", "sanitizer_cat.png")), (110, 110))
VACCINE_CAT_IMAGE_D = pygame.transform.scale(pygame.image.load(os.path.join("images", "vaccine_cat.png")), (95, 100))
ALCOHOL_CAT_IMAGE_D = pygame.transform.scale(pygame.image.load(os.path.join("images", "alcohol_cat.png")), (105, 100))

NORMAL_CAT_ATTACK_IMAGE_D = pygame.transform.scale(pygame.image.load(os.path.join("images", "cat_attack.png")), (80, 85))
MASK_CAT_ATTACK_IMAGE_D = pygame.transform.scale(pygame.image.load(os.path.join("images", "mask_cat_attack.png")), (80, 85))
SANI_CAT_ATTACK_IMAGE_D = pygame.transform.scale(pygame.image.load(os.path.join("images", "sanitizer_cat_attack.png")), (110, 110))
VACCINE_CAT_ATTACK_IMAGE_D = pygame.transform.scale(pygame.image.load(os.path.join("images", "vaccine_cat_attack.png")), (95, 100))
ALCOHOL_CAT_ATTACK_IMAGE_D = pygame.transform.scale(pygame.image.load(os.path.join("images", "alcohol_cat_attack.png")), (105, 100))


# virus image
virus_size_M = 110
BLUE_VIRUS_IMAGE_M = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus.png")), (virus_size_M, virus_size_M))
RED_VIRUS_IMAGE_M = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_red.png")), (virus_size_M, virus_size_M))
YELLOW_VIRUS_IMAGE_M = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_yellow.png")), (virus_size_M, virus_size_M))
BLACK_VIRUS_IMAGE_M = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_black.png")), (virus_size_M, virus_size_M))
ORANGE_VIRUS_IMAGE_M = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_orange.png")), (virus_size_M, virus_size_M))

BLUE_VIRUS_IMAGE_S = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus.png")), (50, 50))
RED_VIRUS_IMAGE_S = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_red.png")), (50, 50))
YELLOW_VIRUS_IMAGE_S = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_yellow.png")), (50, 50))
BLACK_VIRUS_IMAGE_S = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_black.png")), (60, 60))
ORANGE_VIRUS_IMAGE_S = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus_orange.png")), (60, 60))


# heart image for day game
HEART = pygame.transform.scale(pygame.image.load(os.path.join("images", "heart.png")), (30, 30))
HEART_DEAD = pygame.transform.scale(pygame.image.load(os.path.join("images", "heart_dead.png")), (30, 30))

#
VIRUS_COUNT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "knock_down_count.png")), (200, 55))

