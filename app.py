import streamlit as st
import google.generativeai as genai
import PyPDF2
import os

# Configuración inicial
st.set_page_config(page_title="Sara Matrix", layout="wide")

# Configuración de la API
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Estilo visual (Black & Gold)
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3 { color: #FFD700; text-align: center; }
    .stMarkdown, p, div { color: #FFFFFF; }
    .stButton>button { background-color: #FFD700; color: #000000; font-weight: bold; border-radius: 10px; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# Lógica de estados
if 'curso' not in st.session_state: st.session_state.curso = None

st.title("SARA MATRIX")
st.subheader("Zona de Hackeo")

tema = st.text_area("Ingresa el tema a investigar:")
archivo = st.file_uploader("Sube tus apuntes (PDF):", type=['pdf'])

if st.button("GENERAR ESTRUCTURA TOTAL"):
    if tema or archivo:
        texto_pdf = ""
        if archivo:
            reader = PyPDF2.PdfReader(archivo)
            for page in reader.pages: texto_pdf += page.extract_text()
        
        prompt = f"""
        Actúa como una experta académica. Basado en este tema: '{tema}' y este texto: '{texto_pdf[:5000]}', 
        crea una estructura de curso completa con:
        1. Tres niveles: Básico, Intermedio, Avanzado.
        2. Tres clases por nivel con objetivos claros.
        3. Para cada clase: ejercicios prácticos y preguntas de repaso.
        4. Sugerencias de videos de YouTube, mapas mentales y esquemas.
        5. Formato de estilo 'Pinterest' (usando emojis y viñetas visuales).
        """
        
        try:
            with st.spinner("Sincronizando con el Matrix..."):
                response = model.generate_content(prompt)
                st.session_state.curso = response.text
        except Exception as e:
            st.error(f"Error técnico: {e}")

if st.session_state.curso:
    st.markdown("---")
    st.markdown(st.session_state.curso)
    if st.button("Limpiar pantalla"):
        st.session_state.curso = None
        st.rerun()
