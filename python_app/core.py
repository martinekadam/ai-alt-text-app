import os
import sys
import traceback

from processing.processing_pipeline import processing_pipeline
from batch_api.batch_pipeline import run_batch_pipeline
from translation_api.translation_pipeline import translation_pipeline

def main(input_folder: str, output_folder: str) -> None:
    try:
        if not os.path.exists(input_folder):
            print(f"Error: Input folder '{input_folder}' does not exist.")
            sys.exit(1)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        images_base64 = processing_pipeline(input_folder)
        batch_results_df = run_batch_pipeline(images_base64)

        output_file = translation_pipeline(batch_results_df, output_folder, "translated_results.xlsx")

        print(f"✅ Processing completed! Output saved to: {output_file}")

    except Exception as e:
        traceback.print_exc()
        print(f"❌ Error during processing: {e}")
        sys.exit(1)
