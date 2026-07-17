import streamlit as st

# Configuración de página
st.set_page_config(page_title="Sara Matrix", layout="centered")

# Estilos CSS
st.markdown(
    """
    <style>
        .stApp {
            background-color: #001f5b !important;
        }
        h1 {
            background: linear-gradient(90deg, #FFD700 0%, #FFFACD 25%, #4682B4 70%, #00BFFF 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            filter: drop-shadow(0px 0px 5px rgba(255, 215, 0, 0.7)) drop-shadow(0px 0px 10px rgba(0, 191, 255, 0.5));
            font-family: 'Montserrat', sans-serif !important;
            font-weight: 800 !important;
            text-align: center !important;
            text-transform: uppercase !important;
            font-size: 3em !important;
        }
        .stButton>button {
            background-color: #F8F9FA !important;
            color: #002366 !important;
            border-radius: 20px !important;
            border: 1px solid #D4AF37 !important;
            font-weight: bold !important;
            text-transform: uppercase !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Interfaz
st.title("BIENVENIDOS A SARA MATRIX")
st.markdown("## ⚡ Zona de Hackeo")

tema = st.text_area("¿Qué contenido quieres hackear hoy?")
archivo = st.file_uploader("O sube tu libro/apuntes aquí:")

if st.button("Generar Curso de Alto Rendimiento"):
    if tema or archivo:
        st.write("---")
        st.subheader("📊 Estructura de tu Curso")
        
        with st.expander("Básico: Fundamentos y conceptos clave."):
            st.write("Aquí irá el contenido básico.")
        with st.expander("Intermedio: Aplicaciones prácticas y casos."):
            st.write("Aquí irá el contenido intermedio.")
        with st.expander("Avanzado: Análisis crítico y lógica aplicada."):
            st.write("Aquí irá el contenido avanzado.")
            
        st.write("---")
        st.subheader("📝 Tu Quiz de Nivel")
        st.write("Estamos listos para el reto. Próximamente: Quiz de selección y casos prácticos con calificación 0-20.")
    else:
        st.warning("Por favor, introduce un tema o sube un archivo.")

