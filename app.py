import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Sara Matrix", layout="centered")
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# --- CSS (Diseño Azul/Dorado sin degradados) ---
st.markdown("""
    <style>
    .stApp { background-color: #002366 !important; }
    h1, h2, h3 { color: #FFD700 !important; font-family: sans-serif; text-align: center; }
    .stMarkdown, p { color: #FFFFFF !important; }
    .stButton>button { background-color: #FFD700 !important; color: #002366 !important; font-weight: bold; border-radius: 10px; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# --- ESTADO DE LA APLICACIÓN ---
if 'step' not in st.session_state: st.session_state.step = 'home'

# --- PÁGINA 1: INICIO ---
if st.session_state.step == 'home':
    st.title("BIENVENIDOS A SARA MATRIX")
    st.subheader("⚡ Zona de Hackeo")
    tema = st.text_area("¿Qué contenido quieres hackear hoy?")
    archivo = st.file_uploader("Sube tus apuntes/libros:", type=['pdf', 'txt'])
    
    if st.button("Generar Curso de Alto Rendimiento"):
        if tema:
            with st.spinner('Procesando tu matrix de conocimiento...'):
                # Aquí Gemini estructura los niveles y clases
                st.session_state.curso = model.generate_content(f"Crea un curso estructurado de {tema}. Define 3 niveles (Básico, Intermedio, Avanzado). Para cada nivel define 3 clases. Incluye autores, bibliografía, ejercicios y una pregunta de selección simple para cada clase.")
                st.session_state.step = 'menu_niveles'
                st.rerun()
        else: st.warning("Por favor, ingresa un tema.")

# --- PÁGINA 2: SELECCIÓN DE NIVEL ---
elif st.session_state.step == 'menu_niveles':
    st.title("Niveles Disponibles")
    col1, col2, col3 = st.columns(3)
    if col1.button("Básico"): st.session_state.nivel = 'Básico'; st.session_state.step = 'lista_clases'; st.rerun()
    if col2.button("Intermedio"): st.session_state.nivel = 'Intermedio'; st.session_state.step = 'lista_clases'; st.rerun()
    if col3.button("Avanzado"): st.session_state.nivel = 'Avanzado'; st.session_state.step = 'lista_clases'; st.rerun()

# --- PÁGINA 3: LISTA DE CLASES ---
elif st.session_state.step == 'lista_clases':
    st.title(f"Nivel: {st.session_state.nivel}")
    st.write("Selecciona una clase para comenzar:")
    # Botones dinámicos para las clases
    for i in range(1, 4):
        if st.button(f"Clase {i}: Título de la Clase"):
            st.session_state.clase_actual = i
            st.session_state.step = 'contenido_clase'
            st.rerun()

# --- PÁGINA 4: CONTENIDO Y EVALUACIÓN ---
elif st.session_state.step == 'contenido_clase':
    st.title(f"Clase {st.session_state.clase_actual}")
    st.markdown("### Contenido de la clase, autores, videos y esquema tipo Pinterest...")
    
    if st.button("Finalizar clase y realizar cuestionario"):
        st.session_state.step = 'cuestionario'
        st.rerun()

elif st.session_state.step == 'cuestionario':
    st.title("Evaluación de Clase")
    st.write("Pregunta de selección simple:")
    opcion = st.radio("¿Qué aprendiste?", ["Opción A", "Opción B", "Opción C"])
    
    if st.button("Confirmar Respuesta"):
        st.success("Correcto: Justificación detallada.")
        if st.button("Ir a siguiente clase"):
            st.session_state.clase_actual += 1
            st.session_state.step = 'contenido_clase'
            st.rerun()

# --- BOTÓN RETORNO ---
if st.session_state.step != 'home':
    if st.button("Volver al Menú Principal"):
        st.session_state.step = 'home'
        st.rerun()
