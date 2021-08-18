import pygame
from settings import *
from all_image import *
from color_settings import *


class GameView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def draw_bg(self):
        self.win.blit(BACKGROUND_IMAGE, (0, 0))

    def draw_enemies(self, enemies):
        enemies.tower.draw(self.win)
        for virus in enemies.get():
            self.win.blit(virus.image, virus.rect)

    def draw_ally(self, allies):
        allies.tower.draw(self.win)
        for cat in allies.get():
            self.win.blit(cat.image, cat.rect)

    def draw_knock_down_number(self, model):
        # 呈現打倒幾個病毒的數字
        self.win.blit(VIRUS_COUNT_IMAGE, (400, 10))
        num = model.knocked_down_num
        font = pygame.font.SysFont("consolas", 40)
        text = font.render(f"{num}", True, (5, 5, 5))
        self.win.blit(text, (600+len(str(num))*5, 13))

    def draw_menu(self, menu):
        """the menu is the button menu in the game"""
        for but in menu.get_buttons():
            self.win.blit(but.image, but.rect)
            if but.virus_image is not None:
                self.win.blit(but.virus_image, (but.rect.centerx+20, but.rect.centery+20))
            if but.key_object is not None:
                font = pygame.font.SysFont("microsofthimalaya", 40, bold=True)
                text = font.render(f"{but.key_object}", True, (1, 46, 103))
                self.win.blit(text, (but.rect.centerx-50, but.rect.centery+40))

    def draw_game_over(self, game_over_type):
        """draw the scene when game over"""
        game_over_type.draw(self.win)

    def draw_pause_scene(self, pause_menu):
        """draw the pause menu when game is paused"""
        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surface, (255, 255, 255, 100), [0, 0, WIN_WIDTH, WIN_HEIGHT], 0)
        surface.set_alpha(128)
        self.win.blit(BACKGROUND_IMAGE, (0, 0))
        self.win.blit(surface, (0, 0))
        for but in pause_menu.get_buttons():
            self.win.blit(but.image, but.rect)

    def draw_user_guide_scene(self, user_guide_menu, guide_claim):
        """draw the game guide when the first level starts"""
        user_guide = user_guide_day_list
        guide_page = guide_claim.guide_count
        self.win.fill(WHITE)
        self.win.blit(user_guide[guide_page], (0, 0))
        for but in user_guide_menu.get_buttons():
            self.win.blit(but.image, but.rect)


