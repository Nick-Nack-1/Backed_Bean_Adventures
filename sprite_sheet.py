import pygame

class read_out():
	def __init__(self, file_name):
		self.main_sheet = pygame.image.load(file_name).convert_alpha()
	
	
	def Get_img(self,rectangle):
		# rectangle = [(img_top_left_pos),(img_size_x,img_size_y)]
		rect = pygame.Rect(rectangle)
		image = pygame.Surface(rect.size)
		image.blit(self.main_sheet, (0,0), rect)
		image.set_colorkey((0,0,0))
		return image
	


class animate():
	def __init__(self,scr):
		# super(animate, self).__init__()
		self.counter = 0
		self.screen = scr
		self.frame_num = 0
		self.sheet = None


	def Set_sheet(self, S_sheet):
		self.sheet = pygame.image.load(S_sheet).convert_alpha
#		self.counter = 0
#		self.frame_num = 0


	def Play(self,pos):
		pass
