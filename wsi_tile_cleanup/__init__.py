import sys

if sys.version_info[0] < 3:
    raise Exception("Error: You are not running Python 3")

__version__ = "0.1.0"

from wsi_tile_cleanup.utils.pyvips import read_image, split_rgb

from wsi_tile_cleanup.masks.blackish import blackish_percent
from wsi_tile_cleanup.masks.pens import pen_percent
from wsi_tile_cleanup.masks.otsu import background_percent, otsu_threshold