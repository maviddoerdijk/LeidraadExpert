import streamlit as st
from pydantic import BaseModel
from typing import List, Optional
from backend.proxies.openai_proxy import generate_formatted_reference, check_known_fields
from backend.helpers import KnownField, UnknownField, CheckFieldsResponse

st.set_page_config(page_title="Leidraad Expert", page_icon="📚")
st.title("Leidraad Expert")



# --- Helper Functions ---
def generate_and_show_references(known_data: dict):
    """Generate both footnote and literature list references and display them."""
    if not known_data:
        st.warning("Geen data beschikbaar om referenties te genereren.")
        return

    with st.spinner("Bezig met genereren van referenties..."):
        footnote_ref = generate_formatted_reference(known_data, ref_type='footnote')
        literature_list_ref = generate_formatted_reference(known_data, ref_type='literature_list')

    st.subheader("Gegenereerde Referenties")

    st.markdown("**Footnote**:")
    footnote_container = st.container()
    footnote_container.markdown(f"```\n{footnote_ref}\n```")

    st.markdown("**Literatuurlijst**:")
    literature_list_container = st.container()
    literature_list_container.markdown(f"```\n{literature_list_ref}\n```")


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