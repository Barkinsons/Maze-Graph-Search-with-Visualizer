import pygame as pg
pg.init()

from settings import Settings
from maze import SquareMaze, TriangleMaze
# from walls import get_walls_overlay
from tiles import Tiles, SquareTile, TriangleTile
from search import a_star


class App:
    """Application class for graph search visualizer."""
    def __init__(self):
        self.screen = pg.display.set_mode(tuple(map(lambda x: x * Settings.tile_size, Settings.size)), pg.SRCALPHA)
        self.clock = pg.time.Clock()

        self.maze = SquareMaze(Settings.size)
        self.tiles = Tiles(Settings.size, SquareTile)
        # self.maze_screen = pg.Surface(self.screen.get_size(), pg.SRCALPHA)

        # self.maze = TriangleMaze(Settings.size)
        # self.tiles = Tiles(Settings.size, TriangleTile)
        # self.maze_screen = pg.Surface((Settings.tile_size * (Settings.size[0]+1) // 2, Settings.tile_size * Settings.size[1]), pg.SRCALPHA)

        self.search = a_star(self.maze, 0, Settings.size[0] * Settings.size[1] - 1)

    def run(self):

        timer = 0
        gen = False
        found = False

        while True:
            
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    exit(0)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        pass

            timer += self.clock.tick() / 1000

            if not gen:
                r = None
                while not r:
                    r = self.maze.step()
                if r == True:
                    gen = True
                    pg.image.save(self.screen, "img.png")
                    break
                elif r:
                    for v in r:
                        self.tiles[v].generate_walls(self.maze[v])
                        self.tiles[v].generate_shape()
                        self.tiles[v].draw(self.screen)

            elif not found and timer > 0.01:
                timer = 0

                r, vertices = self.search.step()

                # If found.
                if r:
                    found = True

                for v in vertices:
                    self.tiles[v].color = Settings.color_seen
                    self.tiles[v].generate_shape()
                    self.tiles[v].draw(self.screen)

            # self.screen.fill((0, 0, 0, 0))

            # self.screen.blit(self.screen, ((self.screen.get_size()[0] - self.maze_screen.get_size()[0]) // 2, 0))
            pg.display.flip()



if __name__ == "__main__":

    print("\nWelcome to my Maze Graph Search Visualization Program!\n\n")

    app = App()
    app.run()