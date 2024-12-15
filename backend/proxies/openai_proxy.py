from openai import OpenAI
import json

def generate_formatted_reference(prompt: str) -> dict:
    """
    Sends a prompt to the OpenAI API to generate formatted references.

    Args:
        prompt (str): The prompt string containing formatting instructions and source details.

    Returns:
        dict: A dictionary with formatted reference components ('footnote', 'bibliography', etc.).
    """
    client = OpenAI()  # Instantiate OpenAI client
            
    try:
        # Create chat completion using the OpenAI SDK
        completion = client.chat.completions.create(
            model="gpt-4o",  # Use the desired model,
            messages=[
                {"role": "system", "content": "You are a formatting assistant for academic references."},
                {"role": "user", "content": prompt}
            ],
        )

        # Extract and parse the response content
        response_content = completion.choices[0].message.content
        
        # Attempt to parse the response as JSON
        return json.loads(response_content)

    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse the OpenAI response as JSON: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while generating the reference: {e}")
