import pygame
import os
from cardType import cardType
import math

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
		self.Range = cardType.Range[self.ctype] * 51
		self.Cooldown = cardType.Cooldown[self.ctype] * 50000

		self.cd = self.Cooldown

		self.last_update_time = pygame.time.get_ticks()
		self.image = cardType.imageName[ctype]

		
	
	def pos(self, x, y):
		self.xCoord = x
		self.yCoord = y

	def animate(self, enemies, surface):
		self.cd -= pygame.time.get_ticks()-self.last_update_time
		if(self.cd < 0):
			self.cd += self.Cooldown
			for enemy in enemies:
				if(self.in_range(enemy)):
					enemy.health -= self.Damage
					pygame.draw.line(surface, FONT_COLOR, (self.xCoord, self.yCoord), enemy.getCoordinates(), 10)
					return

	def in_range(self, enemy):
		dist = math.sqrt((self.xCoord - enemy.getCoordinates()[0]) * (self.xCoord - enemy.getCoordinates()[0]) + (self.yCoord - enemy.getCoordinates()[1]) * (self.yCoord - enemy.getCoordinates()[1]))
		if(dist < self.Range):
			return True
		return False
