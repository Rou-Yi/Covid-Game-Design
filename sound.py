import pygame
import os


def play_soundtrack_win():
    pygame.mixer.music.load("./sound/Game Win (mixkit-game level completed 2059).wav")
    pygame.mixer.music.play(0)


def play_soundtrack_loss():
    pygame.mixer.music.load("./sound/Game Lose (mixkit-arcade retro game over 213).wav")
    pygame.mixer.music.play(0)



def cat_dead_soundtrack():
    pygame.mixer.music.load("./sound/Cat dead(mixkit-little-cat-pain-meow-87).wav")
    pygame.mixer.music.play(0)


def cat_attack_soundtrack():
    pygame.mixer.music.load("./sound/Cat attack(mixkit-angry-cartoon-kitty-meow-94).wav")
    pygame.mixer.music.play(0)


def virus_dead_soundtrack():
    pygame.mixer.music.load("./sound/virus dead(mixkit-short-explosion-1694).wav")
    pygame.mixer.music.play(0)


def virus_attack_soundtrack():
    pygame.mixer.music.load(os.path.join("sound", "virus attack (mixkit-falling-on-undergrowth-390).wav"))
    pygame.mixer.music.play(0)


