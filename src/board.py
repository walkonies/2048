import pygame as pg
from config import NUM_ROWS, NUM_COLS, BOARD_PAD, COLORS, S_WIDTH
from tile import Tile


class Board():
	NUM_ROWS = NUM_ROWS
	NUM_COLS = NUM_COLS
	PAD = BOARD_PAD
	tile_size = (S_WIDTH - PAD * 2)//NUM_ROWS

	def __init__(self, win):
		self.surface = win
		self.board = self.newBoard()
		self.populateBoard()
		

	def populateBoard(self):
		for i in range(NUM_ROWS):
			for j in range(NUM_COLS):
				self.board[i][j] = Tile(self.surface, self.getPos(i,j), self.tile_size)

	def newBoard(self):
		return [[0 for _ in range(self.NUM_ROWS)] for _ in range(self.NUM_COLS)]

	def getPos(self, row, col):
		x = self.PAD + (col * self.tile_size) 
		y = 100 + (row * self.tile_size) 
		return (x,y)

	def drawGrid(self):
		startX = self.PAD
		startY = 100
		for i in range(NUM_ROWS):
			for j in range(NUM_COLS):
				rect = pg.Rect((startX+ j*self.tile_size, startY+ i*self.tile_size), (self.tile_size, self.tile_size))
				pg.draw.rect(self.surface, COLORS['black'], rect, 2)


	def draw(self):
		for i, row in enumerate(self.board):
			for j, tile in enumerate(row):
				if tile:
					tile.draw()
		self.drawGrid()
		
					