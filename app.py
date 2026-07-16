import streamlit as st

# Configuración de página con colores Sara Matrix
st.set_page_config(page_title="Sara Matrix", page_icon="⚡")

st.markdown("""
    <style>
    .main { background-color: #050505; color: #D4AF37; }
    h1 { color: #D4AF37; text-align: center; }
    h2 { color: #D4AF37; text-align: center; }
    .stButton>button { background-color: #001A33; color: #D4AF37; border: 2px solid #D4AF37; }
    </style>
    """, unsafe_allow_html=True)

st.title("Bienvenidos a Sara Matrix")
st.markdown("## ⚡ Zona de Hackeo")

tema = st.text_area("¿Qué contenido quieres hackear hoy?")
archivo = st.file_uploader("O sube tu libro/apuntes aquí:")

if st.button("Generar Curso de Alto Rendimiento"):
    if tema or archivo:
        st.write("---")
        st.subheader("📊 Estructura de tu Curso")
        st.info("Básico: Fundamentos y conceptos clave.")
        st.info("Intermedio: Aplicaciones prácticas y casos.")
        st.info("Avanzado: Análisis crítico y lógica aplicada.")
        
        st.write("---")
        st.subheader("📝 Tu Quiz de Nivel")
        st.write("Estamos listos para el reto. Próximamente: Quiz de selección y casos prácticos con calificación 0-20.")
    else:
        st.warning("Por favor, introduce un tema o sube un archivo para empezar.")
