from _night.ally.cat import Cats
from _night.level_setting import level_setting

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


class CatsGenerator:
    def __init__(self, subject, level):
        subject.register(self)
        self.cats_name = ['normal', 'mask', 'sanitizer', 'alcohol', 'vaccine']

    def update(self, user_request: str, model):
        """add new cat"""
        for name in self.cats_name:
            if user_request == name:
                cats_dict = {'normal': Cats.Normal_Cat(), 'mask': Cats.Mask_Cat(),
                             'sanitizer': Cats.Sanitizer(), 'alcohol': Cats.Alcohol(),
                             'vaccine': Cats.Vaccine()}
                new_cats = cats_dict[user_request]

                if model.mana_value >= new_cats.get_cost:
                    model.mana_value -= new_cats.get_cost
                    model.mana.mana_update(model.mana_value)
                    model.allies.get().append(new_cats)
                    # The last step also means 'campaign cats'


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
        if level == 'Lv_1':
            self.have_user_guide = True
        else:
            self.have_user_guide = False
        self.guide_count = 0

    def update(self, user_request: str, model):
        if user_request == "navigation_prev":
            if self.guide_count > 0:
                self.guide_count -= 1
        elif user_request == "navigation_next":
            if self.guide_count < 3:
                self.guide_count += 1
            elif self.guide_count >= 3:
                self.have_user_guide = False

