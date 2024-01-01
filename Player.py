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
        self.spawn_point = map.tmxdata.get_object_by_name("Spawn_plr")
        self.map_x = self.spawn_point.x
        self.map_y = self.spawn_point.y
        self.screen_x = 0
        self.screen_y = 0
        self.state = STANDING
        self.jump_timer = 0 #Frame based
        self.jump_y_start = 0 #the y coord were the jump started

        self.plr_rect = pygame.Rect((self.map_x, self.map_y), (TILE_SIZE, TILE_SIZE)) 
    ##NOT DIRECTLY PLR
        self.movement_dir = 0
        self.screen = scrn
        self.dead_anm_done = False #Death_animation_done
        self.map = map
        self.collide_box = (6, TILE_SIZE) #This will be used to test tile collisions

        self.jump_scedule = [] ##THIS WILL CONTAIN ALL THE STEPS OR DELTA_Y'S FOR JUMPING
        previous_jump = 0
        for i in range(JUMPDURATION):
            curren_jump = -(48/900)*((i)-(JUMPDURATION//2))**2+48
            self.jump_scedule.append(curren_jump-previous_jump)
            previous_jump = curren_jump
    ##ANIMATIONS
        self.stand_animate = sprite_sheet.animate(4, 4)
        self.stand_animate.Set_sheet("./Images/player_standing.png")
        self.stand_animate.Set_speed(60)

        self.run_animation = sprite_sheet.animate(5,5)
        self.run_animation.Set_sheet("./Images/player_run.png")
        self.run_animation.Set_speed(9)

        self.death_animation = sprite_sheet.animate(5,5)
        self.death_animation.Set_sheet("./Images/Cinamon_roll_unrapping.png")
        self.death_animation.Set_speed(90)
    

    def update(self):
        if self.state != DEAD:
            ##MOVEMENT
            self.map_x += self.movement_dir*speed
            Collisions = self.map.Check_Collisions((self.map_x+5,self.map_y), (self.collide_box[0],self.collide_box[1]-1))
            if "TR" in Collisions or "BR" in Collisions:
                self.map_x = ((self.map_x//TILE_SIZE)*TILE_SIZE)+4
            elif "TL" in Collisions or "BL" in Collisions:
                self.map_x = (((self.map_x+15)//TILE_SIZE)*TILE_SIZE)-5

            ##JUMPING
            if self.state == JUMPING:
                self.jump_timer += 1
                if self.jump_timer > JUMPDURATION-1:
                    # self.movement_dir = 0
                    self.state = RUNNING
                else:
                    self.map_y -= self.jump_scedule[self.jump_timer] 
                Collisions = self.map.Check_Collisions((self.map_x+5,self.map_y), self.collide_box)
                if "TL" in Collisions or "TR" in Collisions:
                        self.map_y = ((self.map_y+15)//TILE_SIZE)*TILE_SIZE
                        self.state = RUNNING
                elif self.jump_timer > JUMPDURATION//2-1:
                    if "BL" in Collisions or "BR" in Collisions:
                        # self.movement_dir = 0
                        self.map_y = (self.map_y//TILE_SIZE)*TILE_SIZE
                        self.state = RUNNING


            ##GRAVITY
            if self.state != JUMPING:
                Collisions = self.map.Check_Collisions((self.map_x+5,self.map_y), (self.collide_box[0], self.collide_box[1]+1))
                self.map_y += FALL_SPEED
                if "BL" in Collisions or "BR" in Collisions:
                    self.map_y = ((self.map_y//TILE_SIZE)*TILE_SIZE)
                # if not("BL" in Collisions or "BR" in Collisions):
                #     self.map_y += FALL_SPEED
                # else:
                #     self.map_y = (self.map_y//TILE_SIZE)*TILE_SIZE

            ##Updates the screen pos
            self.rect.x,self.rect.y = self.map.Calculate_screen_pos((self.map_x,self.map_y))

            ##UPDATE STATE
            if self.movement_dir == 0 and self.state != JUMPING:
                self.state = STANDING
            elif self.movement_dir != 0 and self.state != JUMPING:
                self.state = RUNNING

            ##ANIMATIONS
            if self.state == STANDING:
                picture = self.stand_animate.Play()
                if picture != None:
                    self.image = picture[0]
            if self.state in [RUNNING, JUMPING]:
                picture = self.run_animation.Play()
                if picture != None:
                    if self.movement_dir == -1:
                        self.image = pygame.transform.flip(picture[0], True, False)
                    else:
                        self.image = picture[0]
            
            self.Boundry_box()

            ##Updates the screen pos
            self.rect.x,self.rect.y = self.map.Calculate_screen_pos((self.map_x,self.map_y))

        elif not self.dead_anm_done:
            for i in range(5):
                picture = self.death_animation.Play()
                if picture != None:
                    self.image = picture[0]
                    if picture[1]: #This checks if the animation has finished
                        self.dead_anm_done = True


    
    def Is_Jumping(self, is_jumping):
        if is_jumping:
            Collisions = self.map.Check_Collisions((self.map_x+5,self.map_y), self.collide_box)
            if "BL" in Collisions or "BR" in Collisions:
        ## if is_jumping and not self.map.Chack_falling((self.map_x+5,self.map_y), (6, TILE_SIZE)):
                self.state = JUMPING
                self.jump_timer = 0
                self.jump_y_start = self.map_y


    def Get_movement(self, move_dir):
        # if self.state != JUMPING:
        self.movement_dir = move_dir
        
            ##-1 = move left
            ## 0 = stand still
            ## 1 = move right
    

    def Interact(self):
        ##This will be called by main
        self.map.tile_interact((int((self.map_x+TILE_SIZE/2)/TILE_SIZE),int((self.map_y+TILE_SIZE/2)/TILE_SIZE)))

    
    def Is_dead(self):
        test_tiles = self.map.Test_tile(DANGER, 
                                        (self.map_x,self.map_y), 
                                        (self.collide_box[0],self.collide_box[1]-1))
        if len(test_tiles) != 0:
            for T in test_tiles:
                if "Will_kill" in T:
                    if T["Will_kill"]:
                        ##If it will kill the player.
                        self.state = DEAD
        if self.dead_anm_done:
            return True
        return False
    

    def Boundry_box(self):
        screen_x,screen_y = self.map.Calculate_screen_pos((self.map_x,self.map_y))
        x_dif = int(screen_x - SCREEN_CENTRE[0])
        y_dif = int(screen_y - SCREEN_CENTRE[1])
        if abs(x_dif) > (5*TILE_SIZE): ##If the player is outside the boundry box
            # print("x")
            if x_dif < 0:
                self.map.Panning("l",screen_x-LEFT_B)
            elif x_dif > 0:
                self.map.Panning("r",screen_x-RIGHT_B)
            
        if abs(y_dif) > (5*TILE_SIZE): ##If the player is outside the boundry box
            if y_dif < 0:
                self.map.Panning("t",screen_y-TOP_B)
            elif y_dif > 0:
                self.map.Panning("b",screen_y-BOTTOM_B)


    def Exit(self):
        self.plr_rect = pygame.Rect((self.map_x, self.map_y), (TILE_SIZE, TILE_SIZE))
        return self.map.Exit_Check(self.plr_rect)
    

    def Reset(self, map):
        self.map = map
        self.spawn_point = map.tmxdata.get_object_by_name("Spawn_plr")
        self.map_x = self.spawn_point.x
        self.map_y = self.spawn_point.y

    