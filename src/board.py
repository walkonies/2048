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
		self.board[self.getIndex(0,0)] = (Tile(self.surface,self.getPos(0,0), 0, 0, self.TILE_SIZE))
		self.board[self.getIndex(3,3)] = (Tile(self.surface,self.getPos(3,3), 3, 3, self.TILE_SIZE))
		self.board[self.getIndex(2,3)] =(Tile(self.surface,self.getPos(2,3), 2, 3, self.TILE_SIZE))
		self.board[self.getIndex(1,2)] =(Tile(self.surface,self.getPos(1,2), 1, 2, self.TILE_SIZE))
		self.pb()


	def move(self, dir):
		print('move')
		board = self.board.copy()
		for tile in self.board:
			if tile:
				old_row, old_col = tile.row, tile.col
				row, col = tile.row, tile.col
				if dir == 'down':
					row -= 1
				if dir == 'left':
					col -= 1
				if dir == 'right':
					col += 1
				if dir == 'up':
					row -= 1
				move = not self.checkCollide(board, row, col)
				while move:
					board = self.moveTile(board, tile, row, col)
					move = not self.checkCollide(board, row, col)

		self.update(board)

	def moveTile(self, board, tile, row, col):
		old_row, old_col = tile.row, tile.col
		index = self.getIndex(row, col)
		pos = self.getPos(row, col)
		board[index] = tile
		tile.update(pos, row, col)

		board[self.getIndex(old_row, old_col)] = 0

		return board


	def checkCollide(self, board, row, col):
		if row >= self.NUM_ROWS or row < 0 or col >= self.NUM_COLS or col < 0:
			print('collide wall')
			return True
		if board[self.getIndex(row, col)]:
			print('collide Tile')
			return True
		print('move')
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

	def update(self, board):
		self.board = board
		self.pb()

	def getIndex(self, row, col):
		return (row*NUM_COLS) + col


	def draw(self):
		for tile in self.board:
			if tile:
				tile.draw()
		self.drawGrid()

	def pb(self):
		print('\n\n')
		for i, elem in enumerate(self.board):
			if i > 0 and not i%(NUM_COLS):
				print()
			if elem:
				print('x', end ='')
			else:
				print('_', end ='')
		print()
		
					