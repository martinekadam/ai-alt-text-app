import pandas as pd
import json
import os

def process_batch_result(batch_result_full_path: str) -> pd.DataFrame:
    """
    Process a batch result file and extract relevant data into a DataFrame.

    Parameters
    ----------
    batch_result_full_path : str
        Full path to the batch result file.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing extracted results with columns:
        - "file_name": Custom ID associated with the processed task.
        - "alt_text": Extracted message content from the response.
    """
    result = []

    if not os.path.isfile(batch_result_full_path):
        raise FileNotFoundError(f"Batch result file not found: {batch_result_full_path}")

    with open(batch_result_full_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                data = json.loads(line.strip())

                custom_id = data.get('custom_id')
                message_content = (
                    data.get('response', {})
                    .get('body', {})
                    .get('choices', [{}])[0]
                    .get('message', {})
                    .get('content')
                )

                if custom_id and message_content:
                    result.append({'file_name': custom_id, 'alt_text': message_content})
            except (json.JSONDecodeError, IndexError, AttributeError) as e:
                continue

    batch_result_dataframe = pd.DataFrame(result)

    return batch_result_dataframe