import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="Sara Matrix", layout="centered")

# Configurar API de Gemini usando los Secrets que ya guardaste
# Esto busca la clave que pusiste en la sección "Secrets" de Streamlit
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# Estilos CSS
st.markdown("""<style>
    .stApp { background-color: #001f5b !important; }
    h1 { color: #FFD700 !important; text-align: center; }
    .stButton>button { background-color: #F8F9FA !important; color: #002366 !important; border-radius: 20px !important; }
</style>""", unsafe_allow_html=True)

st.title("SARA MATRIX: ZONA DE HACKEO")

tema = st.text_area("¿Qué contenido quieres hackear hoy?")

if st.button("Generar Curso de Alto Rendimiento"):
    if tema:
        with st.spinner('Hackeando contenido...'):
            # Llamada a Gemini
            response = model.generate_content(f"Actúa como un profesor experto. Crea un curso de alto rendimiento para el tema: {tema}. Estructura: 1. Fundamentos básicos y autores clave, 2. Aplicaciones prácticas y sugerencia de video educativo, 3. Análisis profundo y esquema conceptual tipo Pinterest.")
            
            st.write("---")
            st.subheader("📊 Estructura de tu Curso")
            st.markdown(response.text)
    else:
        st.warning("Por favor, introduce un tema.")
