import os
from typing import List
from pydantic import BaseModel

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


# --- Pydantic Models ---
            #    "properties": {
            #         "necessary_fields": {
            #             "type": "array",
            #             "description": "Een lijst met noodzakelijke velden.",
            #             "items": {
            #             "type": "object",
            #             "properties": {
            #                 "field_type": {
            #                 "type": "string",
            #                 "description": "Het type van het noodzakelijke veld."
            #                 }
            #         },
            #         "known_fields": {
            #             "type": "array",
            #             "description": "Een lijst met bekende velden met hun types en waarden.",
            #             "items": {
            #             "type": "object",
            #             "properties": {
            #                 "field_type": {
            #                 "type": "string",
            #                 "description": "Het type van het bekende veld."
            #                 },
            #                 "value": {
            #                 "type": "string",
            #                 "description": "De waarde van het bekende veld."
            #                 }
            #             },
            #             "required": [
            #                 "field_type",
            #                 "value"
            #             ],
            #             "additionalProperties": False
            #             }
            #         },
            #         "unknown_fields": {
            #             "type": "array",
            #             "description": "Een lijst met onbekende velden, alleen hun types.",
            #             "items": {
            #             "type": "object",
            #             "properties": {
            #                 "field_type": {
            #                 "type": "string",
            #                 "description": "Het type van het onbekende veld."
            #                 }
            #             },
            #             "required": [
            #                 "field_type"
            #             ],
            #             "additionalProperties": False
            #             }
            #         }
                    
class NecessaryField(BaseModel):
    field_type: str
    extra_info: str = None

class KnownField(BaseModel):
    field_type: str
    value: str

class UnknownField(BaseModel):
    field_type: str

class CheckFieldsResponse(BaseModel):
    necessary_fields: List[NecessaryField] = []
    known_fields: List[KnownField] = []
    unknown_fields: List[UnknownField] = []
