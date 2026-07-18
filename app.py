import streamlit as st
import google.generativeai as genai
import PyPDF2
import os

# Configuración inicial
st.set_page_config(page_title="Sara Matrix", layout="centered")

# Configuración de la API usando la clave de tus Secrets
# Aquí estamos usando la forma que debería aceptar tu clave actual
api_key = st.secrets["GEMINI_API_KEY"]
os.environ["GOOGLE_API_KEY"] = api_key
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

# Diseño CSS
st.markdown("""
    <style>
    .stApp { background-color: #002366 !important; }
    h1, h2 { color: #FFD700 !important; text-align: center; }
    .stMarkdown, p { color: #FFFFFF !important; }
    .stButton>button { background-color: #FFD700 !important; color: #002366 !important; font-weight: bold; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# Lógica de navegación
if 'step' not in st.session_state: st.session_state.step = 'home'

if st.session_state.step == 'home':
    st.title("BIENVENIDOS A SARA MATRIX")
    tema = st.text_area("¿Qué contenido quieres hackear hoy?")
    archivo = st.file_uploader("Sube tus apuntes (PDF):", type=['pdf'])
    
    if st.button("Generar Curso"):
        if tema or archivo:
            texto_archivo = ""
            if archivo:
                reader = PyPDF2.PdfReader(archivo)
                for page in reader.pages: texto_archivo += page.extract_text()
            
            prompt = f"Analiza: {tema} {texto_archivo}. Crea un curso detallado con 3 niveles (Básico, Intermedio, Avanzado) y 3 clases por nivel. Incluye bibliografía, ejercicios y preguntas."
            try:
                st.session_state.curso = model.generate_content(prompt).text
                st.session_state.step = 'menu'
                st.rerun()
            except Exception as e:
                st.error(f"Error al conectar con la IA: {e}")

elif st.session_state.step == 'menu':
    st.title("Selecciona tu nivel")
    if st.button("Básico"): st.session_state.step = 'contenido'; st.rerun()
    if st.button("Volver al Inicio"): st.session_state.step = 'home'; st.rerun()

elif st.session_state.step == 'contenido':
    st.markdown(st.session_state.curso)
    if st.button("Volver al Menú"): st.session_state.step = 'menu'; st.rerun()
