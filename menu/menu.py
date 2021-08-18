from button import Button
from all_image import *


class Menu:
    """主畫面選單，用繼承寫白天黑夜兩個版本"""
    def __init__(self, button_list, response, background_image):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.bg_image = background_image
        self.__buttons = button_list
        self.this_menu_response = response
        self.button_response = response

    def draw(self):
        """Draw everything here."""
        # draw background
        self.win.blit(self.bg_image, (0, 0))
        self.win.blit(LOGO_IMAGE_small, (1017, 5))
        # draw button
        for but in self.__buttons:
            self.win.blit(but.image, but.rect)
        pygame.display.update()

    def update(self, events: dict):
        """
        Update for quit event and click button.
        """
        # reset the button_response
        self.button_response = self.this_menu_response

        if events["mouse position"] is not None:
            mouse_x, mouse_y = events["mouse position"]
            for btn in self.__buttons:
                if btn.clicked(mouse_x, mouse_y):
                    btn.play_soundtrack_button()
                    self.button_response = btn.response

    @property
    def response(self):
        return self.button_response

    @classmethod
    def MainMenu_Night(cls):  # 主頁面
        btn_list = [Button(LEVEL_BTN_NIGHT_IMAGE, "level menu night", 400, 200),
                    Button(INTRO_BTN_NIGHT_IMAGE, "introduction night", 800, 200),
                    Button(TIME_CHANGE_IMAGE, "time: night to day", 50, 50),
                    Button(PLAY_BTN, 'play music', 1100, 670), Button(MUTE_BTN, 'pause music', 1165, 670)]
        main_menu = cls(btn_list, 'main menu night', MENU_BG_NIGHT)
        return main_menu

    @classmethod
    def MainMenu_Day(cls):  # 主頁面
        btn_list = [Button(LEVEL_BTN_IMAGE, "level menu day", 400, 200),
                    Button(INTRO_BTN_IMAGE, "introduction day", 800, 200),
                    Button(TIME_CHANGE_IMAGE, "time: day to night", 50, 50),
                    Button(PLAY_BTN, 'play music', 1100, 670), Button(MUTE_BTN, 'pause music', 1165, 670)]
        main_menu = cls(btn_list, 'main menu day', MENU_BG_DAY)
        return main_menu
# -------------------------------------------------------------------------------------


class LevelMenu:
    """關卡選單，包含關卡解鎖控制，用繼承寫白天黑夜兩個版本"""
    def __init__(self, button_list, level_unlock_list, level_locked_list, response, bg_image, return_image):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.bg_image = bg_image
        self.return_image = return_image
        self.__unlock = level_unlock_list
        self.__locked = level_locked_list
        self.this_menu_response = response
        self.button_response = response
        self.return_button = button_list[0]
        self.__buttons = button_list

    def draw(self):
        # draw background
        self.win.blit(self.bg_image, (0, 0))
        self.win.blit(LOGO_IMAGE_small, (1017, 5))
        # draw button
        for but in self.__buttons:
            self.win.blit(but.image, but.rect)
        pygame.display.update()

    def update(self, events: dict):
        # reset the button_response
        self.button_response = self.this_menu_response

        if events["mouse position"] is not None:
            mouse_x, mouse_y = events["mouse position"]
            for btn in self.__buttons:
                if btn.clicked(mouse_x, mouse_y):
                    btn.play_soundtrack_button()
                    self.button_response = btn.response

    def update_level_state(self, level_state: list):
        """update the level state when a new level is unlocked"""
        btn_list = [self.return_button]
        # 如果關卡解鎖就放上解鎖圖按鈕
        btn_list.extend([self.__unlock[i] if level_state[i] else self.__locked[i] for i in range(3)])
        self.__buttons = btn_list

    @property
    def response(self):
        return self.button_response

    @classmethod
    def LevelMenu_Night(cls, level_state):  # 關卡選擇頁面
        btn_list = [Button(RETURN_WHITE_IMAGE, "main menu night", 75, 50)]
        Level_unlock = [Button(LV1_OP_NIGHT_BTN_IMAGE, "Lv_1", 325, 220),
                        Button(LV2_OP_NIGHT_BTN_IMAGE, "Lv_2", 600, 220),
                        Button(LV3_OP_NIGHT_BTN_IMAGE, "Lv_3", 875, 220)]
        Level_locked = ["Level 1 has no locked problem.",
                        Button(LV2_CL_NIGHT_BTN_IMAGE, "level menu night", 600, 220),
                        Button(LV3_CL_NIGHT_BTN_IMAGE, "level menu night", 875, 220)]
        # 如果關卡解鎖就放上解鎖圖按鈕
        btn_list.extend([Level_unlock[i] if level_state[i] else Level_locked[i] for i in range(3)])
        level_menu = cls(btn_list, Level_unlock, Level_locked, 'level menu night', MENU_BG_NIGHT, RETURN_WHITE_IMAGE)
        return level_menu

    @classmethod
    def LevelMenu_Day(cls, level_state):  # 關卡選擇頁面
        btn_list = [Button(RETURN_BLACK_IMAGE, "main menu day", 75, 50)]
        Level_unlock = [Button(LV1_OP_BTN_IMAGE, "Lv_Easy", 325, 220),
                        Button(LV2_OP_BTN_IMAGE, "Lv_Hard", 600, 220),
                        Button(LV3_OP_BTN_IMAGE, "Lv_Infinity", 875, 220)]
        Level_locked = ["Level 1 has no locked problem.",
                        Button(LV2_CL_BTN_IMAGE, "level menu day", 600, 220),
                        Button(LV3_CL_BTN_IMAGE, "level menu day", 875, 220)]
        # 如果關卡解鎖就放上解鎖圖按鈕
        btn_list.extend([Level_unlock[i] if level_state[i] else Level_locked[i] for i in range(3)])
        level_menu = cls(btn_list, Level_unlock, Level_locked, 'level menu day', MENU_BG_DAY, RETURN_BLACK_IMAGE)
        return level_menu
