import pyvips as vips


def read_image(image_path):
    vips_image = vips.Image.new_from_file(f"{image_path}")
    # n=3 discards alpha channel, keeping only r,g,b
    return vips_image.extract_band(0, n=3)


def split_rgb(vips_image):
    bands = vips_image.bandsplit()
    return bands
