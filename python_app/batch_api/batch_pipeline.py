import shutil
import time
import tempfile
import pandas as pd

from batch_api.create_tasks_array import create_tasks_array
from batch_api.create_batch_file import create_batch_file
from batch_api.upload_batch_file import upload_batch_file
from batch_api.create_batch_job import create_batch_job
from batch_api.check_batch_status import check_batch_status
from batch_api.save_batch_result import save_batch_result
from batch_api.process_batch_result import process_batch_result

def run_batch_pipeline(images_base64: dict[str, str], verbose: bool = True) -> pd.DataFrame:
    """
    Execute the batch processing pipeline for a set of Base64-encoded images.

    Parameters
    ----------
    images_base64 : dict
        Dictionary where keys are identifiers and values are Base64-encoded image strings.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing processed batch results.

    Raises
    ------
    Exception
        If the batch job fails or is cancelled.
    """
    temp_dir = tempfile.mkdtemp(prefix="batch_api_")

    try: 
        tasks = create_tasks_array(images_base64)

        batch_file_path = create_batch_file(temp_dir, "batch_tasks.jsonl", tasks)

        batch_file = upload_batch_file(batch_file_path)

        batch_job = create_batch_job(batch_file)

        while True:
            current_batch_status = check_batch_status(batch_job.id, verbose=verbose)
            if current_batch_status["status"] == "completed":
                batch_result = save_batch_result(batch_job.id, temp_dir, "batch_result.jsonl")
                break
            elif current_batch_status["status"] in ["failed", "cancelled"]:
                raise Exception(f"Batch job failed or was cancelled.")
            time.sleep(30)

        batch_result_dataframe = process_batch_result(batch_result)
        return batch_result_dataframe

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
