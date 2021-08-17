import pygame
from menu.page_controller import Page_controller
from settings import WIN_WIDTH, WIN_HEIGHT, FPS

pygame.init()
pygame.mixer.init()


class StartMenu:
    """the menu in front of the game start, including the opening"""
    def __init__(self):
        # win
        self.menu_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # set start page as intro
        self.page = 'intro'
        self.page_controller = Page_controller()

    def menu_run(self):
        quit_game = False
        clock = pygame.time.Clock()
        pygame.display.set_caption("Cat-to-vid")

        while not quit_game:
            clock.tick(FPS)
            if self.page.startswith('Lv'):
                self.page_controller.choose_level(self.page)  # 關卡選擇
            self.page = self.page_controller.page_response
            quit_game = self.page_controller.quit
            self.page_controller.choose_menu(self.page)  # 開場 + 主頁面選單
            self.page_controller.receive_user_input()
            self.page_controller.update_menu()
            self.page_controller.update_view()

        pygame.quit()




