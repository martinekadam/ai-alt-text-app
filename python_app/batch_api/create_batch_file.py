import os
import json

def create_batch_file(output_file_path: str, output_file_name: str, tasks: list[dict]) -> str:
    """
    Create a batch file containing JSON-formatted tasks.

    Parameters
    ----------
    output_file_path : str
        Path to the directory where the batch file will be saved.
    output_file_name : str
        Name of the output batch file.
    tasks : list of dict
        List of task dictionaries to be written to the file.

    Returns
    -------
    str
        Full path to the created batch file.
    """
    full_path = os.path.join(output_file_path, output_file_name)

    os.makedirs(output_file_path, exist_ok=True)

    with open(full_path, 'w', encoding='utf-8') as file:
        for obj in tasks:
            file.write(json.dumps(obj, ensure_ascii=False) + '\n')

    return full_path