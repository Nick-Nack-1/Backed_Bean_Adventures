from Globals import speed
import pygame
import math
#  *!4T#P3@iU33@Qm

class Player(pygame.sprite.Sprite):
    def __init__(self,scrn,map):
        super(Player, self).__init__()
    ##DIRECTLY PLR
        self.animate_sheet = None
        ##This is the distance from map origen to plr
        self.map_x = 0
        self.map_y = 0
        self.screen_x = 0
        self.screen_y = 0
    ##NOT DIRECTLY PLR
        self.movement_dir = 0
        self.screen = scrn
        self.map = map
    

    def update(self):
        ##MOVEMENT
        pass


    def animate(self,images, time):
        '''Images is a list of all die seperite images in the animation'''
        '''Time is the amount of cycles between each image changing'''
        '''Will return the next image in the sequince'''
        pass


    def Get_movement(self, move_dir):
        self.movement_dir = move_dir
        ##-1 = move left
        ## 0 = stand still
        ## 1 = move right