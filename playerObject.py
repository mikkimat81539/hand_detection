import pygame

pygame.init()

class Player:
	def __init__(self, x_pos, y_pos, width, height, color):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.height = height
		self.color = color
		self.rect = pygame.Rect((self.x_pos, self.y_pos), (self.width, self.height))

		self.activate = False

		self.velocity_x = 3
		self.velocity_y = 2


	def draw_player(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)	


	def player_movement(self, surface, x, y):
		# print(x, y)

		if self.rect.x > 0.4:
			self.rect.x -= self.velocity_x 	


	def reset_player(self):
		self.rect.x = 400
		self.rect.y = 230	
#		self.velocity_x = 0
#		self.velocity_y = 0

