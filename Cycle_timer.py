import time
import pygame

class timer():
    def __init__(self,scn):
        pygame.font.init()
        self.start = time.perf_counter()
        self.time = 0
        self.screen = scn
        self.font1 = pygame.font.SysFont("Amasis MT Pro Light",15)
    

    def stop(self):
        self.time = time.perf_counter()-self.start
        self.start = time.perf_counter()

        text = self.font1.render("speed: "+str(int(self.time*1000))+" ms", 1,(255,255,255))
        self.screen.blit(text, (0, 3))