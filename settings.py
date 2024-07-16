class Settings:
    """Container for application variables."""

    tile_size = 25
    wall_width = max(tile_size // 10, 1)
    maze_size = (80, 50)
    color_empty  = (255, 255, 255)
    color_seen   = (  0, 255, 255)
    color_active = (255,   0,   0)
    color_wall   = (  0,   0,   0)