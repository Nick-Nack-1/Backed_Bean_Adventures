import pygame
import Level_controle
import sprite_sheet
from Globals import *
import Player
import Cycle_timer
# import time

##PYGAME SETUP
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.SCALED | pygame.FULLSCREEN | pygame.RESIZABLE)
fps = 60
clock = pygame.time.Clock()
back_colour = 9,9,9
full_screen = False

##SPRITE SHEETS AND MAPS
Sheet1 = sprite_sheet.read_out("./Maps/Cave Tiles.png")
#Sprite sheet 1 and 2
Sheet2 = sprite_sheet.read_out("./Maps/mines_of_sharega.png")

##SIDEBAR SETUP
#((left,top),(width,height))
rect = pygame.Rect((SCREEN_WIDTH-120,0),(120,SCREEN_HEIGHT))
Side_bar = pygame.Surface(rect.size)

##KEYFLAGS
K_enter_down = False
K_alt_down = False
K_end_down = False

##MAP SETUP
level_nom = 0
Map = Level_controle.map(level_nom, screen) 
# Map = Level_controle.map("./Maps/Test.tmx", screen)

##PLAYER
player = Player.Player(screen, Map)

state = INTRO
running = True
full_screen = True
##DO CYCLE TIMER
Debug_screen = False

##GROUPS
S_Draw = pygame.sprite.Group()
S_Update = pygame.sprite.Group()
S_Draw.add(player)
S_Update.add(player)


def Reset(): #to reset the level
    pass

timer = Cycle_timer.timer(screen)
frm_cnt = 0
t_avg = 0
while running == True:
    if state == PLAY:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_a:
                    ##move left
                    player.Get_movement(-1)
                elif event.key == pygame.K_d:
                    ##move right
                    player.Get_movement(1)
                if event.key == pygame.K_SPACE:
                    ##jump
                    player.Is_Jumping(True)
                
                if event.key == pygame.K_e:
                    player.Interact()
                
                if event.key == pygame.K_END:
                    K_end_down = True

                ##TO GO FULLSCREEN
                if event.key == pygame.K_RETURN:
                    K_enter_down = True
                if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                    K_alt_down = True
                
                ##TOGGLE CYCLE TIMER
                if event.key == pygame.K_F3:
                    Debug_screen = not Debug_screen


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    ##stop moving
                    player.Get_movement(0)
                elif event.key == pygame.K_d:
                    ##stop moving
                    player.Get_movement(0)
                if event.key == pygame.K_SPACE:
                    ##stop jumping
                    pass
                    # player.Is_Jumping(False)

                ##TO GO FULLSCREEN
                if event.key == pygame.K_RETURN:
                    K_enter_down = False
                if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                    K_alt_down = False
        

        ##CHECK FOR FULL SCREEN
        if K_alt_down and K_enter_down:
            full_screen = not full_screen
            K_alt_down = False
            K_enter_down = False
            if full_screen == False: 
                screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.SCALED)
            else:
                screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.SCALED | pygame.FULLSCREEN)


        # t0 = time.perf_counter()
        ##UPDATE
        S_Update.update()
        if player.Is_dead():
            ##ADD DEATHSCREEN LATER
            state = DEAD
        
        if player.Exit() or K_end_down:
            level_nom += 1
            Map = Level_controle.map(level_nom, screen)
            player.Reset(Map)
            K_end_down = False

        ##DRAW
            
        # t1 = time.perf_counter()
        screen.fill(back_colour)
        # t2 = time.perf_counter()
        Map.draw()
        # t3 = time.perf_counter()
        if state == PLAY: 
            S_Draw.draw(screen)
        # t4 = time.perf_counter()
        ##CYCLE COUNTER
        if Debug_screen:
            timer.stop()
            pygame.draw.rect(screen, (255,0,0), ((160, 80),(160,160)), 1 )
        
        ##SIDE_BAR
        Side_bar.fill("#26150a")
        screen.blit(Side_bar, (SCREEN_WIDTH-SIDE_BAR_WIDTH, 0))
        pygame.display.update()

        # t5 = time.perf_counter()    

        # t_avg += (t3-t2)
        # frm_cnt += 1
        # if frm_cnt % 60 == 0:
        #     frm_cnt = 0
        #     print(f"{t1-t0:.4f}, {t2-t1:.4f}, {t_avg/60:.4f}, {t4-t3:.4f}, {t5-t4:.4f}")
        #     t_avg = 0


    if state == INTRO:
        state = MENU
        ##MORE WILL BE ADDED HERE LATER


    if state == MENU:
        state = PLAY
        ##MORE WILL BE ADDED HERE LATER
    
    if state == DEAD:
        running = False
        state = INTRO
        ##MORE WILL BE ADDED HERE LATER

if state == DEAD or not running:
    pygame.quit()
    quit()