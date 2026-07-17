import streamlit as st

# Configuración de página con colores Sara Matrix
st.set_page_config(page_title="Sara Matrix", page_icon="⚡")

st.markdown(
    """
    <style>
                /* 1. Fondo Azul Real Profundo y Brillante (forzado) */
        .stApp {
            background-color: #001f5b !important; /* Un azul real más vibrante para el fondo */
        }

            background-color: #002366; /* Un azul real profundo */
            color: white; /* Texto general en blanco para que resalte */
        }

                /* 2. Título Principal Intenso y Metálico */
        h1 {
            /* Colores de degradado más saturados e intensos */
            background: linear-gradient(90deg, #FFD700 0%, #FFFACD 25%, #4682B4 70%, #00BFFF 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            
            /* Sombra/Resplandor para efecto metálico e iluminación */
            filter: drop-shadow(0px 0px 5px rgba(255, 215, 0, 0.7)) 
                    drop-shadow(0px 0px 10px rgba(0, 191, 255, 0.5));
            
            font-family: 'Poppins Bold', sans-serif !important;
            font-weight: 800 !important;
            text-align: center !important;
            text-transform: uppercase !important;
            font-size: 3em !important;
            padding-bottom: 10px !important;
            margin-bottom: 0px !important;
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

                /* 5. Estilo para el botón "Generar Curso" - Blanco Sutil */
        .stButton>button {
            background-color: #F8F9FA !important; /* Un blanco muy suave (casi gris perla) */
            color: #002366 !important; /* Azul profundo para que las letras resalten sobre el fondo claro */
            border-radius: 20px !important;
            border: 1px solid #D4AF37 !important; /* Un borde dorado muy fino y elegante */
            font-weight: bold !important;
            font-size: 1.1em !important;
            text-transform: uppercase !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2) !important;
            transition: all 0.3s ease !important;
        }
        
        /* Efecto al pasar el mouse por el botón */
        .stButton>button:hover {
            background-color: #E2E6EA !important; /* Un gris muy clarito al pasar el mouse */
            border-color: #FFD700 !important;
            color: #002366 !important;
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
        # Botones para los niveles
with st.expander("Básico: Fundamentos y conceptos clave."):
    st.write("Aquí irá el contenido básico.")

with st.expander("Intermedio: Aplicaciones prácticas y casos."):
    st.write("Aquí irá el contenido intermedio.")

with st.expander("Avanzado: Análisis crítico y lógica aplicada."):
    st.write("Aquí irá el contenido avanzado.")

    st.write("---")
    st.subheader("Tu Quiz de Nivel")
    st.write("Estamos listos para el reto. Próximamente: Quiz de selección y casos prácticos con calificación 0-20.")
else:
    st.warning("Por favor, introduce un tema o sube un archivo.")
