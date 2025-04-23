import pandas as pd

def join_dataframes(first_df: pd.DataFrame, second_df: pd.DataFrame) -> pd.DataFrame:
    """
    Join two DataFrames on the "file_name" column.

    Parameters
    ----------
    first_df : pandas.DataFrame
        First DataFrame containing original data.
    second_df : pandas.DataFrame
        Second DataFrame containing translated data.

    Returns
    -------
    pandas.DataFrame
        Merged DataFrame with columns from both input DataFrames.
        Columns from `first_df` are suffixed with "_original" and columns from `second_df` are suffixed with "_translated".
    """    
    for df_name, df in [("first_df", first_df), ("second_df", second_df)]:
        if "file_name" not in df.columns:
            raise ValueError(f"{df_name} must contain a 'file_name' column.")
        
    joined_df = first_df.merge(second_df, on="file_name", suffixes=("_original", "_translated"))

    return joined_df