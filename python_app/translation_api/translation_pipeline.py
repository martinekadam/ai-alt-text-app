import pandas as pd

from translation_api.translate_dataframe import translate_dataframe
from translation_api.join_dataframes import join_dataframes
from translation_api.save_complete_alt_text_table import save_complete_alt_text_table


def translation_pipeline(original_df: pd.DataFrame, output_file_path: str, output_file_name: str) -> str:
    if original_df.empty:
        raise ValueError("Input DataFrame is empty. Cannot proceed with translation.")
    
    print("Translating alt text...")
    
    translated_dataframe = translate_dataframe(original_df)

    joined_dataframes = join_dataframes(original_df, translated_dataframe)

    final_file_path = save_complete_alt_text_table(joined_dataframes, output_file_path, output_file_name)

    return final_file_path

