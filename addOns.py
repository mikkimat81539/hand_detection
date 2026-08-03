import pygame

pygame.init()

class setupFont:
	def __init__(self, x_pos, y_pos, text):
		self.text = text
		self.x_pos = x_pos
		self.y_pos = y_pos

	def displayFont(self, surface):
		createFont = pygame.font.SysFont("Arial", 30)
		renderFont = createFont.render(self.text, False, "red")
		surface.blit(renderFont, (self.x_pos, self.y_pos))
