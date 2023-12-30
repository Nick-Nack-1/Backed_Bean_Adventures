import time
import pytmx
import pygame

def opt1(times):
    screen = pygame.display.set_mode((10,10))
    tmxdata = pytmx.load_pygame("./Maps/Test.tmx")
    for t in range(times):
        tmxdata.get_tile_image(0, 0, 0)

def opt2(times):
    screen = pygame.display.set_mode((10,10))
    tmxdata = pytmx.load_pygame("./Maps/Test.tmx")
    for t in range(times):
        tmxdata.get_tile_properties(0, 0, 0)


def test_time(f, times):
    start = time.perf_counter()
    f(times)
    stop = time.perf_counter()
    print(str(stop-start))
