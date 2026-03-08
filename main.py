import streamlit as st

from ppv1_portafolio.componente_sidebar import componente_sidebar
from ppv1_portafolio.conf_rutas import LOGO_URL


st.set_page_config(
    page_title="Proyecto PPV1",
    page_icon=LOGO_URL,
    layout="wide",
    initial_sidebar_state="expanded"
)


componente_sidebar()