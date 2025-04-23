import base64
import os

image_path = os.path.join(os.path.dirname(__file__), "assets", "bride_kidnapping_2024.jpg")

def load_base64_image(path: str) -> str:
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

try:
    image_base64 = load_base64_image(image_path)
except FileNotFoundError:
    image_base64 = None
    print(f"Warning: One-shot image not found at {image_path}")

class BatchAPIConfig:
    ENDPOINT = "/v1/chat/completions"
    COMPLETION_WINDOW = "24h"
    TEMPERATURE = 0.3
    MODEL = "gpt-4o"

class Prompts:
    # Prompts for the Vision API.
    SYSTEM_PROMPT = "Jsi expert na webovou přístupnost. Vytváříš alt texty pro obrázky. Alt texty vytváříš v českém jazyce."
    USER_PROMPT = "Vytvoř alt texty pro tento obrázek."

class ShotExamples:
    # Uses an example of image and alt text from One World 2024 Bride Kidnapping, 2023. 
    # URL: https://m.media-amazon.com/images/M/MV5BM2YxZmU2YzktOTYyNi00MTcwLTk3OWYtODBlMWIwYjA1ZDc3XkEyXkFqcGc@._V1_QL75_UX582_.jpg
    IMAGE_PATH = image_path
    ONE_SHOT_IMAGE_BASE64 = image_base64
    ONE_SHOT_ASSISTANT_RESPONSE = "Rodina sedí a povídá si u stolu s ovocem a občerstvením."

