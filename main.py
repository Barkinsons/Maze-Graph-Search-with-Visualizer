import pygame as pg
pg.init()

from settings import Settings
from maze import SquareMaze
# from walls import get_walls_overlay
from tiles import Tiles, SquareTile
from search import a_star


class App:
    """Application class for graph search visualizer."""
    def __init__(self):
        self.screen = pg.display.set_mode(tuple(map(lambda x: x * Settings.tile_size, Settings.size)))
        self.clock = pg.time.Clock()

        self.maze = SquareMaze(Settings.size)
        self.tiles = Tiles(Settings.size, SquareTile)
        self.search = a_star(self.maze, 0, Settings.size[0] * Settings.size[1] - 1)

    def run(self):

        timer = 0
        gen = False
        found = False

        self.screen.fill((Settings.color_wall))

        while True:
            
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    exit(0)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        pass


            timer += self.clock.tick(400) / 1000

            if not gen:
                r = None
                while not r:
                    r = self.maze.step()
                if r == True:
                    gen = True
                elif r:
                    for v in r:
                        self.tiles[v].generate_walls(self.maze[v])
                        self.tiles[v].draw(self.screen)

            elif not found and timer > 0.05:
                timer = 0

                r, vertices = self.search.step()

                # If found.
                if r:
                    found = True

                for v in vertices:
                    self.tiles[v].color = Settings.color_seen
                    self.tiles[v].draw(self.screen)

            pg.display.flip()



if __name__ == "__main__":

    print("\nWelcome to my Maze Graph Search Visualization Program!\n\n")

    app = App()
    app.run()