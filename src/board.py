import pygame as pg
from config import NUM_ROWS, NUM_COLS, TILE_GAP, BOARD_PAD
from tile import Tile


class Board():
	NUM_ROWS = NUM_ROWS
	NUM_COLS = NUM_COLS
	GAP = TILE_GAP
	PAD = BOARD_PAD
	def __init__(self, win):
		self.surface = win
		self.board = self.newBoard()
		self.board[0][0] = Tile(win, self.getPos(0,0))
		self.board[0][3] = Tile(win, self.getPos(0,3))


	def newBoard(self):
		return [[0 for _ in range(self.NUM_ROWS)] for _ in range(self.NUM_COLS)]

	def getPos(self, row, col):
		print(Tile.size)
		x = self.PAD + (col * Tile.size) + (col * self.GAP)
		y = 150
		return (x,y)


	def draw(self):
		for row in self.board:
			for tile in row:
				if tile:
					tile.draw()