import pygame as pg
pg.init()

from settings import Settings
from maze import Maze
from walls import get_walls_overlay
from tiles import Tiles, Tile
from search import a_star


class App:
    """Application class for graph search visualizer."""
    def __init__(self):
        self.screen = pg.display.set_mode(tuple(map(lambda x: x * Settings.tile_size, Settings.maze_size)))
        self.clock = pg.time.Clock()

        self.maze = Maze(Settings.maze_size)
        self.wall_overlay = get_walls_overlay(self.maze, Settings.tile_size, self.screen.get_size())
        self.tiles = Tiles(Settings.maze_size)
        self.search = a_star(self.maze, 0, (self.maze.size[0]*self.maze.size[1])-1, self)

    def run(self):

        self.tiles.draw(self.screen)
        self.screen.blit(self.wall_overlay, (0, 0))
        timer = 0
        found = False

        while True:
            
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    exit(0)

            timer += self.clock.tick(60)
            if not found and timer > .25:
                if (self.search.step()): found = True

            pg.display.flip()

    def change_tile(self, vertex, color):
        tile = self.tiles[vertex]
        Tiles.set_color(color, [tile])
        tile.draw(self.screen)
        self.screen.blit(self.wall_overlay, (0, 0))


if __name__ == "__main__":

    print("\nWelcome to my Maze Graph Search Visualization Program!\n\n")

    app = App()
    app.run()