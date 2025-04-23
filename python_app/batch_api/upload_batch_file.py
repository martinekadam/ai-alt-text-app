import os
from openai import OpenAI

client = OpenAI()

def upload_batch_file(batch_file_path: str) -> dict:
    """
    Upload a batch file for processing.

    Parameters
    ----------
    batch_file_path : str
        Path to the batch file to be uploaded.

    Returns
    -------
    dict
        Response object containing details of the uploaded file.
    """
    if not os.path.isfile(batch_file_path):
        raise FileNotFoundError(f"Batch file not found: {batch_file_path}")

    with open(batch_file_path, "rb") as file:
        batch_file = client.files.create(
            file=file,
            purpose="batch"
        )

    return batch_file