import pygame as pg
pg.init()

from settings import Settings
from maze import Maze
from walls import get_walls_overlay


class App:
    """Application class for graph search visualizer."""
    def __init__(self):
        self.screen = pg.display.set_mode(tuple(map(lambda x: x * Settings.tile_size, Settings.maze_size)))

        self.maze = Maze(Settings.maze_size)
        self.wall_overlay = get_walls_overlay(self.maze, Settings.tile_size, self.screen.get_size())

    def run(self):

        while True:
            
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    exit(0)

            self.screen.fill(Settings.color_empty)

            self.screen.blit(self.wall_overlay, (0, 0))

            pg.display.flip()


if __name__ == "__main__":

    print("\nWelcome to my Maze Graph Search Visualization Program!\n\n")

    app = App()
    app.run()