from openai import OpenAI
import json
from backend.proxies.strings import leidraad_source_prompt
from backend.helpers import CheckFieldsResponse

### Examples
# 1. 
# Input: 
# known_data = {
#     "Auteur": "A. de Vries",
#     "Titel van het artikel": "Privacy en de AVG",
#     "Jaar van publicatie": "2018",
#     "Tijdschrift": "NJB",
#     "Pagina's": "1234-1240",
# }
# ref_type = "footnote"
# Output:
# "2. De Vries 2018, p. 1236."
# 2. 
# Input: 
# known_data = {
#     "Auteur": "A. de Vries",
#     "Titel van het artikel": "Privacy en de AVG",
#     "Jaar van publicatie": "2018",
#     "Tijdschrift": "NJB",
#     "Pagina's": "1234-1240",
# }
# ref_type = "literature_list"
# Output:
# """
# De Vries 2018
# A. de Vries, 'Privacy en de AVG', NJB 2018, p. 1234-1240.
# """

def generate_formatted_reference(known_data: dict, ref_type: str) -> str:
    """
    Generates a formatted reference based on known data and the desired reference type.

    Args:
        known_data (dict): A dictionary containing known reference data.
        ref_type (str): The type of reference to generate ('footnote' or 'literature_list').

    Returns:
        str: The formatted reference.
    """
    # Placeholder logic for demonstration
    client = OpenAI()  # Instantiate OpenAI client
    prompt = f"""
    Instructies voor het genereren van een geformatteerde verwijzing:
    ```
    {leidraad_source_prompt}
    ```
    Bekende informatie:
    {known_data}
    
    Genereer een JSON-object.
    """
    
    try:
        # Create chat completion using the OpenAI SDK
        completion = client.chat.completions.create(
            model="gpt-4o",  # Use the desired model,
            messages=[
                {"role": "system", "content": "Je bent een expert op het gebied van de Juridische Leidraad. Je genereert antwoorden op basis van kennis die je reeds hebt, en hanteert de regels uit de Juridische Leidraad. Je antwoord alles in Nederlands."},
                {"role": "user", "content": prompt}
            ],
            response_format={
                "type": "json_schema",
                "json_schema": {
                "name": "reference_rules",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                    "rules_to_follow_footnote": {
                        "type": "string",
                        "description": "Regels om te volgen bij voetnootverwijzingen."
                    },
                    "rules_to_follow_literature_list": {
                        "type": "string",
                        "description": "Regels om te volgen bij verwijzingen in de literatuurlijst."
                    },
                    "footnote": {
                        "type": "string",
                        "description": "De tekst van de voetnoot."
                    },
                    "literature_list": {
                        "type": "string",
                        "description": "De tekst voor de literatuurlijst."
                    }
                    },
                    "required": [
                    "rules_to_follow_footnote",
                    "rules_to_follow_literature_list",
                    "footnote",
                    "literature_list"
                    ],
                    "additionalProperties": False
                }
            }
        },
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        # Extract and parse the response content
        response_content = completion.choices[0].message.content
        
        # Attempt to parse the response as JSON
        response = json.loads(response_content)
        
        return response.get(ref_type)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse the OpenAI response as JSON: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while generating the reference: {e}")
    
    
def check_known_fields(user_input: str) -> CheckFieldsResponse:
    """
    Based on the information provided in the user input, determine known and unknown fields.
    Fill in as many as you can in the known fields.
    """
    client = OpenAI()
    prompt = f"""
    Instructies voor het genereren van een geformatteerde verwijzing:
    ```
    {leidraad_source_prompt}
    ```
    
    Bepaal op basis van de verstrekte informatie in de gebruikersinvoer welke velden bekend en onbekend zijn.
    Vul alle bekende velden zo volledig mogelijk in.

    Verstrekte informatie:
    {user_input}
    """
    try:
        # Create chat completion using the OpenAI SDK
        completion = client.chat.completions.create(
            model="gpt-4o",  # Use the desired model,
            messages=[
                {"role": "system", "content": "Je bent een expert op het gebied van de Juridische Leidraad. Je genereert antwoorden op basis van kennis die je reeds hebt, en hanteert de regels uit de Juridische Leidraad. Je antwoord alles in Nederlands."},
                {"role": "user", "content": prompt},
            ],
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "CheckFieldsResponse",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties": {
                            "necessary_fields": {
                                "type": "array",
                                "description": "Een lijst van noodzakelijke velden, elk vereist een veldtype en aanvullende informatie.",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "field_type": {
                                            "type": "string",
                                            "description": "Het type van het noodzakelijke veld."
                                        },
                                        "extra_info": {
                                            "type": "string",
                                            "description": "Aanvullende informatie met betrekking tot het noodzakelijke veld."
                                        }
                                    },
                                    "required": [
                                        "field_type",
                                        "extra_info"
                                    ],
                                    "additionalProperties": False
                                }
                            },
                            "known_fields": {
                                "type": "array",
                                "description": "Een lijst van bekende velden, elk vereist een veldtype en een waarde.",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "field_type": {
                                            "type": "string",
                                            "description": "Het type van het bekende veld."
                                        },
                                        "value": {
                                            "type": "string",
                                            "description": "De waarde die bij het bekende veld hoort."
                                        }
                                    },
                                    "required": [
                                        "field_type",
                                        "value"
                                    ],
                                    "additionalProperties": False
                                }
                            },
                            "unknown_fields": {
                                "type": "array",
                                "description": "Een lijst van onbekende velden, elk vereist alleen een veldtype.",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "field_type": {
                                            "type": "string",
                                            "description": "Het type van het onbekende veld."
                                        }
                                    },
                                    "required": [
                                        "field_type"
                                    ],
                                    "additionalProperties": False
                                }
                            }
                        },
                        "required": [
                            "necessary_fields",
                            "known_fields",
                            "unknown_fields"
                        ],
                        "additionalProperties": False
                    }
                }
            },
            temperature=1,
            max_completion_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Extract and parse the response content
        response_content = completion.choices[0].message.content
        
        # Attempt to parse the response as JSON
        response = json.loads(response_content)
        
        # load it as a CheckFieldsResponse object
        return CheckFieldsResponse(**response)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse the OpenAI response as JSON: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while checking known fields: {e}")
