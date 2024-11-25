from backend.proxies.openai_proxy import generate_formatted_reference


def run_test():
    prompt = """
    Generate a JSON object with the following fields:
    - 'footnote': Shortened reference format for footnotes.
    - 'bibliography': Full reference format for bibliographies.
    - 'bibliography_list_entry': Format for an alphabetized bibliography list.

    Example Output:
    {
    "footnote": "Botman 2015, p. 430.",
    "bibliography": "M. Botman, *De Dienstenrichtlijn in Nederland*, Den Haag: Boom juridisch 2015.",
    "bibliography_list_entry": "Botman 2015"
    }

    Input:
    Source Type: Book
    Details: {"author": "M. Botman", "title": "De Dienstenrichtlijn in Nederland", "year": 2015, "place_of_publication": "Den Haag", "publisher": "Boom juridisch"}

    Output:
    """

    formatted_reference = generate_formatted_reference(prompt)
    print(formatted_reference)
