from config import *
import pygame as pg
pg.init()
pg.display.set_caption('2048')
clock = pg.time.Clock()
window = pg.display.set_mode((S_WIDTH, S_HEIGHT))

window.fill(COLORS['white'])

def main():
    running = True

    while running:
        clock.tick(FPS)

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
    main()