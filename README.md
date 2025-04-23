# Alt Text Generator and Translator (CLI)

A lightweight Python CLI tool for generating and translating alt text for images using OpenAI's Vision and Chat models. Designed for accessibility researchers, content creators, and educators.

---

## Features

- **Image Processing**: Converts images to base64 for API compatibility
- **Batch Alt Text Generation**: Uses OpenAI's Vision API in batch mode to generate Czech alt texts
- **Alt Text Translation**: Translates Czech alt text into English
- **Excel Export**: Final result saved in a well-structured `.xlsx` file

---

## Folder Structure

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

---

## Output

A single `.xlsx` file containing:
- 
- AI generated alt texts in Czech)
- Translated Czech alt texts into English)

---

## Project Status

- ✅ CLI version: **Stable and ready for demo/presentation**
- ⚒ GUI version: In R&D (using Electron, not included in this release)

---

## License

MIT — free for personal and academic use.