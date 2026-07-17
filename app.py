import streamlit as st

# Configuración de página con colores Sara Matrix
st.set_page_config(page_title="Sara Matrix", page_icon="⚡")

st.markdown(
    """
    <style>
        /* 1. Fondo Azul Profundo (como el de la foto) */
        .main {
            background-color: #002366; /* Un azul real profundo */
            color: white; /* Texto general en blanco para que resalte */
        }

        /* 2. Estilo para el título principal "BIENVENIDOS A SARA MATRIX" */
        /* Intentamos imitar el degradado Dorado y Azul Metálico de la foto */
        h1 {
            background: linear-gradient(135deg, #FFD700 0%, #D4AF37 30%, #4682B4 70%, #1E90FF 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: 'Montserrat', sans-serif; /* Una fuente elegante y moderna */
            font-weight: 800;
            text-align: center;
            text-transform: uppercase;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5); /* Sombra para dar efecto 3D */
            font-size: 3em !important;
            padding-bottom: 20px;
        }

        /* 3. Estilo para el subtítulo "ZONA DE HACKEO" y el emoji ⚡ */
        /* Usamos el Dorado Brillante de la foto */
        h2 {
            color: #FFD700; /* Oro Puro */
            font-family: 'Cursive', sans-serif; /* Le da un toque más artístico, como las notas musicales */
            font-weight: bold;
            text-align: center;
            text-shadow: 1px 1px 3px rgba(255,215,0,0.5); /* Brillo dorado */
        }

        /* 4. Estilo para los textos de ayuda (como "@saramatrix") */
        /* Usamos el Dorado Suave de la foto */
        p, label, .stMarkdown {
            color: #D4AF37; /* Oro Viejo/Bronce */
            font-family: 'Arial', sans-serif;
        }

        /* 5. Estilo para el botón "Generar Curso" */
        /* Fondo Dorado y Texto Azul Metálico, como el texto de la foto */
        .stButton>button {
            background-color: #FFD700 !important; /* Oro */
            color: #1E1F29 !important; /* Azul muy oscuro para el texto */
            border-radius: 20px;
            border: 2px solid #D4AF37; /* Borde oro viejo */
            font-weight: bold;
            font-size: 1.1em;
            text-transform: uppercase;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            transition: all 0.3s ease;
        }
        
        /* Efecto al pasar el mouse por el botón */
        .stButton>button:hover {
            background-color: #D4AF37 !important; /* Se vuelve un oro más viejo */
            border-color: #FFD700;
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(255,215,0,0.4);
        }

    </style>
    """,
    unsafe_allow_html=True
)


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
