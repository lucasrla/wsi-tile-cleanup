import pyvips as vips
import numpy as np


def bw_histogram(vi):
    vi_bw = vi.colourspace("b-w")
    vi_hist = vi_bw.hist_find()

    np_hist = np.ndarray(
        buffer=vi_hist.write_to_memory(),
        dtype=np.uint32,
        shape=[
            256,
        ],
    )

    np_hist = np_hist.astype(float)
    return np_hist


def background_percent(vi_tile, otsu_threshold):
    np_tile_hist = bw_histogram(vi_tile)
    tissue_perc = np.sum(np_tile_hist[:otsu_threshold]) / np.sum(np_tile_hist)
    # tissue_perc = np.round(tissue_perc, decimals=5) if tissue_perc > 0 else 0
    return 1.0 - tissue_perc


def otsu_threshold(vi_wsi):
    # heavily inspired by scikit-image otsu implementation
    # https://github.com/scikit-image/scikit-image/blob/master/skimage/filters/thresholding.py#L237

    np_hist = bw_histogram(vi_wsi)

    bins = np.arange(256)

    # class probabilities for all possible thresholds
    w1 = np.cumsum(np_hist)
    w2 = np.cumsum(np_hist[::-1])[::-1]

    # class means for all possible thresholds
    # https://stackoverflow.com/questions/26248654/how-to-return-0-with-divide-by-zero
    a1 = np.cumsum(np_hist * bins)
    mean1 = np.divide(a1, w1, out=np.zeros_like(a1), where=w1 != 0)

    a2 = np.cumsum((np_hist * bins)[::-1])
    mean2 = np.divide(a2, w2[::-1], out=np.zeros_like(a2), where=w2 != 0)[::-1]

    # Clip ends to align class 1 and class 2 variables:
    # The last value of ``weight1``/``mean1`` should pair with zero values in
    # ``weight2``/``mean2``, which do not exist.
    variance12 = w1[:-1] * w2[1:] * (mean1[:-1] - mean2[1:]) ** 2
    # print(variance12)

    idx = np.argmax(variance12)
    otsu_threshold = bins[:-1][idx]

    return otsu_threshold
