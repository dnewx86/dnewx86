import streamlit as st

from ppv1_portafolio.conf_rutas import LOGO_URL, NO_IMAGEN_URL
from ppv1_portafolio.utils import email_valido

def pagina_acercade():
    st.title("🧑 A cerca de mí")

    col1, col2 = st.columns([1,3])
    
    with col1:
        st.image(LOGO_URL)
    
    with col2:
        st.subheader("Proyecto PPV1")
        
        st.write("""
            Por: D' New x86
            
            Bienvenid@ a mi portafolio.
            Estoy iniciando en el mundo del análisis de datos con un enfoque en tecnologías de código abierto.
            
            Puedes encontrarme en mis redes sociales:
        """)

        st.markdown("""
            <style>
                .social-button {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    width: 155px;
                    padding: 10px 0;
                    margin: 5px;
                    background-color: white;
                    color: black !important;
                    border-radius: 12px;
                    border: 1px solid #454545;
                    cursor: pointer;
                    text-decoration: none !important;
                    transition: all 0.2s ease;
                }

                .social-button:hover {
                    background-color: #A6A6A6;
                    border-color: #525252;
                    color: black !important;
                }
            </style>
        """, unsafe_allow_html=True)
                
        st.markdown("""
            <div style="display:flex; gap:10px;">
                <a href="https://github.com/dnewx86" class="social-button" target="_blank">🐱 GitHub</a>
                <a href="https://instagram.com/dnewx86" class="social-button" target="_blank">📷 Instagram</a>
                <a href="https://www.tiktok.com/@dnewx86" class="social-button" target="_blank">♪ TikTok</a>
            </div>
        """, unsafe_allow_html=True)


def pagina_conocimientos():
    st.title("📚 Conocimientos")

    st.subheader('Tecnologías')

    st.markdown("""
        <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
        <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
        <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" />
        <br><br>
    """, unsafe_allow_html=True)
    
    st.subheader('Cursos y certificaciones')

    st.subheader('Otros')


def pagina_proyectos():
    st.title("💼 Proyectos")

    f1_col1, f1_col2, f1_col3 = st.columns(3)

    with f1_col1:
        st.image(NO_IMAGEN_URL)
        st.write("PROYECTO 1")
        st.write("Descripcion ....")

    with f1_col2:
        st.image(NO_IMAGEN_URL)
        st.write("PROYECTO 2")
        st.write("Descripcion ....")
    
    with f1_col3:
        st.image(NO_IMAGEN_URL)
        st.write("PROYECTO 3")
        st.write("Descripcion ....")


def pagina_contacto():
    st.title("✉️ Contacto")

    st.markdown("""
<style>

div[data-testid="stForm"] button {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 155px;
    padding: 10px 0;
    margin: 5px;
    background-color: white;
    color: black !important;
    border-radius: 12px;
    border: 1px solid #454545;
    cursor: pointer;
    transition: all 0.2s ease;
}

div[data-testid="stForm"] button:hover {
    background-color: #A6A6A6;
    border-color: #525252;
    color: black !important;
}

</style>
""", unsafe_allow_html=True)

    with st.form("Envíame un mensaje"):
        nombre = st.text_input("Nombre *")
        email = st.text_input("Correo electrónico *")
        mensaje = st.text_area("Mensaje *")

        enviar = st.form_submit_button("Enviar")

    if enviar:
        if not nombre or not email or not mensaje:
            st.error("Todos los campos son obligatorios.")

        if not email_valido(email):
            st.error("Coloque un correo electrónico valido!")

        else:
            st.success("Formulario enviado correctamente.")
            st.write("Nombre:", nombre)
            st.write("Email:", email)
            st.write("Mensaje:", mensaje)




def pagina_atribuciones():
    st.title("📝 Atribuciones")

    st.markdown("""
        <a href="https://www.flaticon.com/free-icons/picture" title="picture icons">Picture icons created by Pixel perfect - Flaticon</a>
    """, unsafe_allow_html=True)
    