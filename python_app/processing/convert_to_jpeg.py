import os
from PIL import Image

def convert_to_jpeg(image_path, temp_dir):
    """
    Convert an image file to JPEG format and save it in a temporary directory.

    Parameters
    ----------
    image_path : str
        Path to the original image file.
    temp_dir : str
        Path to the temporary directory where the JPEG image will be stored.

    Returns
    -------
    str
        Path to the converted JPEG image.
    """
    with Image.open(image_path) as img:
        # Convert image to RGB (required for JPEG format)
        img = img.convert("RGB")
        
        # Define the new file path in the temporary directory
        filename_wo_ext = os.path.splitext(os.path.basename(image_path))[0]
        jpeg_path = os.path.join(temp_dir, f"{filename_wo_ext}.jpeg")
        
        # Save the image as JPEG
        img.save(jpeg_path, format="JPEG")

    return jpeg_path
