import unicodedata

def clean_filename(filename: str) -> str:
    """
    Clean up the filename by removing diacritics, lowercasing, and replacing special characters.
    """
    # Normalize unicode (remove accents/diacritics)
    normalized = unicodedata.normalize('NFKD', filename)
    ascii_encoded = normalized.encode('ASCII', 'ignore').decode('ASCII')

    # Lowercase and replace unwanted characters
    cleaned = ascii_encoded.lower().replace(' ', '_')
    cleaned = ''.join(char for char in cleaned if char.isalnum() or char in ('_', '-', '.'))
    return cleaned
