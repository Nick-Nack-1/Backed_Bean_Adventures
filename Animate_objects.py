import pygame
from Globals import *


def Monster_setup():
    pass








class Monster(pygame.sprite.Sprite):
    def __init__(self,scrn, dir_points):
        super(Monster, self).__init__()
        self.image = pygame.image.load(DEFAULT_TEXTURE).convert_alpha()
        self.rect = self.image.get_rect()