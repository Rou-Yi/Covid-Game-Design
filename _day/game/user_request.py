import pygame
from _day.ally.cat import Cats
"""This module is import in model.py"""

"""
Here we demonstrate how does the Observer Pattern work
Once the subject updates, if will notify all the observer who has register the subject
"""


class RequestSubject:
    def __init__(self, model):
        self.__observers = []
        self.model = model

    def register(self, observer):
        self.__observers.append(observer)

    def notify(self, user_request):
        for o in self.__observers:
            o.update(user_request, self.model)


class CatsChanger:
    def __init__(self, subject):
        subject.register(self)
        self.cat_name = ['normal', 'mask', 'sanitizer', 'alcohol', 'vaccine']

    def update(self, user_request: str, model):
        """clear cat list and add a new cat"""
        for name in self.cat_name:
            if user_request == name:
                cats_dict = {'normal': Cats.Normal_Cat(), 'mask': Cats.Mask_Cat(),
                             'sanitizer': Cats.Sanitizer(), 'alcohol': Cats.Alcohol(),
                             'vaccine': Cats.Vaccine()}
                new_cats = cats_dict[user_request]
                model.allies.clear()
                # 點擊按鈕，換貓咪
                model.allies.get().append(new_cats)


class Pause_game:
    def __init__(self, subject):
        subject.register(self)
        self.pause_game = False
        self.force_end_game = False
        self.play_music = True

    def update(self, user_request: str, model):
        if user_request == "pause game":
            self.pause_game = True
        elif user_request == "continue game":
            self.pause_game = False
        elif user_request == "force end":
            self.force_end_game = True
            self.pause_game = False
        elif user_request == "play music":
            self.play_music = True
        elif user_request == "pause music":
            self.play_music = False


class Guide:
    def __init__(self, subject, level):
        subject.register(self)
        if level == 'Easy':
            self.have_user_guide = True
        else:
            self.have_user_guide = False
        self.guide_count = 0

    def update(self, user_request: str, model):
        if user_request == "navigation_prev":
            if self.guide_count > 0:
                self.guide_count -= 1
        elif user_request == "navigation_next":
            if self.guide_count < 4:
                self.guide_count += 1
            elif self.guide_count >= 4:
                self.have_user_guide = False

