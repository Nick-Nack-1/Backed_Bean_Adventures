import pygame
import Level_controle
import sprite_sheet
from Globals import *


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
rect = pygame.Rect((800,0),(192,640))
side_bar = pygame.Surface(rect.size)

##KEYFLAGS
K_enter_down = False
K_alt_down = False

##MAP SETUP
Map = Level_controle.map("./Maps/Test.tmx", screen)

running = True
full_screen = True

while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            ##TO GO FULLSCREEN
            if event.key == pygame.K_RETURN:
                K_enter_down = True
            if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                K_alt_down = True

        if event.type == pygame.KEYUP:

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


    ##DRAW
    screen.fill(back_colour)
    Map.draw()
    pygame.display.update()


pygame.quit()
quit()