import sys

if sys.version_info[0] < 3:
    raise Exception("Error: You are not running Python 3")

__version__ = "0.1.0"

import wsi_tile_cleanup.utils
import wsi_tile_cleanup.filters
