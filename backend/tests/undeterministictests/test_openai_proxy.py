from backend.proxies.openai_proxy import generate_formatted_reference, check_known_fields


# 1. 
# Input

# Wanted response

def test_1():
    ref_type = "literature_list"
    known_data = {
        "Auteur": "A. de Vries",
        "Titel van het artikel": "Privacy en de AVG",
        "Jaar van publicatie": "2018",
        "Tijdschrift": "NJB",
        "Pagina's": "1234-1240",
    }
    output = generate_formatted_reference(known_data, ref_type)
    print(output)

def test_2():
    user_input = "Privacy en de AVG"
    output = check_known_fields(user_input)
    print(output)
    
def test_3():
    user_input = "Privacy en de AVG, Tijdschrift: Nederlands Juristenblad (NJB)  uit 2018"
    output = check_known_fields(user_input)
    print(output)
    
def test_4():
    user_input = "Privacy en de AVG, Tijdschrift: Nederlands Juristenblad (NJB)  uit 2018 A. de Vries "
    output = check_known_fields(user_input)
    print(output)
    
def test_5():
    user_input = "Privacy en de AVG, Tijdschrift: Nederlands Juristenblad (NJB)  uit 2018, volgensmij geschreven door Vries maar weet ik niet zeker.. "
    output = check_known_fields(user_input)
    print(output)