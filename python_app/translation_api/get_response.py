from openai import OpenAI

from translation_api.config import TranslationConfig

client = OpenAI()

def get_response(alt_text: str) -> str:
    """
    Generate a response using the chat model based on the provided alt text.

    Parameters
    ----------
    alt_text : str
        Alternative text to be translated or processed by the model.

    Returns
    -------
    str
        Model-generated response content.
    """
    response = client.chat.completions.create(
        model=TranslationConfig.MODEL,
        temperature=TranslationConfig.TEMPERATURE,
        messages=[
            {
                "role": "system",
                "content": TranslationConfig.SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": TranslationConfig.USER_PROMPT + f"{alt_text}"
            },
        ]
    )

    response = response.choices[0].message.content

    return response