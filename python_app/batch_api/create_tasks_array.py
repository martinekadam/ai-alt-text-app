from batch_api.config import Prompts, ShotExamples, BatchAPIConfig

def build_message_chain(image_base64: str) -> list:
    return [
        {"role": "system", "content": Prompts.SYSTEM_PROMPT},
        {"role": "user", "content": [
            {"type": "text", "text": Prompts.USER_PROMPT},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{ShotExamples.ONE_SHOT_IMAGE_BASE64}", "detail": "low"}}
        ]},
        {"role": "assistant", "content": ShotExamples.ONE_SHOT_ASSISTANT_RESPONSE},
        {"role": "user", "content": [
            {"type": "text", "text": Prompts.USER_PROMPT},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}", "detail": "low"}}
        ]}
    ]

def create_tasks_array(images_base64: dict[str, str]) -> list[dict]:
    """
    Create an array of task dictionaries for Vision API requests.

    Parameters
    ----------
    images_base64 : dict
        Dictionary where keys are identifiers and values are Base64-encoded image strings.

    Returns
    -------
    list
        List of task dictionaries formatted for Vision API requests.
    """

    tasks = []

    for key, value in images_base64.items():

        task = {
            "custom_id": f"{key}",
            "method": "POST",
            "url": BatchAPIConfig.ENDPOINT,
            "body": {
                "model": BatchAPIConfig.MODEL,
                "temperature": BatchAPIConfig.TEMPERATURE,
                "messages": build_message_chain(value)
            }
        }
        
        tasks.append(task)

    return tasks