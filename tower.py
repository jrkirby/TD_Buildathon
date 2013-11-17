import pygame
import os
from cardType import cardType

FONT_SIZE = 10
FONT_PADDING = 10
FONT_COLOR = (0,0,0)
FONT_BACKGROUND =(255,255,255)
FONT_LINESPACE = 4

class tower:
	
	xCoord, yCoord = 0, 0
	projectile = None

	def __init__(self, ctype):
		self.ctype = ctype
		self.Damage = cardType.Damage[self.ctype]
		self.Range = cardType.Range[self.ctype]
		self.Cooldown = cardType.Cooldown[self.ctype]

		self.cd = self.Cooldown

		self.last_update_time = pygame.time.get_ticks()
		self.image = cardType.imageName[ctype]

		
	
	def pos(self, x, y):
		self.xCoord = x
		self.yCoord = y

	def animate(self, enemies):
		# self.cd -= pygame.time.get_ticks()-self.last_update_time
		x = 0
