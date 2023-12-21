import pytmx
from Globals import TILE_SIZE, FALL_SPEED


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
                ##BACKGROUND
                tile_image = self.tmxdata.get_tile_image(x+self.offset_x//TILE_SIZE,
                                                         y+self.offset_y//TILE_SIZE,
                                                         0)
                if tile_image != None:
                    ##If the Background tint clour isn't black then it gets a gray tint
                    ##If you dont want a tint clour make the tint colour Black(#000000)
                    if self.back_tint != "#000000":
                        tile_image.set_alpha(100)
                    self.screen.blit(tile_image, (x*TILE_SIZE-(self.offset_x%TILE_SIZE), y*TILE_SIZE-(self.offset_y%TILE_SIZE)))
                    tile_image.set_alpha(255)
                
                ##MID GROUND
                tile_image = self.tmxdata.get_tile_image(x+self.offset_x//TILE_SIZE,
                                                         y+self.offset_y//TILE_SIZE,
                                                         1)
                if tile_image != None:
                    self.screen.blit(tile_image, (x*TILE_SIZE-(self.offset_x%TILE_SIZE), y*TILE_SIZE-(self.offset_y%TILE_SIZE)))

                ##PLATEFORMS            
                tile_image = self.tmxdata.get_tile_image(x+self.offset_x//TILE_SIZE,
                                                         y+self.offset_y//TILE_SIZE,
                                                         2)
                if tile_image != None:
                    self.screen.blit(tile_image, (x*TILE_SIZE-(self.offset_x%TILE_SIZE), y*TILE_SIZE-(self.offset_y%TILE_SIZE)))
               

    def Calculate_screen_pos(self, sprite_pos):
        ##Turns the map pos that is inserted to screen pos 
        return (sprite_pos[0]-self.offset_x, sprite_pos[1]-self.offset_y)
    
    # def Chack_falling(self, pos, rect):
    #     ##pos = Map pos
    #     ##rect = (width, height)
    #     #Bottem Left
    #     BL = (int(pos[0]/TILE_SIZE), int((pos[1]+rect[1]+1)/TILE_SIZE))
    #     #Bottem Right
    #     BR = (int((pos[0]+rect[0])/TILE_SIZE), int((pos[1]+rect[1]+1)/TILE_SIZE))

    #     #BR is not on tile flag
    #     BR_fall = False
    #     #Bl is not on tile flag
    #     BL_fall = False 
    #     tile = self.tmxdata.get_tile_image(BL[0], BL[1], 2)
    #     if tile == None:
    #         BL_fall = True
    #     tile = self.tmxdata.get_tile_image(BR[0], BR[1], 2)
    #     if tile == None:
    #         BR_fall = True
        
    #     if BL_fall and BR_fall:
    #         #If both corners(BL and BR) are in the air
    #         return True
    #     else:
    #         return False
    

    def Check_Collisions(self, pos, rect):
        ##pos = (map_x, map_y)
        ##rect = (width, height)

        all_colide_corners = []

        ##Top Left
        TL = (int(pos[0]/TILE_SIZE), int((pos[1]+2)/TILE_SIZE)) #The +2 is just that it is a bit lower than 16
        ##Top Right
        TR = (int((pos[0]+rect[0])/TILE_SIZE), int((pos[1]+2)/TILE_SIZE))
        ##Bottom Left
        BL = (int(pos[0]/TILE_SIZE), int((pos[1]+rect[1])/TILE_SIZE))
        ##Bottom Right
        BR = (int((pos[0]+rect[0])/TILE_SIZE), int((pos[1]+rect[1])/TILE_SIZE))

        ##CHECK TOP LEFT CORNER
        tile = self.tmxdata.get_tile_image(TL[0], TL[1], 2)
        if tile != None:
            all_colide_corners.append("TL")
        
        ##CHECK TOP RIGHT CORNER
        tile = self.tmxdata.get_tile_image(TR[0], TR[1], 2)
        if tile != None:
            all_colide_corners.append("TR")
        
        ##CHECK BOTTOM LEFT CORNER
        tile = self.tmxdata.get_tile_image(BL[0], BL[1], 2)
        if tile != None:
            all_colide_corners.append("BL")
        
        ##CHECK BOTTOM RIGHT CORNER
        tile = self.tmxdata.get_tile_image(BR[0], BR[1], 2)
        if tile != None:
            all_colide_corners.append("BR")
        
        # print(all_colide_corners)
        return all_colide_corners

          
    