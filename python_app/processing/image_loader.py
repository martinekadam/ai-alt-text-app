import os

from processing.config import ALLOWED_EXTENSIONS

def image_loader(input_dir: str) -> list[str]:
    """
    Retrieve image file paths from a directory, filtering by allowed extensions.

    Parameters
    ----------
    input_dir : str
        Path to the directory containing images.

    Returns
    -------
    list
        List of file paths to images that match the allowed extensions.
    """
    if not os.path.isdir(input_dir):
        raise ValueError(f"Input directory does not exist: {input_dir}")
    
    image_paths = [
        os.path.join(root, file)
        for root, _, files in os.walk(input_dir)
        for file in files if file.lower().endswith(ALLOWED_EXTENSIONS)
    ]

    image_paths.sort()

    return image_paths