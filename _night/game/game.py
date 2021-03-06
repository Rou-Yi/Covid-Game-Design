import pygame
from _night.game.controller import GameControl
from _night.game.model import GameModel
from _night.game.view import GameView
from settings import FPS


class Game_night:
    def __init__(self, level, volume_setting, current_volume):
        self.sound = pygame.mixer.Sound("./sound/Game Background Music (mixkit-sports-rock-78).mp3")
        self.music_volume = volume_setting  # 獲取外部音量設定 (根據一開始的裝置選擇)
        self.sound.play(loops=-1, fade_ms=1000)  # 播放遊戲內音樂
        self.sound.set_volume(current_volume)  # 根據原本的播放音量來設定音量(主音樂靜音就跟著靜音)

        self.game_model = GameModel(level, self.sound)  # core of the game (database, game logic...)
        self.game_view = GameView()  # render everything
        self.game_control = GameControl(self.game_model, self.game_view)  # deal with the game flow and user request
        self.quit_game = False
        self.level = level

    def run(self):
        # initialization pygame.init()
        game_over = False
        jump_page = False
        but_response = 'main menu night'
        while not self.quit_game:
            pygame.time.Clock().tick(FPS)  # control the frame rate
            if not game_over:
                # for game start
                self.game_control.receive_user_input()  # receive user input
                if self.game_control.have_user_guide:
                    self.game_control.update_user_guide()  # update the view for user guide
                elif self.game_control.pause_game is not True:
                    self.game_control.update_model()  # update the model
                    self.game_control.update_view()  # update the view
                else:
                    self.game_control.update_pause_game()  # update the view when pause game
                    self.game_control.update_music_state()

                if self.game_control.play_sound is not None:  # 音樂控制
                    if self.game_control.play_sound:
                        self.sound.set_volume(self.music_volume)
                    else:
                        self.sound.set_volume(0)

                pygame.display.update()
                self.quit_game = self.game_control.quit_game
                game_over = self.game_control.game_over
            else:
                # for game over
                self.game_control.update_game_over_view()
                pygame.display.update()
                while not jump_page:
                    self.game_control.receive_user_input()  # receive user input
                    self.game_control.update_game_over_model()
                    but_response, jump_page = self.game_control.jump_page_data  # but_response: 準備跳去的頁面
                    self.quit_game = self.game_control.quit_game
                    if self.quit_game:
                        break
                break
        self.sound.stop()  # 停止播放遊戲音樂
        return but_response, self.game_control.unlock_next_level

    @property
    def quit(self):
        return self.quit_game



