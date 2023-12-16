import pytmx
from Globals import TILE_SIZE


class map():
    def __init__(self, map_file, scn):
        self.screen = scn
        self.tmxdata = pytmx.load_pygame(map_file)
        self.map_file = map_file
        #This is the pixel offset between the map origen(top-left) and the screen origen(0,0)
        self.offset_x = 0
        self.offset_y = 0
        self.back_tint = self.tmxdata.get_layer_by_name("Background").tintcolor
    
    

    def draw(self):
        for y in range (self.tmxdata.height):
            for x in range (self.tmxdata.width):
                ##PLATEFORMS            
                tile_image = self.tmxdata.get_tile_image(x+self.offset_x//TILE_SIZE,
                                                         y+self.offset_y//TILE_SIZE,
                                                         2)
                if tile_image != None:
                    self.screen.blit(tile_image, (x*TILE_SIZE-(self.offset_x%TILE_SIZE), y*TILE_SIZE-(self.offset_y%TILE_SIZE)))
                
                ##MID GROUND
                tile_image = self.tmxdata.get_tile_image(x+self.offset_x//TILE_SIZE,
                                                         y+self.offset_y//TILE_SIZE,
                                                         1)
                if tile_image != None:
                    self.screen.blit(tile_image, (x*TILE_SIZE-(self.offset_x%TILE_SIZE), y*TILE_SIZE-(self.offset_y%TILE_SIZE)))
                
                ##BACKGROUND
                tile_image = self.tmxdata.get_tile_image(x+self.offset_x//TILE_SIZE,
                                                         y+self.offset_y//TILE_SIZE,
                                                         0)
                if tile_image != None:
                    ##If the Background tint clour isn't black then it gets a gray tint
                    ##If you dont want a tint clour make the tint colour Black(#000000)
                    if self.back_tint != "#000000":
                        tile_image.set_alpha(20)
                    self.screen.blit(tile_image, (x*TILE_SIZE-(self.offset_x%TILE_SIZE), y*TILE_SIZE-(self.offset_y%TILE_SIZE)))
                    tile_image.set_alpha(255)
    