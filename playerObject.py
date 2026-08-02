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

		self.velocity_x = 1
		self.velocity_y = 2


	def draw_player(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)	


	def player_movement(self, surface, x, y, d):
		# print(x, y)

		if d <= 0.25:
			self.rect.x -= self.velocity_x 	

			if self.rect.x <= 1:
				self.rect.x += self.velocity_x

		elif d > 0.25:
			self.rect.x += self.velocity_x

			if self.rect.x >= surface.get_width()-self.width:
				self.rect.x -= self.velocity_x

