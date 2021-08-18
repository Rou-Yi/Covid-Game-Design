import pygame
import random
from _day.tower.tower import Tower
from _day.enemy.virus import Virus
from _day.level_setting import level_setting


class EnemyGroup:
    def __init__(self, level):
        self.enemy_num = 0
        self.enemy_num_max = level_setting[level]['enemy_num']    # 病毒數量
        self.enemy_speed = level_setting[level]['enemy_speed']    # 病毒移動速度
        self.virus_type_num = level_setting[level]['button_num']  # 病毒使用種類數量
        self.__expedition = [Virus.Black_Virus(self.enemy_speed)]
        self.tower = Tower.Enemy_tower()
        self.hp_count = False  # used in self.advance() to check tower is dead
        self.campaign_count = 0
        self.campaign_max_count = level_setting[level]['campaign_count']  # 病毒派兵速度

    def advance(self, player_group):
        """check the movement and health of virus and their tower
           and return True when the tower is dead"""
        # Virus 移動 & 血量判斷
        for virus in self.__expedition:
            # Control the move
            if virus.health <= 0:
                if virus.attack_tower:
                    self.retreat(virus)
                else:
                    dead = virus.retreat_move()
                    if dead:
                        self.retreat(virus)
            else:
                if virus.check_moving():
                    virus.move()

        # Enemy Tower 血量判斷
        if self.tower.health == 0:
            return True
        return False

    def campaign(self):
        """Enemy go on an expedition."""
        virus_list = [Virus.Black_Virus(self.enemy_speed), Virus.Blue_Virus(self.enemy_speed),
                      Virus.Orange_Virus(self.enemy_speed), Virus.Yellow_Virus(self.enemy_speed),
                      Virus.Red_Virus(self.enemy_speed)][:self.virus_type_num]
        if (self.campaign_count > self.campaign_max_count) and (self.enemy_num < self.enemy_num_max):
            self.__expedition.append(random.choice(virus_list))
            self.campaign_count = 0
            self.enemy_num += 1
        else:
            self.campaign_count += 1

    def retreat(self, virus):
        """
        Remove the enemy from the expedition
        :param virus: class Virus()
        :return: None
        """
        self.__expedition.remove(virus)

    def get(self):
        """
        To return the enemy list.
        """
        return self.__expedition

    def is_empty(self):
        return True if self.__expedition == [] else False




