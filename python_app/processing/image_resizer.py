from PIL import Image
from typing import Tuple

from processing.config import DEFAULT_IMAGE_SIZE

def resize_image(image: Image.Image, size: Tuple[int, int] = DEFAULT_IMAGE_SIZE) -> Image.Image:
    """
    Resize an image to the specified dimensions.

    Parameters
    ----------
    image : PIL.Image.Image
        Image object to be resized.
    size : tuple of int, optional
        Target dimensions (width, height) in pixels. Default is (512, 512).

    Returns
    -------
    PIL.Image.Image
        Resized image.
    """
    if not (isinstance(size, tuple) and len(size) == 2 and all(isinstance(dim, int) for dim in size)):
        raise ValueError("Size must be a tuple of two integers (width, height).")

    return image.resize(size)