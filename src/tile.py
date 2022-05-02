from config import TILE_SIZE, COLORS
from random import randint
import pygame as pg
pg.font.init()

class Tile():
	font = pg.font.Font('freesansbold.ttf', 32)
	size = TILE_SIZE
	color = (100,100,100)
	def __init__(self, win, pos):
		self.surface = win
		self.pos = pos
		self.num = 2
		self.setRect()
		self.setLabl()
		print(self)

	def setRect(self):
		self.rect = pg.Rect((self.pos),(self.size, self.size))

	def update(self, pos):
		self.pos = pos
		self.setRect()
		self.setLabl()

	def draw(self):
		#draw rect
		pg.draw.rect(self.surface, self.color, self.rect)

		#draw num
		self.surface.blit(self.labl, self.getLablRect().topleft)

	def getLablRect(self):
		rect = self.labl.get_rect(center = self.rect.center)
		return rect

	def setLabl(self):
		self.labl = self.font.render(str(self.num), True, COLORS['black'])

	def __str__(self):
		return f'{self.pos}, {self.num}, {self.rect}'