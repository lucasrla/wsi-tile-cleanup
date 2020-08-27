import wsi_tile_cleanup as cleanup

# pen marks and black artifacts

tile_path = "examples/images/tiles/3.jpeg"
print(tile_path)
vi_tile = cleanup.read_image(tile_path)

bands = cleanup.split_rgb(vi_tile)

colors = ["red", "green", "blue"]

for color in colors:
    perc = cleanup.pen_percent(bands, color)
    print(f"{color}: {perc*100:.3f}%")

perc = cleanup.blackish_percent(bands)
print(f"blackish: {perc*100:.3f}%")


# background (via otsu)

wsi_path = "examples/images/wsi/TCGA-A1-A0SB-01Z-00-DX1.B34C267B-CAAA-4AB6-AD5C-276C26F997A1.svs-level=2.jpg"
print(wsi_path)
vi_wsi = cleanup.read_image(wsi_path)

otsu = cleanup.otsu_threshold(vi_wsi)
print(f"otsu_threshold: {otsu}")

tile_bg = "examples/images/tiles/20_15.png"
print(tile_bg)
vi_bg = cleanup.read_image(tile_bg)

perc = cleanup.background_percent(vi_bg, otsu)
print(f"background: {perc*100:.3f}%")