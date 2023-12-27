import pytmx
from Globals import *


class map():
    def __init__(self, map_nom, scn):
        self.screen = scn
        self.all_maps = ["./Maps/Test.tmx", "./Maps/Test1.tmx", "./Maps/Test2.tmx", "./Maps/Debug_map.tmx"]
        self.tmxdata = pytmx.load_pygame(self.all_maps[map_nom]) #map_nom is for which map to play
        #This is the pixel offset between the map origen(top-left) and the screen origen(0,0)
        self.offset_x = 0
        self.offset_y = 0
        self.back_tint = self.tmxdata.get_layer_by_name("Background").tintcolor

        ##ANIMATION INDEX
        self.fire_index = 0
        self.key_index = 0 
        self.diamond_index = 0
        self.cion_index = 0 
        self.counter = 0 #Frame counter

        ##INTERACT INEMATIONS
        self.door_types = ["Red_door", "Green_door", "Blue_door"]
        self.lever_types = ["Red_lever", "Green_lever", "Blue_lever"]

    

    def draw(self):
        for y in range (20):
            for x in range (30):
                tile_x = x+self.offset_x//TILE_SIZE
                tile_y = y+self.offset_y//TILE_SIZE
                ##BACKGROUND
                tile_image = self.tmxdata.get_tile_image(tile_x,
                                                         tile_y,
                                                         BACKGROUND)
                if tile_image != None:
                    ##If the Background tint clour isn't black then it gets a gray tint
                    ##If you dont want a tint clour make the tint colour Black(#000000)
                    if self.back_tint != "#000000":
                        tile_image.set_alpha(100)
                    self.screen.blit(tile_image, 
                                     (x*TILE_SIZE-(self.offset_x%TILE_SIZE), 
                                      y*TILE_SIZE-(self.offset_y%TILE_SIZE)))
                    tile_image.set_alpha(255)
                
                ##MID GROUND
                tile_image = self.tmxdata.get_tile_image(tile_x,
                                                         tile_y,
                                                         MIDGROUND)
                if tile_image != None:
                    self.screen.blit(tile_image, 
                                     (x*TILE_SIZE-(self.offset_x%TILE_SIZE), 
                                      y*TILE_SIZE-(self.offset_y%TILE_SIZE)))

                ##DANGER TILES           
                tile_image = self.tmxdata.get_tile_image(tile_x,
                                                         tile_y,
                                                         DANGER)
                if tile_image != None:
                    self.screen.blit(tile_image, 
                                     (x*TILE_SIZE-(self.offset_x%TILE_SIZE), 
                                      y*TILE_SIZE-(self.offset_y%TILE_SIZE)))

                ##PLATEFORMS            
                tile_image = self.tmxdata.get_tile_image(tile_x,
                                                         tile_y,
                                                         PLAYGROUND)
                if tile_image != None:
                    self.screen.blit(tile_image, 
                                     (x*TILE_SIZE-(self.offset_x%TILE_SIZE), 
                                      y*TILE_SIZE-(self.offset_y%TILE_SIZE)))
                
                ##ANIMATED TILES
                tile_proprerties = self.tmxdata.get_tile_properties(tile_x,
                                                                    tile_y,
                                                                    ANIMATION_LAYER)
                #Flames
                if tile_proprerties != None:
                    if tile_proprerties["type"] == "fire":
                        if self.counter % tile_proprerties["frames"][self.fire_index].duration == 0:
                            self.fire_index = (self.fire_index+1)%len(tile_proprerties["frames"])
                        tile_image = self.tmxdata.get_tile_image_by_gid(tile_proprerties["frames"][self.fire_index].gid)
                
                        self.screen.blit(tile_image,
                                                (x*TILE_SIZE-(self.offset_x%TILE_SIZE), 
                                                y*TILE_SIZE-(self.offset_y%TILE_SIZE)))
                        
                ##INTERACTIBLE ANIMATIONS - stuff like doors and levers
                #Doors
                tile_proprerties = self.tmxdata.get_tile_properties(tile_x,
                                                                    tile_y,
                                                                    PLAYGROUND)
                for d in self.door_types:
                    if tile_proprerties != None:
                        if "type" in tile_proprerties:
                            if tile_proprerties["type"] == d:
                                if tile_proprerties["Open"]:
                                    interact_image = self.tmxdata.get_tile_image_by_gid(tile_proprerties["frames"][1].gid)
                                else:
                                    interact_image = self.tmxdata.get_tile_image_by_gid(tile_proprerties["frames"][0].gid)
                                if interact_image != None:
                                    self.screen.blit(interact_image,
                                                    (x*TILE_SIZE-(self.offset_x%TILE_SIZE), 
                                                    y*TILE_SIZE-(self.offset_y%TILE_SIZE)))
                
                # #Levers
                # tile_proprerties = self.tmxdata.get_tile_properties(tile_x,
                #                                                     tile_y,
                #                                                     INTERACTABLES)
                # for l in self.lever_types:
                #     if tile_proprerties != None:
                #         if "type" in tile_proprerties:
                #             if tile_proprerties["type"] == l:
                #                 if tile_proprerties["On"]:
                #                     interact_image = self.tmxdata.get_tile_image_by_gid(tile_proprerties["frames"][1].gid)
                #                 else:
                #                     interact_image = self.tmxdata.get_tile_image_by_gid(tile_proprerties["frames"][0].gid)
                #                 if interact_image != None:
                #                     self.screen.blit(interact_image,
                #                                     (x*TILE_SIZE-(self.offset_x%TILE_SIZE), 
                #                                     y*TILE_SIZE-(self.offset_y%TILE_SIZE)))
                                
        self.counter += 1
               

    def Calculate_screen_pos(self, sprite_pos):
        ##Turns the map pos that is inserted to screen pos 
        return (sprite_pos[0]-self.offset_x, sprite_pos[1]-self.offset_y)
    
    

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
        tile = self.tmxdata.get_tile_image(TL[0], TL[1], PLAYGROUND)
        tile_prop = self.tmxdata.get_tile_properties(TL[0], TL[1], PLAYGROUND) #tile_prop = tile properties
        if tile != None:
            if tile_prop == None or not "Open" in tile_prop or not tile_prop["Open"]: #if the tile doesnt have the open propertie or the propertie is not true
                all_colide_corners.append("TL")

        ##CHECK TOP RIGHT CORNER
        tile = self.tmxdata.get_tile_image(TR[0], TR[1], PLAYGROUND)
        tile_prop = self.tmxdata.get_tile_properties(TR[0], TR[1], PLAYGROUND) #tile_prop = tile properties
        if tile != None:
            if tile_prop == None or not "Open" in tile_prop or not tile_prop["Open"]: #if the tile doesnt have the open propertie or the propertie is not true
                all_colide_corners.append("TR")
        
        ##CHECK BOTTOM LEFT CORNER
        tile = self.tmxdata.get_tile_image(BL[0], BL[1], PLAYGROUND)
        tile_prop = self.tmxdata.get_tile_properties(BL[0], BL[1], PLAYGROUND) #tile_prop = tile properties
        if tile != None:
            if tile_prop == None or not "Open" in tile_prop or not tile_prop["Open"]: #if the tile doesnt have the open propertie or the propertie is not true
                all_colide_corners.append("BL")

        ##CHECK BOTTOM RIGHT CORNER
        tile = self.tmxdata.get_tile_image(BR[0], BR[1], PLAYGROUND)
        tile_prop = self.tmxdata.get_tile_properties(BR[0], BR[1], PLAYGROUND) #tile_prop = tile properties
        if tile != None:
            if tile_prop == None or not "Open" in tile_prop or not tile_prop["Open"]: #if the tile doesnt have the open propertie or the propertie is not true
                all_colide_corners.append("BR")
        
        return all_colide_corners


    def Test_tile(self, map_layer, pos, rect):
        ##It will return the tile data of the tiles with which BL and BR collided
        ##pos = (x,y)
        ##rect = (width, height)
        collide_tiles = []
        ##Top Left
        TL = (int(pos[0]/TILE_SIZE), int((pos[1]+2)/TILE_SIZE)) #The +2 is just that it is a bit lower than 16
        ##Top Right
        TR = (int((pos[0]+rect[0])/TILE_SIZE), int((pos[1]+2)/TILE_SIZE))
        ##Bottom Left
        BL = (int(pos[0]/TILE_SIZE), int((pos[1]+rect[1]/2)/TILE_SIZE))
        ##Bottom Right
        BR = (int((pos[0]+rect[0])/TILE_SIZE), int((pos[1]+rect[1]/2)/TILE_SIZE))

        tile = self.tmxdata.get_tile_properties(BL[0], BL[1], map_layer)
        if tile != None:
            collide_tiles.append(tile)

        tile = self.tmxdata.get_tile_properties(BR[0], BR[1], map_layer)
        if tile != None:
            collide_tiles.append(tile)

        tile = self.tmxdata.get_tile_properties(TL[0], TL[1], map_layer)
        if tile != None:
            collide_tiles.append(tile)

        tile = self.tmxdata.get_tile_properties(TR[0], TR[1], map_layer)
        if tile != None:
            collide_tiles.append(tile)

        return collide_tiles
    

    def tile_interact(self,pos):
        ##pos == map_pos
        tile = self.tmxdata.get_tile_properties(pos[0], pos[1], INTERACTABLES)
        if tile != None:
            if "Can_Interact" in tile:
                if tile["Can_Interact"]:
                    if tile["type"] == "Red_lever":
                        tile["On"] = not tile["On"]
                        self.Change_tile_type_property("Red_door", "Open", tile["On"], PLAYGROUND)
                    elif tile["type"] == "Green_lever":
                        tile["On"] = not tile["On"]
                        self.Change_tile_type_property("Green_door", "Open", tile["On"], PLAYGROUND)
                    elif tile["type"] == "Blue_lever":
                        tile["On"] = not tile["On"]
                        self.Change_tile_type_property("Blue_door", "Open", tile["On"], PLAYGROUND)
    

    def Change_tile_type_property(self, type, property, change_to, layer): ##(str, str, any, int)
        ##This will search the intire map for tiles whit the same types on the given layer and
        ##chance the given property of those tiles to the given values
        for y in range(self.tmxdata.height):
            for x in range(self.tmxdata.width):
                tile = self.tmxdata.get_tile_properties(x, y, layer)
                if tile != None:
                    if "type" in tile:
                        if tile["type"] == type:
                            if property in tile:
                                tile[property] = change_to
