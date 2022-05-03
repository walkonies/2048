from config import COLORS, NUM_FONT, NUM_FONT_SIZE
from random import randint
import pygame as pg
pg.font.init()

class Tile():
	font = pg.font.Font(NUM_FONT, NUM_FONT_SIZE)
	
	color = (COLORS['tile'])
	def __init__(self, win, pos, row, col, size):
		self.surface = win
		self.pos = pos
		self.size = size
		self.row = row
		self.col = col
		self.num = 2
		self.setRect()
		self.setLabl()

	def setRect(self):
		self.rect = pg.Rect((self.pos),(self.size, self.size))

	def update(self, pos, row, col):
		self.pos = pos
		self.row = row
		self.col = col
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