# Alt Text Generator and Translator (CLI)

A lightweight Python CLI tool for generating Czech and English alt text for images using OpenAI's Vision and Completions API. Designed for accessibility researchers, content creators, and educators.

---

## How it works

The application automates the process of generating and translating alt text for images. It begins by taking images from a specified input folder and processing them to ensure compatibility with the OpenAI Vision API. This includes converting, resizing, and base64 encoding the images. Once prepared, the app sends a batch job to the OpenAI Vision API, which generates alt text in Czech for each image. Subsequently, the app connects to the OpenAI Completions API to translate the Czech alt text into English. The final output is an Excel spreadsheet (.xlsx) that lists the original image names alongside their alt text in both Czech and English.

![alt_text_explanation](https://github.com/user-attachments/assets/4a7a3cf4-80fa-461e-966c-46764ced7502)

---

## Module Structure

```
python_app/
├── cli.py                  # Entry point
├── core.py                 # Pipeline controller
├── processing/             # Converts and prepares images
├── batch_api/              # Handles OpenAI batch interactions
├── translation_api/        # Translation and table export
```

---

## Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python python_app/cli.py --input_folder path/to/images --output_folder path/to/save
```

- `--input_folder`: Folder containing image files (jpg, png, etc.)
- `--output_folder`: Where the translated Excel table will be saved

For information regarding OpenAI APIs check the documentation at https://platform.openai.com

---

## Allowed Image Formats
- .bmp, .jpg, .jpeg, .png, .tif, .tiff, .webp

## Output

A single `.xlsx` file containing:

- Cleaned names of original image files
- AI generated alt text in Czech
- Alt text translated by AI into English

---

## Project Status

- ✅ CLI version: **Stable and ready for use**
- 🛠 GUI version: Under construction.

---

## License

This project is licensed under the [MIT License](LICENSE).
