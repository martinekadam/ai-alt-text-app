import os
from openai import OpenAI

client = OpenAI()

def save_batch_result(batch_job_id: str, output_file_path: str, output_file_name: str) -> str:
    """
    Retrieve and save the result of a batch job to a file.

    Parameters
    ----------
    batch_job_id : str
        Response object of the created batch job containing its ID.
    output_file_path : str
        Path to the directory where the result file will be saved.
    output_file_name : str
        Name of the output file.

    Returns
    -------
    str
        Full path to the saved batch result file.
    """
    try:
        batch_job_result = client.batches.retrieve(batch_job_id)
        result_file_id = batch_job_result.output_file_id
        result = client.files.content(result_file_id).content
    except Exception as e:
        raise RuntimeError(f"Failed to retrieve batch result: {e}")

    full_path = os.path.join(output_file_path, output_file_name)

    os.makedirs(output_file_path, exist_ok=True)
    with open(full_path, 'wb') as file:
        file.write(result)

    return full_path
