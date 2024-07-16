import pygame as pg
pg.init()

from settings import Settings


class Tiles():
    """Container for holding, drawing, and settings multiple tile attributes."""
    def __init__(self, size: tuple):
        self.tiles = {y*size[0]+x: Tile(x, y) for x in range(size[0]) for y in range(size[1])}

    def draw(self, screen: pg.Surface):
        for t in self.tiles.values():
            t.draw(screen)

    def set_color_all(self, color):
        for t in self.tiles.values():
            t.color = color

    def __getitem__(self, key):
        return self.tiles[key]
    
    @staticmethod
    def set_color(color, tiles):
        for t in tiles:
            t.color = color
    
class Tile():
    """Tile class for holding draw data."""
    def __init__(self, x, y):
        self.color = Settings.color_empty
        self.rect = pg.Rect(x * Settings.tile_size, y * Settings.tile_size, Settings.tile_size, Settings.tile_size)

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.color, self.rect)