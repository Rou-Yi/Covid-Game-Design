import pygame
from menu.start_menu import StartMenu


if __name__ == '__main__':
    pygame.init()
    m = StartMenu()
    m.menu_run()