# -------------------------------------------------------------------------------------


class Introduction_Menu:
    """介紹畫面"""
    def __init__(self, response):
        if response == 'night':
            self.this_menu_response = 'introduction night'
            self.button_response = 'introduction night'
            self.__buttons = [Button(RETURN_WHITE_IMAGE, 'main menu night', 75, 50)]
            self.bg_image = MENU_BG_NIGHT
        elif response == 'day':
            self.this_menu_response = 'introduction day'
            self.button_response = 'introduction day'
            self.__buttons = [Button(RETURN_BLACK_IMAGE, 'main menu day', 75, 50)]
            self.bg_image = MENU_BG_DAY

        self.__pages = INTRODUCE_IMAGE_LIST
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.surf = pygame.surface.Surface((WIN_WIDTH, WIN_HEIGHT*9))
        self.scroll = 0

    def draw(self):
        """
        Draw everything here.
        :return: None
        """
        # draw background
        self.win.blit(self.bg_image, (0, 0))
        # draw page
        for i, page in enumerate(self.__pages):
            self.surf.blit(page, (0, WIN_HEIGHT*i))

    def update(self, events: dict):
        # clear the button_response
        self.button_response = self.this_menu_response
        # 接收滾輪使用反應，輸出畫面 y軸 控制 self.scroll
        if events["scroll up"]:
            self.scroll = min(self.scroll + 100, 0)
        if events["scroll down"]:
            self.scroll = max(self.scroll - 100, -WIN_HEIGHT*8)
        # draw the introduction page
        self.win.blit(self.surf, (0, self.scroll))

        # 滾輪最右邊那條 (顯示用，沒有功能 XD)
        color = (170, 164, 160)
        scroll_y = abs(self.scroll/(WIN_HEIGHT*8)) * 618 + 10
        pygame.draw.rect(self.win, color, [1183, scroll_y+2, 16, 60], 0)
        pygame.draw.circle(self.win, color, (1183+8, scroll_y), 8)
        pygame.draw.circle(self.win, color, (1183+8, scroll_y+62), 8)

        # draw button
        for but in self.__buttons:
            self.win.blit(but.image, but.rect)
        self.win.blit(LOGO_IMAGE_small, (1017, 2))
        pygame.display.update()

        if events["mouse position"] is not None:
            mouse_x, mouse_y = events["mouse position"]
            for btn in self.__buttons:
                if btn.clicked(mouse_x, mouse_y):
                    btn.play_soundtrack_button()
                    self.button_response = btn.response

    @property
    def response(self):
        return self.button_response
# -------------------------------------------------------------------------------------


class Time_Changer:
    """ 用來給主畫面切換白天黑夜的過場動畫，用繼承寫白天黑夜兩個版本"""
    def __init__(self, response, next_page, original_bg, target_bg, story_bg):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.original_bg = original_bg
        self.target_bg = target_bg
        self.story_bg = story_bg
        self.this_menu_response = response   # 轉換前的頁面名字
        self.page_response = response  # 現在處於哪個頁面
        self.next_page = next_page  # 轉換後要去的頁面
        self.fade = 'in'
        self.alpha = 0

    def draw(self):
        """ draw everything """
        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        surface.fill((0, 0, 0))
        surface.set_alpha(self.alpha)
        self.win.blit(surface, (0, 0))
        pygame.display.update()

    def update(self, events: dict):
        """ control the screen alpha """
        self.page_response = self.this_menu_response  # clear page_response
        # self.alpha: 淡入黑幕 0 -> 255, 淡出黑幕 255 -> 0
        if self.fade == 'in':
            self.win.blit(self.original_bg, (0, 0))  # 建置原本的頁面背景
            if self.alpha < 255:
                self.alpha += 4
                pygame.time.wait(3)
            else:
                self.fade = 'out'
                pygame.time.wait(3)
        elif self.fade == 'out':
            self.win.blit(self.target_bg, (0, 0))  # 建置後來的 / 要去的頁面背景
            self.win.blit(self.story_bg, (0, 0))  # 建置故事畫面
            if self.alpha > 50:
                self.alpha -= 4
                pygame.time.wait(3)
            elif self.alpha > 0:
                self.alpha -= 1
                pygame.time.wait(9)
            else:
                self.page_response = self.next_page
                self.fade = 'in'  # 重置淡入設定

    @property
    def response(self):
        return self.page_response

    @classmethod
    def Change_to_night(cls):
        night = cls('time: day to night', 'main menu night', MENU_SCENE_DAY, MENU_SCENE_NIGHT, MENU_SCENE_NIGHT_STORY)
        return night

    @classmethod
    def Change_to_Day(cls):
        day = cls('time: night to day', 'main menu day', MENU_SCENE_NIGHT, MENU_SCENE_DAY, MENU_SCENE_DAY_STORY)
        return day



