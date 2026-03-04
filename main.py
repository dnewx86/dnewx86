import streamlit as st


st.set_page_config(
    page_title="Portafolio",
    page_icon="ppv1_portafolio/img/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.sidebar.title("Menú")
option = st.sidebar.radio("", ["Home", "Proyectos", "Contacto"])



if option == "Home":
    st.subheader("Página Home")
    st.write("")

elif option == "Proyectos":
    st.subheader("Proyectos")
    st.write("")

elif option == "Contacto":
    st.subheader("Contacto")
    st.write("")