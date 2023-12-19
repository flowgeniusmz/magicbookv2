import streamlit as st

def initialize_session_states():
    # STORY ELEMENTS
    if "character_name" not in st.session_state:
        st.session_state.character_name = ""
    if "character_description" not in st.session_state:
        st.session_state.character_description = ""
    if "relation_to_character" not in st.session_state:
        st.session_state.relation_to_character = ""
    if "theme_category" not in st.session_state:
        st.session_state.theme_category = ""
    if "theme_description" not in st.session_state:
        st.session_state.theme_description = ""
    if "genre" not in st.session_state:
        st.session_state.genre = ""
    if "setting" not in st.session_state:
        st.session_state.setting = ""
    if "magical_object" not in st.session_state:
        st.session_state.magical_object = ""
    if "secondary_character" not in st.session_state:
        st.session_state.secondary_character = ""
    if "plot_element" not in st.session_state:
        st.session_state.plot_element = ""

    #IMAGE ELEMENTS
    if "uploaded_image" not in st.session_state:
        st.session_state.uploaded_image = ""
    if "uploaded_image_path" not in st.session_state:
        st.session_state.uploaded_image_path = ""
    if "uploaded_image_base64" not in st.session_state:
        st.session_state.uploaded_image_base64 = ""
    if "generated_image" not in st.session_state:
        st.session_state.generate_image = ""

    #STORY DATA OBJECTS
    if "story_data_elements" not in st.session_state:
        st.session_state.story_data_form_elements = {
            "character_name": "",
            "relation_to_character": "",
            "theme_category": "",
            "theme_description": "",
            "genre": "",
            "setting": "",
            "secondary_character": "",
            "plot_element": "",
            "magical_object": "",
        }

    if "story_data_pages"  not in st.session_state:
        st.session_state.story_data_pages = {
            "page1": {"narrative_outline": "", "storybook_text": "", "illustration_description": "", "gen-id": "", "seed": ""},
            "page2": {"narrative_outline": "", "storybook_text": "", "illustration_description": "", "gen-id": "", "seed": ""},
            "page3": {"narrative_outline": "", "storybook_text": "", "illustration_description": "", "gen-id": "", "seed": ""},
            "page4": {"narrative_outline": "", "storybook_text": "", "illustration_description": "", "gen-id": "", "seed": ""},
            "page5": {"narrative_outline": "", "storybook_text": "", "illustration_description": "", "gen-id": "", "seed": ""},
            "page6": {"narrative_outline": "", "storybook_text": "", "illustration_description": "", "gen-id": "", "seed": ""},
            "page7": {"narrative_outline": "", "storybook_text": "", "illustration_description": "", "gen-id": "", "seed": ""},
            "page8": {"narrative_outline": "", "storybook_text": "", "illustration_description": "", "gen-id": "", "seed": ""},
            "page9": {"narrative_outline": "", "storybook_text": "", "illustration_description": "", "gen-id": "", "seed": ""},
            "page10": {"narrative_outline": "", "storybook_text": "", "illustration_description": "", "gen-id": "", "seed": ""}
        }
    
    if "story_data_character" not in st.session_state:
        st.session_state.story_data_character = {
            "character_name": "", 
            "relation_to_character": "",
            "character_description": "", 
            "character_image": ""
        }
    return