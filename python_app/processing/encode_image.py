import base64
from io import BytesIO
from PIL import Image

def encode_image(image: Image.Image) -> str:
    """
    Encode a PIL Image into Base64 format.

    Parameters
    ----------
    image : PIL.Image.Image
        Image object to be encoded.

    Returns
    -------
    str
        Base64-encoded string representing the image content.
    """
    buffer = BytesIO()
    try:
        image.save(buffer, format="JPEG")  # Ensure it's saved in JPEG format
    except Exception as e:
        raise RuntimeError(f"Failed to encode image to JPEG: {e}")
    buffer.seek(0)

    return base64.b64encode(buffer.getvalue()).decode("utf-8")
