import pygame

pygame.init()

class Player:
	def __init__(self, x_pos, y_pos, width, height, color):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.height = height
		self.color = color
		self.surface = pygame.Surface((self.width, self.height))
		self.rect = self.surface.get_rect(topleft=(self.x_pos, self.y_pos))

		self.surface.fill(self.color)

		# self.rect = pygame.Rect((self.x_pos, self.y_pos), (self.width, self.height))

		self.image = pygame.transform.scale(pygame.image.load("assets/cigarette.png"), (self.width, self.height))

		self.velocity_x = 1
		self.velocity_y = 1


	def draw_player(self, surface):
		surface.blit(self.surface, (self.rect))
		self.surface.blit(self.image, (0, 0))

		# pygame.draw.rect(surface, self.color, self.rect)	

	# FOR LEFT HAND
	def player_movement_x(self, surface, d):
		if d <= 0.25:
			self.rect.x -= self.velocity_x 	

			if self.rect.x <= 1:
				self.rect.x += self.velocity_x

		elif d > 0.25:
			self.rect.x += self.velocity_x

			if self.rect.x >= surface.get_width()-self.width:
				self.rect.x -= self.velocity_x


	# FOR RIGHT HAND
	def player_movement_y(self, surface, d):
		if d <= 0.25:
			self.rect.y -= self.velocity_y 	

			if self.rect.y <= 1:
				self.rect.y += self.velocity_y

		elif d > 0.25:
			self.rect.y += self.velocity_y

			if self.rect.y >= surface.get_height()-self.height:
				self.rect.y -= self.velocity_y

	def camera_collision(self, camera):
		if self.rect.colliderect(camera.get_rect()):
			self.rect.x -= self.velocity_x

