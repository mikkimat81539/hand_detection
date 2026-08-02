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


	def player_movement_x(self, surface, x, d):
		if d <= 0.25:
			self.rect.x -= self.velocity_x 	

			if self.rect.x <= 1:
				self.rect.x += self.velocity_x

		elif d > 0.25:
			self.rect.x += self.velocity_x

			if self.rect.x >= surface.get_width()-self.width:
				self.rect.x -= self.velocity_x


	def player_movement_y(self, surface, y, d):
		if d <= 0.25:
			self.rect.y -= self.velocity_y 	

			if self.rect.y <= 1:
				self.rect.y += self.velocity_y

		elif d > 0.25:
			self.rect.y += self.velocity_y

			if self.rect.y >= surface.get_height()-self.height:
				self.rect.y -= self.velocity_y

