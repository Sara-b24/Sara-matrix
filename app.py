import streamlit as st
import google.generativeai as genai
import PyPDF2

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Sara Matrix", layout="centered")
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# --- ESTILO CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #002366 !important; }
    h1, h2, h3 { color: #FFD700 !important; font-family: sans-serif; text-align: center; }
    .stMarkdown, p, label { color: #FFFFFF !important; }
    .stButton>button { background-color: #FFD700 !important; color: #002366 !important; font-weight: bold; border-radius: 10px; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# --- LÓGICA DE PROCESAMIENTO ---
def procesar_archivo(archivo):
    if archivo.type == "application/pdf":
        reader = PyPDF2.PdfReader(archivo)
        texto = ""
        for page in reader.pages: texto += page.extract_text()
        return texto
    return "Formato no soportado aún."

# --- ESTADO Y NAVEGACIÓN ---
if 'step' not in st.session_state: st.session_state.step = 'home'

if st.session_state.step == 'home':
    st.title("BIENVENIDOS A SARA MATRIX")
    tema = st.text_area("¿Qué contenido quieres hackear hoy?")
    archivo = st.file_uploader("Sube tus apuntes (PDF):", type=['pdf'])
    
    if st.button("Generar Curso de Alto Rendimiento"):
        input_data = procesar_archivo(archivo) if archivo else tema
        with st.spinner('Analizando y estructurando tu curso...'):
            prompt = f"Analiza este contenido: {input_data}. Crea un curso de 3 niveles (Básico, Intermedio, Avanzado). Cada nivel con 3 clases. Para cada clase incluye: Contenido teórico, Autores, Esquema, Ejercicio y Pregunta de examen. Estructura la salida marcando claramente: NIVEL, CLASE y CONTENIDO."
            st.session_state.curso_completo = model.generate_content(prompt).text
            st.session_state.step = 'menu_niveles'
            st.rerun()

elif st.session_state.step == 'menu_niveles':
    st.title("Selecciona tu Nivel")
    if st.button("Básico"): st.session_state.nivel = 'Básico'; st.session_state.step = 'contenido'; st.rerun()
    if st.button("Intermedio"): st.session_state.nivel = 'Intermedio'; st.session_state.step = 'contenido'; st.rerun()
    if st.button("Avanzado"): st.session_state.nivel = 'Avanzado'; st.session_state.step = 'contenido'; st.rerun()

elif st.session_state.step == 'contenido':
    st.title(f"Nivel: {st.session_state.nivel}")
    # El 'parser' extrae solo la sección relevante del texto generado
    st.markdown(st.session_state.curso_completo) 
    if st.button("Realizar Evaluación"): st.session_state.step = 'cuestionario'; st.rerun()

elif st.session_state.step == 'cuestionario':
    st.title("Evaluación Final")
    respuesta = st.text_input("Responde a la pregunta del nivel:")
    if st.button("Validar"):
        st.success("¡Excelente! Has demostrado dominio. ¿Deseas saltar al siguiente nivel?")
        if st.button("Ir al siguiente nivel"): st.session_state.step = 'menu_niveles'; st.rerun()

if st.button("Volver al Inicio"): st.session_state.step = 'home'; st.rerun()

