import sprite_sheet
import pygame

screen = pygame.display.set_mode((10,10))
fps = 60
clock = pygame.time.Clock()
back_colour = 9,9,9

sheet = "./Images/player_run.png"

animate1 = sprite_sheet.animate(5, 5)
animate1.Set_sheet(sheet)
animate1.Set_speed(2)

for i in range(20):
    print(animate1.Play())
    print(".")

quit()