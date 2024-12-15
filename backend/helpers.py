import os

def load_prompt(file_path: str) -> str:
    """
    Loads a prompt file and returns its content.

    Args:
        file_path (str): Path to the prompt file.

    Returns:
        str: Content of the prompt file.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If the file cannot be read.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The prompt file '{file_path}' was not found.")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except IOError as e:
        raise IOError(f"Error reading the prompt file: {e}")
