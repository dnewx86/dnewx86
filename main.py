import streamlit as st

from ppv1_portafolio.componente_sidebar import componente_sidebar


st.set_page_config(
    page_title="Portafolio",
    page_icon="https://raw.githubusercontent.com/dnewx86/dnewx86/main/ppv1_portafolio/img/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)


componente_sidebar()