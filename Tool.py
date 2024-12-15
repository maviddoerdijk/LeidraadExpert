import streamlit as st
from pydantic import BaseModel
from typing import List, Optional

st.set_page_config(page_title="Leidraad Expert", page_icon="📚")
st.title("Leidraad Expert")

# --- Pydantic Models ---
class KnownField(BaseModel):
    field_type: str
    value: str

class UnknownField(BaseModel):
    field_type: str

class CheckFieldsResponse(BaseModel):
    known_fields: List[KnownField] = []
    unknown_fields: List[UnknownField] = []

# --- Placeholder Functions ---
def check_known_fields(user_input: str) -> CheckFieldsResponse:
    # In a real scenario, logic would parse user_input and determine known/unknown fields
    return CheckFieldsResponse(
        known_fields=[
            KnownField(field_type="Auteur", value="A. de Vries"),
            KnownField(field_type="Titel van het artikel", value="Privacy en de AVG"),
            KnownField(field_type="Jaar van publicatie", value="2018")
        ],
        unknown_fields=[
            UnknownField(field_type="Tijdschrift"),
            UnknownField(field_type="Pagina's")
        ]
    )

def get_formatted_reference(known_data: dict, ref_type: str) -> str:
    # Placeholder logic for demonstration
    if ref_type == 'footnote':
        return "2. De Vries 2018, p. 1236."
    elif ref_type == 'lit_list':
        return """
De Vries 2018
A. de Vries, 'Privacy en de AVG', NJB 2018, p. 1234-1240.
        """
    return ""

# --- Helper Functions ---
def generate_and_show_references(known_data: dict):
    """Generate both footnote and literature list references and display them."""
    if not known_data:
        st.warning("Geen data beschikbaar om referenties te genereren.")
        return

    with st.spinner("Bezig met genereren van referenties..."):
        footnote_ref = get_formatted_reference(known_data, ref_type='footnote')
        lit_list_ref = get_formatted_reference(known_data, ref_type='lit_list')

    st.subheader("Gegenereerde Referenties")

    st.markdown("**Footnote**:")
    footnote_container = st.container()
    footnote_container.markdown(f"```\n{footnote_ref}\n```")

    st.markdown("**Literatuurlijst**:")
    lit_list_container = st.container()
    lit_list_container.markdown(f"```\n{lit_list_ref}\n```")


# --- Session State Initialization ---
if "final_known_data" not in st.session_state:
    st.session_state.final_known_data = {}

if "response" not in st.session_state:
    st.session_state.response = None

# --- App UI ---
st.write("Voer hieronder een omschrijving in en druk op 'Check' om bekende en onbekende velden te achterhalen.")

user_input = st.text_area("Uw invoer:", placeholder="Bijv. 'Privacy en de AVG'")

col1, col2 = st.columns([1,1])
with col1:
    check_button = st.button("Check")

with col2:
    clear_button = st.button("Clear")

if clear_button:
    # Reset the application state
    st.session_state.response = None
    st.session_state.final_known_data = {}
    st.experimental_rerun()

if check_button:
    if not user_input.strip():
        st.error("Voer eerst een omschrijving in voordat u op 'Check' drukt.")
    else:
        with st.spinner("Bezig met controleren..."):
            st.session_state.response = check_known_fields(user_input.strip())
            # Store initial known fields
            st.session_state.final_known_data = {kf.field_type: kf.value for kf in st.session_state.response.known_fields}

# --- Display Known/Unknown Fields and Handle Unknowns ---
if st.session_state.response:
    response = st.session_state.response
    st.subheader("Gevonden velden:")
    if response.known_fields:
        for kf in response.known_fields:
            st.markdown(f"✅ **{kf.field_type}**: {kf.value}")
    else:
        st.info("Er zijn geen bekende velden gevonden.")

    if response.unknown_fields:
        for uf in response.unknown_fields:
            st.markdown(f"❌ **{uf.field_type}**: Onbekend")

        st.subheader("Vul de ontbrekende velden in:")
        with st.form("unknown_fields_form"):
            unknown_values = {}
            for uf in response.unknown_fields:
                unknown_values[uf.field_type] = st.text_input(f"{uf.field_type}")

            submit_unknowns = st.form_submit_button("Genereer Referenties")

        if submit_unknowns:
            # Check if all unknown fields are filled
            if any(not val.strip() for val in unknown_values.values()):
                st.warning("Alle onbekende velden moeten worden ingevuld voordat we verder kunnen gaan.")
            else:
                for field, value in unknown_values.items():
                    st.session_state.final_known_data[field] = value

                # All fields known now?
                if all(val.strip() for val in st.session_state.final_known_data.values()):
                    st.success("Alle velden zijn nu bekend! De referenties worden gegenereerd.")
                    generate_and_show_references(st.session_state.final_known_data)
                else:
                    st.warning("Niet alle velden zijn geldig ingevuld. Probeer opnieuw.")
    else:
        # No unknown fields, directly generate references if all known
        if all(val.strip() for val in st.session_state.final_known_data.values()):
            st.success("Alle velden zijn bekend! De referenties zijn gegenereerd:")
            generate_and_show_references(st.session_state.final_known_data)
        else:
            st.warning("Er ontbreken gegevens om referenties te genereren. Controleer de invoer.")
