import json
from backend.proxies.openai_proxy import generate_formatted_reference


def get_formatted_reference(source_type: str, details: dict) -> dict:
    """
    Generates properly formatted references based on the source type and provided details.
    
    
    Functionality:
        - Takes the source type, e.g. 'book' and the details of the source, and prompts to gpt 
        to generate the formatted reference. 
        - Uses leidraad_source_prompt to generate the formatted reference (information for all source_types).
        - Generates a json using backend.proxies.openai_proxy with the prompt and the source_type.
        - Example leidraad_source_prompt for a specific source_type ('book'):
            1. Boek (book)

            Required Fields:

            author (str): The author's initials followed by the surname (e.g., "M. Botman").
            title (str): The title of the book, including any subtitles, italicized and separated by a period from the main title.
            year (int): The year of publication.
            place_of_publication (str): The city where the book was published (e.g., "Den Haag").
            publisher (str): The name of the publisher (e.g., "Boom Juridisch").
            page_reference (str, optional): Specific page or paragraph referenced (e.g., "p. 45-47" or "par. 2.4").
            Notes:

            The title begins with a capital letter; subtitles are italicized and start after a period.
            Do not include academic titles (e.g., "Dr.", "Prof.") or the publisher's legal form (e.g., "B.V.").
            If the place of publication or year is unknown, use "z.p." (zonder plaats) or "z.j." (zonder jaar).
            Series information can be included in parentheses after the title, not italicized.
            2. Bijdragen in boeken (Contributions in Books)
            In de literatuurlijst:
            Botman 2015
            M. Botman, De Dienstenrichtlijn in Nederland. De gevolgen
            van richtlijn 2006/123/EG voor de nationale rechtsorde vanuit
            Europees perspectief (NILG – Markt, overheid en recht, deel 6),
            Den Haag: Boom juridisch 2015.
            Van Drongelen & Hofsteenge 2022
            J. van Drongelen & J.A. Hofsteenge, De Arbowet geschetst (Arbeidsomstandighedenrecht, deel 5), Zutphen: Uitgeverij Paris
            2022.
            Spijkerboer 2014
            T.P. Spijkerboer, De Nederlandse rechter in het vreemdelingenrecht, Den Haag: Sdu 2014.
            In de voetnoten:
            1. Botman 2015, p. 430.
            2. Spijkerboer 2014, p. 6.
            3. Van Drongelen & Hofsteenge 2022, par. 2.4
        - Returns the formatted references

    Args:
        source_type (str): The type of source, e.g., "Book", "Journal Article", "Case Law", etc.
        details (dict): A dictionary containing all necessary fields for the chosen source type.

    Returns:
        dict: A dictionary containing the formatted references:
            - "footnote": The shortened reference format for footnotes.
            - "bibliography": The full reference format for the bibliography or literature list.
            - "bibliography_list_entry": How the reference is listed alphabetically in the bibliography.
    """
    # Load the leidraad source prompt template
    leidraad_prompt = load_prompt('leidraad_source_prompt.txt')

    # Construct the prompt
    formatted_prompt = (
        f"{leidraad_prompt}\n\n"
        f"### Instructions ###\n"
        f"Generate a JSON object with the following fields:\n"
        f"- 'footnote': Shortened reference format for footnotes.\n"
        f"- 'bibliography': Full reference format for bibliographies.\n"
        f"- 'bibliography_list_entry': Format for an alphabetized bibliography list.\n\n"
        f"### Example Output ###\n"
        f"{{\n"
        f"  \"footnote\": \"Botman 2015, p. 430.\",\n"
        f"  \"bibliography\": \"M. Botman, *De Dienstenrichtlijn in Nederland*, Den Haag: Boom juridisch 2015.\",\n"
        f"  \"bibliography_list_entry\": \"Botman 2015\"\n"
        f"}}\n\n"
        f"### Input Details ###\n"
        f"Source Type: {source_type}\n"
        f"Details: {json.dumps(details, indent=2)}\n\n"
        f"### Output ###"
    )

    # Generate formatted reference using OpenAI API
    formatted_reference = generate_formatted_reference(prompt=formatted_prompt)

    # Extract and return the reference formats
    return {
        "footnote": formatted_reference.get("footnote", ""),
        "bibliography": formatted_reference.get("bibliography", ""),
        "bibliography_list_entry": formatted_reference.get("bibliography_list_entry", "")
    }