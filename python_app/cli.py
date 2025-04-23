import argparse
from core import main

def cli():
    parser = argparse.ArgumentParser(
        description="Generate and translate alt text for images using OpenAI's Vision and Chat APIs."
    )
    parser.add_argument("--input_folder", type=str, required=True, help="Path to folder with images.")
    parser.add_argument("--output_folder", type=str, required=True, help="Where to save the alt texts.")

    args = parser.parse_args()

    main(
        input_folder=args.input_folder,
        output_folder=args.output_folder
    )

if __name__ == "__main__":
    cli()
