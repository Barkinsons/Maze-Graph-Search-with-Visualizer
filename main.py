import pygame as pg
pg.init()

class App:
    """Application class for graph search visualizer."""
    def __init__(self):
        self.screen = pg.display.set_mode(tuple(map(lambda x: x * Settings.tile_size, Settings.maze_size)))

    def run(self):

        while True:
            
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    exit(0)

            self.screen.fill(Settings.color_active)

            pg.display.flip()


class Settings:
    """Container for application variables."""

    tile_size = 20
    maze_size = (40, 22)
    color_empty  = (255, 255, 255)
    color_seen   = (  0, 255, 255)
    color_active = (255,   0,   0)
    color_wall   = (  0,   0,   0)


if __name__ == "__main__":

    print("\nWelcome to my Maze Graph Search Visualization Program!\n\n")

    app = App()
    app.run()