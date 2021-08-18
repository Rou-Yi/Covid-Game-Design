import pygame


# controller
class GameControl:
    def __init__(self, game_model, game_view):
        self.model = game_model
        self.view = game_view
        self.events = {"game quit": False,
                       "mouse position": [0, 0],
                       }
        self.request = None  # response of user input
        self.play_music = None

    def update_model(self):
        """update the model and the view here"""
        self.request = self.model.get_request(self.events)
        self.model.user_request(self.request)
        self.model.enemies_campaign()
        self.model.allies_attack()
        self.model.enemies_attack()
        self.model.allies_advance()
        self.model.enemies_advance()
        self.model.mana_advance()
        self.model.game_over_advance()
        self.model.force_to_end_game()

    def receive_user_input(self):
        """receive user input from the events"""
        # event initialization
        self.events = {"game quit": False,
                       "mouse position": None,
                       }
        # update event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["game quit"] = True
            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.events["mouse position"] = [x, y]

    def update_view(self):
        # render background
        self.view.draw_bg()
        self.view.draw_menu(self.model.menu)
        self.view.draw_ally(self.model.allies)
        self.view.draw_enemies(self.model.enemies)
        self.view.draw_mana_bar(self.model.mana)

    def update_game_over_view(self):
        """draw the ending page when game is over"""
        self.view.draw_game_over(self.model.result)

    def update_game_over_model(self):
        """update used when game over"""
        self.model.result.update(self.events)

    def update_pause_game(self):
        """update the view and request when game is paused"""
        self.view.draw_pause_scene(self.model.pause)
        self.request = self.model.get_request(self.events)
        self.model.user_request(self.request)

    def update_user_guide(self):
        """update the view and request of user guide in the start of the first level"""
        self.view.draw_user_guide_scene(self.model.user_guide, self.model.user_guide_claim)
        self.request = self.model.get_request(self.events)
        self.model.user_request(self.request)

    def update_music_state(self):
        """update music control"""
        self.request = self.model.get_request(self.events)
        self.model.user_request(self.request)
        if (self.model.music.get_volume() == 0) and self.model.play_music:
            self.play_music = True
        elif (self.model.music.get_volume() > 0) and (self.model.play_music is not True):
            self.play_music = False

    @property
    def quit_game(self):
        return self.events["game quit"]

    @property
    def game_over(self):
        return self.model.game_over

    @property
    def unlock_next_level(self):
        return self.model.unlock_next_level

    @property
    def jump_page_data(self):
        return self.model.result.response, self.model.result.jump_page

    @property
    def pause_game(self):
        return self.model.pause_game

    @property
    def have_user_guide(self):
        return self.model.user_guide_claim.have_user_guide

    @property
    def play_sound(self):
        return self.play_music
