import pygame
from settings import *
from all_image import *
from color_settings import *


class GameView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def draw_bg(self):
        self.win.blit(BACKGROUND_NIGHT, (0, 0))

    def draw_enemies(self, enemies):
        enemies.tower.draw(self.win)
        for virus in enemies.get():
            self.win.blit(virus.image, virus.rect)
            # draw health bar
            bar_width = virus.rect.w * (virus.health / virus.max_health)
            max_bar_width = virus.rect.w
            bar_height = 5
            pygame.draw.rect(self.win, RED, [virus.rect.x, virus.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(self.win, GREEN, [virus.rect.x, virus.rect.y - 10, bar_width, bar_height])

    def draw_ally(self, allies):
        allies.tower.draw(self.win)
        for cat in allies.get():
            self.win.blit(cat.image, cat.rect)
            # draw health bar
            bar_width = cat.rect.w * (cat.health / cat.max_health)
            max_bar_width = cat.rect.w
            bar_height = 5
            pygame.draw.rect(self.win, RED, [cat.rect.x, cat.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(self.win, GREEN, [cat.rect.x, cat.rect.y - 10, bar_width, bar_height])

    def draw_menu(self, menu):
        """the menu is the button menu in the game"""
        for but in menu.get_buttons():
            self.win.blit(but.image, but.rect)

    def draw_mana_bar(self, mana_group):
        """draw the magic value on the top of the game"""
        max_bar_width = MANA_W
        bar_width = max_bar_width * (mana_group.mana / mana_group.max_mana)
        bar_height = 20
        pygame.draw.rect(self.win, GRAY, [MANA_X, MANA_Y, max_bar_width, bar_height])
        pygame.draw.rect(self.win, GRAY, pygame.Rect(MANA_X-5, MANA_Y-5, max_bar_width+10, bar_height+10), 2)
        pygame.draw.rect(self.win, WHITE, [MANA_X, MANA_Y, bar_width, bar_height])  # remaining mana

    def draw_game_over(self, game_over_type):
        """draw the scene when game over"""
        game_over_type.draw(self.win)

    def draw_pause_scene(self, pause_menu):
        """draw the pause menu when game is paused"""
        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surface, (255, 255, 255, 100), [0, 0, WIN_WIDTH, WIN_HEIGHT], 0)
        surface.set_alpha(128)
        self.win.blit(BACKGROUND_NIGHT, (0, 0))
        self.win.blit(surface, (0, 0))
        for but in pause_menu.get_buttons():
            self.win.blit(but.image, but.rect)

    def draw_user_guide_scene(self, user_guide_menu, guide_claim):
        """draw the game guide when the first level starts"""
        user_guide = user_guide_night_list
        guide_page = guide_claim.guide_count
        self.win.fill(WHITE)
        self.win.blit(user_guide[guide_page], (0, 0))
        for but in user_guide_menu.get_buttons():
            self.win.blit(but.image, but.rect)



