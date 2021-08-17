from all_image import *
from button import Button


class Intro:  # 起始畫面
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        self.bg_image = MENU_BG_NIGHT
        self.logo_image = LOGO_IMAGE
        self.alpha = 0
        self.fade = 'in'
        self.intro_response = 'intro'
        self.volume_choose = Volume_Choose_Menu()
        self.music_count = 1

    def draw(self):
        self.surface.blit(self.bg_image, (0, 0))  # draw background
        self.surface.blit(self.logo_image, (237, 150))  # draw logo on a transparent surface

    def play_opening_soundtrack(self):
        pygame.mixer.music.load("./sound/Opening (mixkit-unlock game notification 253).wav")
        pygame.mixer.music.set_volume(self.volume_choose.volume)
        pygame.mixer.music.play(0)  # 播放一次

    def update(self, events: dict):
        if self.volume_choose.user_device is None:
            self.volume_choose.draw(self.win)
            self.volume_choose.update(events)
        else:
            if self.music_count:
                self.play_opening_soundtrack()
                self.music_count = 0
            if self.fade == 'in':
                if self.alpha < 255:
                    self.alpha += 5
                    self.surface.set_alpha(self.alpha)
                    self.win.blit(self.surface, (0, 0))
                    pygame.time.wait(2)
                else:
                    self.fade = 'out'
                    self.alpha = 200

            elif self.fade == 'out':
                self.win.blit(self.bg_image, (0, 0))  # every time draw a new background
                if self.alpha > 0:
                    self.alpha -= 4
                    self.surface.set_alpha(self.alpha)
                    self.win.blit(self.surface, (0, 0))
                else:
                    self.intro_response = 'main menu night'
        pygame.display.update()

    @property
    def response(self):
        return self.intro_response

    @property
    def volume(self):
        return self.volume_choose.volume


class Volume_Choose_Menu:
    def __init__(self):
        self.__buttons = [Button(VOLUME_COMPUTER, "computer", 400, 400),
                          Button(VOLUME_EARPHONE, "earphone", 800, 400)]
        self.this_menu_response = 'volume choose'
        self.device = None
        self.volume_setting = 0.2

    def draw(self, win):
        """
        Draw everything here.
        :return: None
        """
        # draw background
        win.blit(MENU_BG_NIGHT, (0, 0))
        win.blit(VOLUME_BG, (0, 0))
        # draw button
        for but in self.__buttons:
            win.blit(but.image, but.rect)

    def update(self, events: dict):
        if events["mouse position"] is not None:
            mouse_x, mouse_y = events["mouse position"]
            for btn in self.__buttons:
                if btn.clicked(mouse_x, mouse_y):
                    btn.play_soundtrack_button()
                    # 根據裝置選擇，從設定讀取音量設置
                    self.device = btn.response
                    self.volume_setting = volume[self.device]

    @property
    def user_device(self):
        return self.device

    @property
    def volume(self):
        return self.volume_setting
