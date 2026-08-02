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

	def player_detect(self, x, y):
		if x >= 50 or y>=50:
			self.activate = True

	def player_movement(self, x, y, width, height):
		# HORIZONTAL MOVEMENT
		if x < width * 0.3:
			self.rect.x -= self.velocity_x

		if x > width * 0.7:
			self.rect.x += self.velocity_x


		# VERTICAL MOVEMENT
		if y < height * 0.3:
			self.rect.y -= self.velocity_y

		elif y > height * 0.7:
			self.rect.y += self.velocity_y
	
