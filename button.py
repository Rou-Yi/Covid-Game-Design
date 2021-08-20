import pygame


class Button:
    def __init__(self, image, name, x, y):
        self.name = name    # name of the button
        self.image = image  # image of the button
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the menu image

    def clicked(self, x, y):
        """
        Return Whether the button is clicked
        :return: bool
        """
        return True if self.rect.collidepoint(x, y) else False

    def play_soundtrack_button(self):
        pygame.mixer.music.load("./sound/Button (mixkit-game ball tap 2073).wav")
        pygame.mixer.music.play(0)

    @property
    def response(self):
        return self.name

