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

	def draw_player(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)	
	
	def player_movement(self, x, y):
		if x >= 50 or y>=50:
			self.activate = True
