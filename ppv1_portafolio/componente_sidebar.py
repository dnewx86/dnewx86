import streamlit as st

def componente_sidebar():

    st.markdown("""
        <style>

            div[role="radiogroup"] label > div:first-child {
                display: none;
            }

            div[role="radiogroup"] label {
                display: flex;
                justify-content: center;
                align-items: center;
                width: 155px;
                padding: 10px 0;
                margin-bottom: 10px;
                background-color: white;
                color: black !important;
                font-weight: bold !important;
                border-radius: 12px;
                border: 1px solid #454545;
                cursor: pointer;
                transition: all 0.2s ease;
            }

            div[role="radiogroup"] label:hover {
                background-color: #A6A6A6;
                border-color: #525252;
                color: black !important;
            }

            div[role="radiogroup"] label div {
                color: black !important;
                font-weight: bold !important;
            }

        </style>
    """, unsafe_allow_html=True)

    st.sidebar.title("Proyecto PPV1")
    opcion = st.sidebar.radio("Bienvenid@", ["A cerca de mí", "Conocimientos", "Proyectos", "Contacto"])

    if opcion == "A cerca de mí":
        st.subheader("Home")
        st.write("")

    elif opcion == "Proyectos":
        st.subheader("Proyectos")
        st.write("")

    elif opcion == "Contacto":
        st.subheader("Contacto")
        st.write("")
    elif opcion == "Conocimientos":
        st.subheader("Conocimientos")
        st.write("")
    else:
        st.subheader("Home")
        st.write("")