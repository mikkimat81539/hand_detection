import pygame

pygame.init()

# OBJECT CLASS

class Object:
	def __init__(self, x_pos, y_pos, width, height, color):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.height = height
		self.color = color
		self.rect = pygame.Rect((self.x_pos, self.y_pos), (self.width, self.height))

		self.velocity = 5

	def draw_object(self, surface):
		pygame.draw.rect(surface, self.color, self.rect)

	def move_object(self):
		self.rect.x += self.velocity


