import pyvips as vips


def read_image(image_path, discard_alpha=True, **kwargs):
    vips_image = vips.Image.new_from_file(f"{image_path}", **kwargs)
    
    if discard_alpha:
        # n=3 discards alpha channel, keeping only r,g,b
        vips_image = vips_image.extract_band(0, n=3)
    
    return vips_image


def split_rgb(vips_image):
    bands = vips_image.bandsplit()
    return bands
