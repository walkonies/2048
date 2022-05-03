import pygame as pg
from config import NUM_ROWS, NUM_COLS, BOARD_PAD, COLORS, S_WIDTH
from tile import Tile


class Board():
	NUM_ROWS = NUM_ROWS
	NUM_COLS = NUM_COLS
	PAD = BOARD_PAD
	TILE_SIZE = (S_WIDTH - PAD * 2)//NUM_ROWS

	def __init__(self, win):
		self.surface = win
		self.board = self.newBoard()
		self.board.append(Tile(self.surface,self.getPos(0,0), 0, 0, self.TILE_SIZE))
		self.board.append(Tile(self.surface,self.getPos(3,3), 3, 3, self.TILE_SIZE))
		self.board.append(Tile(self.surface,self.getPos(3,2), 3, 2, self.TILE_SIZE))


	def move(self, dir):
		board = self.board
		if dir == 'down':
			for tile in self.board:
				if tile:
					if not self.checkCollide(tile.row+1, tile.col):
						pos = self.getPos(tile.row+1, tile.col)
						tile.update(pos, tile.row+1, tile.col)

	def checkCollide(self, row, col):
		if row >= self.NUM_ROWS or row < 0 or col >= self.NUM_COLS or col < 0:
			return True
		if self.board[(row*NUM_COLS) + col]:
			return True

		return False
		
	def newBoard(self):
		return [0 for _ in range(self.NUM_ROWS * self.NUM_COLS)]

	def getPos(self, row, col):
		x = self.PAD + (col * self.TILE_SIZE) 
		y = 100 + (row * self.TILE_SIZE) 
		return (x,y)

	def drawGrid(self):
		startX = self.PAD
		startY = 100
		for i in range(NUM_ROWS):
			for j in range(NUM_COLS):
				rect = pg.Rect((startX+ j*self.TILE_SIZE, startY+ i*self.TILE_SIZE), (self.TILE_SIZE, self.TILE_SIZE))
				pg.draw.rect(self.surface, COLORS['black'], rect, 2)

	def draw(self):
		for tile in self.board:
			if tile:
				tile.draw()
		self.drawGrid()
		
					