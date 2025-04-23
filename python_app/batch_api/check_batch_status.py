from openai import OpenAI
from datetime import datetime

client = OpenAI()

def check_batch_status(batch_job_id: str, verbose: bool = False) -> dict:
    """
    Check the status of a batch job and calculate its running time if not completed.

    Parameters
    ----------
    batch_job_id : str
        Identifier of the batch job to check.

    Returns
    -------
    dict
        Dictionary containing:
        - "status" : str
            Current status of the batch job.
        - "running_time" : str, optional
            Elapsed time since job creation if the job is not yet completed.
    """
    try:
        batch_job = client.batches.retrieve(batch_job_id)
    except Exception as e:
        return {"status": "error", "message": str(e)}

    # Access attributes directly
    status = batch_job.status
    created_at = batch_job.created_at

    result = {
        "status": status
    }

    if status != "completed" and created_at:
        # Convert Unix timestamp to datetime
        created_time = datetime.fromtimestamp(created_at)
        current_time = datetime.now()
        running_time = current_time - created_time
        running_time_str = str(running_time).split('.')[0]  # Remove microseconds
        result["running_time"] = running_time_str

    if verbose:
        print(f"Batch job status: {status}")
        if "running_time" in result:
            print(f"Running time: {result['running_time']}")

    return result