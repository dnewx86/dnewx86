import streamlit as st


def pagina_acercade():
    st.subheader("A cerca de mí")

    col1, col2 = st.columns([1,3])
    
    with col1:
        st.image("https://raw.githubusercontent.com/dnewx86/dnewx86/main/ppv1_portafolio/img/logo.png")
    
    with col2:
        st.title("Proyecto PPV1")
        
        st.write("""
            Por D' New x86
            
            Bienvenid@ a mi portafolio.
            Estoy iniciando en el mundo del análisis de datos con un enfoque en tecnologías de código abierto.
            Este es un proyecto personal.
            
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
    pass


def pagina_proyectos():
    pass


def pagina_contacto():
    pass