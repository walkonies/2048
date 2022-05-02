from config import *
import pygame as pg
from tile import Tile
from board import Board

icon = pg.image.load('images/icon.png')
clock = pg.time.Clock()
window = pg.display.set_mode((S_WIDTH, S_HEIGHT))
board = Board(window)
def main():
    running = True
    while running:
        clock.tick(FPS)
        window.fill(COLORS['white'])
        board.draw()
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pg.mouse.get_pos()
            if event.type == pg.KEYDOWN:
                    key = event.key
                    # handle key events
            if event.type == pg.QUIT:
                running = False
        pg.display.update()

if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('2048')
    pg.display.set_icon(icon)
    main()