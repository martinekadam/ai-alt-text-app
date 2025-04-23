import pandas as pd

from translation_api.get_response import get_response

def translate_dataframe(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Translate alt text in a DataFrame using the chat model.

    Parameters
    ----------
    input_df : pandas.DataFrame
        DataFrame containing alt text to be translated. 
        The first column should contain file identifiers, and the second column should contain alt text.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing translated alt text with columns:
        - "file_name" : str
            Identifier of the original file.
        - "alt_text" : str
            Translated alt text.
    """
    translated_alt_texts = []

    for row in input_df.itertuples(index=False):
        try:
            custom_id = row[0]
            alt_text = row[1]

            response = get_response(alt_text)

            translated_alt_texts.append({
                "file_name": custom_id,
                "alt_text": response
            })
        except Exception as e:
            print(f"Translation failed for {custom_id}: {e}")
            continue

    translated_dataframe = pd.DataFrame(translated_alt_texts)

    return translated_dataframe