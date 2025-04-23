from openai import OpenAI

from batch_api.config import BatchAPIConfig

client = OpenAI()

def create_batch_job(batch_file: dict, endpoint: str = BatchAPIConfig.ENDPOINT, completion_window: str = BatchAPIConfig.COMPLETION_WINDOW) -> dict:
    """
    Create a batch job for processing uploaded tasks.

    Parameters
    ----------
    batch_file : dict
        Response object of the uploaded batch file containing its ID.
    endpoint : str, optional
        API endpoint for processing the batch. Default is "/v1/chat/completions".
    completion_window : str, optional
        Time window for batch job completion. Default is "24h".

    Returns
    -------
    dict
        Response object containing details of the created batch job.
    """
    if not hasattr(batch_file, 'id'):
        raise ValueError("Invalid batch_file: missing 'id' attribute.")

    batch_file_id = batch_file.id

    batch_job = client.batches.create(
        input_file_id=batch_file_id,
        endpoint=endpoint,
        completion_window=completion_window
    )

    print(f"Batch job created with ID: {batch_job.id}")

    return batch_job