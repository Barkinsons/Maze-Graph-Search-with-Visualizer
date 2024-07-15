import pygame as pg
pg.init()

from settings import Settings
from maze import Maze


def get_walls_overlay(maze: Maze, tile_size: int, screen_size: tuple):
    """Generates and returns surface for maze walls overlay."""

    width, height = maze.size
    overlay = pg.Surface(screen_size, pg.SRCALPHA)
    working_tile = pg.Surface((tile_size, tile_size), pg.SRCALPHA)
    for x in range(width):
        for y in range(height):
            paint_tile_overlay(working_tile, y * Settings.maze_size[0] + x, maze)
            overlay.blit(working_tile, pg.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
            working_tile.fill((0, 0, 0, 0))

    return overlay


def paint_tile_overlay(working_tile: pg.Surface, vertex: int, maze: Maze):
    """Paints appropriate tile overlay onto surface."""

    tile_size = working_tile.get_size()[0]
    _w = Settings.wall_width

    # Draw corners.
    pg.draw.rect(working_tile, Settings.color_wall, pg.Rect(0, 0, _w, _w))                            # top left
    pg.draw.rect(working_tile, Settings.color_wall, pg.Rect(0, tile_size - _w, _w, _w))               # bot left
    pg.draw.rect(working_tile, Settings.color_wall, pg.Rect(tile_size - _w, tile_size - _w, _w, _w))  # bot right
    pg.draw.rect(working_tile, Settings.color_wall, pg.Rect(tile_size - _w, 0, _w, _w))               # top right

    _n = maze[vertex]

    # If vertex does not have left neighbor
    if vertex - 1 not in _n:
        pg.draw.rect(working_tile, Settings.color_wall, pg.Rect(0, 0, _w, tile_size))

    # If vertex does not have top neighbor
    if vertex - Settings.maze_size[0] not in _n:
        pg.draw.rect(working_tile, Settings.color_wall, pg.Rect(0, 0, tile_size, _w))

    # If vertex does not have right neighbor
    if vertex + 1 not in _n:
        pg.draw.rect(working_tile, Settings.color_wall, pg.Rect(tile_size-_w, 0, _w, tile_size))

    # If vertex does not have bottom neighbor
    if vertex + Settings.maze_size[1] not in _n:
        pg.draw.rect(working_tile, Settings.color_wall, pg.Rect(0, tile_size-_w, tile_size, _w))
    