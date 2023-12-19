from Globals import *
import pygame
import math
import sprite_sheet
#  *!4T#P3@iU33@Qm

class Player(pygame.sprite.Sprite):
    def __init__(self,scrn,map):
        super(Player, self).__init__()
    ##DIRECTLY PLR
        ##This is the distance from map origen to plr
        self.image = pygame.image.load(DEFAULT_TEXTURE).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
        self.map_x = 0
        self.map_y = 0
        self.screen_x = 0
        self.screen_y = 0
        self.state = STANDING
    ##NOT DIRECTLY PLR
        self.movement_dir = 0
        self.screen = scrn
        self.map = map
    ##ANIMATIONS
        self.stand_animate = sprite_sheet.animate(4, 4)
        self.stand_animate.Set_sheet("./Images/player_standing.png")
        self.stand_animate.Set_speed(60)
    

    def update(self):
        ##MOVEMENT
        if self.state == STANDING:
            picture = self.stand_animate.Play()
            if picture != None:
                print(picture)
                self.image = picture
            # self.rect = self.image.get_rect()





    def Get_movement(self, move_dir):
        self.movement_dir = move_dir
        ##-1 = move left
        ## 0 = stand still
        ## 1 = move right
        # if self.movement_dir == 0:
        #     self.state = STANDING
        # elif self.movement_dir != 0:
        #     self.state = RUNNING