import pygame as pg
pg.init()

from settings import Settings


class Tile():
    """Parent class for individual tiles."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.color = Settings.color_empty
        self.walls = pg.Surface((Settings.tile_size, Settings.tile_size), pg.SRCALPHA)
        self.shape = self.walls.copy()

    def draw(self, screen: pg.Surface):
        """Draw shape and walls on surface."""

        raise NotImplementedError("Parent class \"Tile\" does not implement \"draw().\" Consider using inheriting classes such as \"SquareTile\" or \"TriangleTile\".")
    
    def generate_walls(self, neighbors: list[int]):
        """Generates wall surface according to neighbors."""

        raise NotImplementedError("Parent class \"Tile\" does not implement \"generate_walls().\" Consider using inheriting classes such as \"SquareTile\" or \"TriangleTile\".")
    
    def generate_shape(self):
        """Generates shape image."""

        raise NotImplementedError("Parent class \"Tile\" does not implement \"generate_shape().\" Consider using inheriting classes such as \"SquareTile\" or \"TriangleTile\".")
    

class SquareTile(Tile):
    """Tile class for square tiles."""

    def __init__(self, x, y):
        super().__init__(x, y)

        self.rect = pg.Rect(x*Settings.tile_size, y*Settings.tile_size, Settings.tile_size, Settings.tile_size)

    def draw(self, screen: pg.Surface):
        """Draw square tile on screen."""

        # Draw square.
        pg.draw.rect(screen, self.color, self.rect)

        # Draw walls.
        screen.blit(self.walls, self.rect)

    def generate_walls(self, neighbors: list[int]):
        """Generate walls for a square tile based on neighbors."""

        self.walls.fill((0, 0, 0, 0))

        tile_size = self.walls.get_size()[0]
        w = Settings.wall_width
        vertex = self.y * Settings.size[0] + self.x

        # Draw corners.
        pg.draw.rect(self.walls, Settings.color_wall, pg.Rect(0, 0, w, w))                          # top left
        pg.draw.rect(self.walls, Settings.color_wall, pg.Rect(0, tile_size - w, w, w))              # bot left
        pg.draw.rect(self.walls, Settings.color_wall, pg.Rect(tile_size - w, tile_size - w, w, w))  # bot right
        pg.draw.rect(self.walls, Settings.color_wall, pg.Rect(tile_size - w, 0, w, w))              # top right

        # If vertex does not have left neighbor
        if vertex - 1 not in neighbors:
            pg.draw.rect(self.walls, Settings.color_wall, pg.Rect(0, 0, w, tile_size))

        # If vertex does not have top neighbor
        if vertex - Settings.size[0] not in neighbors:
            pg.draw.rect(self.walls, Settings.color_wall, pg.Rect(0, 0, tile_size, w))

        # If vertex does not have right neighbor
        if vertex + 1 not in neighbors:
            pg.draw.rect(self.walls, Settings.color_wall, pg.Rect(tile_size-w, 0, w, tile_size))

        # If vertex does not have bottom neighbor
        if vertex + Settings.size[0] not in neighbors:
            pg.draw.rect(self.walls, Settings.color_wall, pg.Rect(0, tile_size-w, tile_size, w))
    
    def generate_shape(self):
        """Does nothing.
        
        SquareTile utilizes pygame.draw.rect and therefore does not implement generate_shape.
        """
        pass
  

class Tiles(list):
    """Container for holding, drawing, and settings multiple tile attributes."""

    def __init__(self, size, tile_class: Tile):
        super().__init__([tile_class(x, y) for y in range(size[1]) for x in range(size[0])])
        print(self.__len__())

    def draw(self, tiles: list[int], screen: pg.Surface):
        """Draw tiles on surface."""

        for t in tiles:
            self[t].draw()

    def set_tile_color(self, tile: int, color):
        """Set tile color."""

        self[tile].color = color


    



# OLD TILES CLASS
# class Tiles():
#     """Container for holding, drawing, and settings multiple tile attributes."""
#     def __init__(self, size: tuple):
#         self.tiles = {y*size[0]+x: Tile(x, y) for x in range(size[0]) for y in range(size[1])}

#     def draw(self, screen: pg.Surface):
#         for t in self.tiles.values():
#             t.draw(screen)

#     def set_color_all(self, color):
#         for t in self.tiles.values():
#             t.color = color

#     def __getitem__(self, key):
#         return self.tiles[key]
    
#     @staticmethod
#     def set_color(color, tiles):
#         for t in tiles:
#             t.color = color
    
# OLD TILE CLASS
# class Tile():
#     """Tile class for holding draw data."""
#     def __init__(self, x, y):
#         self.color = Settings.color_empty
#         self.rect = pg.Rect(x * Settings.tile_size, y * Settings.tile_size, Settings.tile_size, Settings.tile_size)

#     def draw(self, screen: pg.Surface):
#         pg.draw.rect(screen, self.color, self.rect)