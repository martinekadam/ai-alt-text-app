import tempfile
import os
from PIL import Image

from processing.image_loader import image_loader
from processing.convert_to_jpeg import convert_to_jpeg
from processing.image_resizer import resize_image
from processing.encode_image import encode_image
from processing.filename_cleaner import clean_filename

def processing_pipeline(input_dir: str) -> dict[str, str]:
    """
    Process all images in a directory by converting to JPEG, resizing,
    and encoding in Base64.

    Parameters
    ----------
    input_dir : str
        Path to the directory containing images.

    Returns
    -------
    dict
        Dictionary where keys are original image paths and values are Base64-encoded
        image strings.
    """
    images_base64 = {}

    # Create a temporary directory for JPEG conversion
    with tempfile.TemporaryDirectory(prefix="jpeg_conversion_") as temp_dir:
        for path in image_loader(input_dir):
            try:
            # Convert to JPEG first
                jpeg_path = convert_to_jpeg(path, temp_dir)
                
                # Open, resize, and encode the image
                with Image.open(jpeg_path) as img:
                    img = resize_image(img)

                    # Use cleaned filename as key
                    file_name = os.path.basename(path)
                    cleaned_key = clean_filename(file_name)                    

                    # Convert to Base64
                    images_base64[cleaned_key] = encode_image(img)
            except Exception as e:
                # Log or report error if needed
                print(f"Failed to process image {path}: {e}")                

    return images_base64
