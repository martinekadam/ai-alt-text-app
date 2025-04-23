import pandas as pd
from pathlib import Path


def save_complete_alt_text_table(input_df: pd.DataFrame, output_file_path: str, output_file_name: str) -> str:
    """
    Save a DataFrame as an Excel file.

    Parameters
    ----------
    input_df : pandas.DataFrame
        DataFrame containing the alt text data.
    output_file_path : str
        Path to the directory where the file will be saved.
    output_file_name : str
        Name of the output Excel file.

    Returns
    -------
    str
        Full path to the saved Excel file.
    """
    if input_df.empty:
        raise ValueError("Input DataFrame is empty. Nothing to save.")

    output_dir = Path(output_file_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    full_path = output_dir / output_file_name
    input_df.to_excel(full_path, index=False, sheet_name="alt_texty")

    return str(full_path)
