# Calcular el promedio y la incertidumbre de un conjunto de datos
import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    .titulo {
        text-align: center !important; 
        color: #3FD33E !important;   
        font-family: 'Trebuchet MS', sans-serif !important; 
        font-size: 55px !important;   
        font-weight: bold !important; 
        text-shadow: 2px 2px 4px #cccccc !important; 
        margin-bottom: 30px !important;
    }
    </style>
    <h1 class="titulo">Promedio y incertidumbre</h1>
    """, unsafe_allow_html=True)

col_image, col_text = st.columns([1, 1.2])

with col_image: 
     url_directa = "https://i.ytimg.com/vi/ZJ-YCsHCQ4w/sddefault.jpg"
     st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <img src="{url_directa}" style="width:int(350); height: 320px; object-fit: cover; border-radius: 5px;">
        </div>
        <p style="text-align: center; color: gray; font-size: 14px;">Analisis de errores</p>
    """, unsafe_allow_html=True)

with col_text:
    st.header("¿Qué es exactamente?")
    
    st.write("""
    El **promedio** es el valor central de tus medidas, mientras que la **incertidumbre** cuantifica el margen de duda inevitable en cualquier experimento. Ninguna medición es exacta; siempre existe una variación por factores ambientales o humanos. 

    Este programa calcula el **error aleatorio** y el **error total** combinado con la precisión del instrumento. Es una herramienta vital en ingeniería para márgenes de seguridad, en medicina para dosis críticas y en control de calidad para validar resultados de laboratorio.
    """)

st.divider() # Una línea para separar

st.markdown("<h3 style='color: #28a745;'>Fórmulas Clave para promedios y incertidumbres</h3>", unsafe_allow_html=True)

# --- FILA 1 ---
col_f1, col_f2 = st.columns(2)
with col_f1:
    st.success("**Valor Promedio ($\overline{x}$):**")
    st.latex(r"\overline{x} = \frac{\sum_{i=1}^{n} x_i}{n}")
    st.write("""
    Representa el valor más probable de un conjunto de datos. Es la base central para determinar cualquier tipo de desviación o error dentro de un experimento científico.
    """)
with col_f2:
    st.success("**Desviación Estándar ($s$):**")
    st.latex(r"s = \sqrt{\frac{\sum (x_i - \overline{x})^2}{n-1}}")
    st.write("""
    Mide qué tan alejados están los datos respecto al promedio. Una desviación baja indica alta precisión, mientras que una alta sugiere mucha dispersión en las medidas.
    """)

# --- FILA 2 ---
col_f3, col_f4 = st.columns(2)
with col_f3:
    st.success("**Error Aleatorio ($e_a$):**")
    st.latex(r"e_a = \frac{s}{\sqrt{n}}")
    st.write("""
    Cuantifica la incertidumbre debida a factores ambientales o humanos. Este valor disminuye a medida que aumenta el número de mediciones realizadas en el laboratorio.
    """)
with col_f4:
    st.success("**Error Total Combinado ($e_t$):**")
    st.latex(r"e_t = \sqrt{e_a^2 + e_i^2}")
    st.write("""
    Es la incertidumbre final del proceso. Combina el error aleatorio con la apreciación del instrumento mediante cuadratura para entregar el margen de error absoluto real.
    """)

# --- FILA 3 ---
col_f5, col_f6 = st.columns(2)
with col_f5:
    st.success("**Error Relativo ($e_r$):**")
    st.latex(r"e_r = \frac{e_t}{\bar{x}}")
    st.write("""
    Compara la incertidumbre total con el valor promedio medido. Es un valor adimensional que permite evaluar qué tan significativa es la duda respecto al tamaño de la medida.
    """)
with col_f6:
    st.success("**Error Porcentual ($e_{\%}$):**")
    st.latex(r"e_{\%} = e_r \cdot 100")
    st.write("""
    Es el error relativo expresado en porcentaje. Es la forma estándar de reportar la calidad y precisión de un experimento en informes técnicos y artículos de investigación.
    """)

st.divider() # Una línea para separar

st.markdown("""
    <style>
    /* Etiquetas en verde */
    label p { color: #00FF00 !important; font-weight: bold !important; }
    
    /* DISEÑO DE BARRAS: Solo en el cuerpo gris, botones fuera */
    .stNumberInput > div > div > div:first-child, 
    .stTextInput > div > div {
        border-left: 3px solid #000000 !important;
        border-right: 3px solid #000000 !important;
        border-top: none !important;
        border-bottom: none !important;
        background-color:  !important;
        border-radius: 0px !important;
    }

    /* Limpieza total de bordes de Streamlit */
    [data-testid="stNumberInputContainer"], [data-testid="stTextInputContainer"] {
        border: none !important;
        background-color: transparent !important;
        box-shadow: none !important;
    }

    .stNumberInput input, .stTextInput input {
        border: none !important;
        background-color: transparent !important;
        font-weight: bold !important;
    }

    /* Botones invisibles y fuera de las barras */
    button[data-testid="stNumberInputStepDown"], 
    button[data-testid="stNumberInputStepUp"] {
        border: none !important;
        background-color: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown("<h3 style='color: #000000;'>Simulador de promedio y incertidumbre</h3>", unsafe_allow_html=True)



def calcular_promedio_e_incertidumbre(mediciones, inc_instrumental):
    # Validamos que haya al menos dos datos para calcular desviación
    if len(mediciones) < 2:
        return None
    
    n = len(mediciones)
    promedio = np.mean(mediciones)
    desviacion = np.std(mediciones, ddof=1)
    error_aleatorio = desviacion / np.sqrt(n)
    
    # Combinación por cuadratura
    error_total = np.sqrt(error_aleatorio**2 + inc_instrumental**2)
    error_relativo = error_total / abs(promedio) if promedio != 0 else 0
    error_porcentual = error_relativo * 100

    return {
        "prom": promedio,
        "err_a": error_aleatorio,
        "err_t": error_total,
        "err_r": error_relativo,
        "err_p": error_porcentual
    }

# --- INPUTS PARA PROMEDIO E INCERTIDUMBRE ---

datos_usuario = st.text_input("Ingrese las mediciones (ej: 10.2, 10.5, 10.1):", value="10.0, 10.1")
inc_instrumental = st.number_input("Ingrese la incertidumbre del instrumento (Apreciación):", value=0.01, format="%.4f")
unidad = st.text_input("¿En qué unidad se midieron los datos? (ej: m, kg, s):")

# Convertir los datos a lista de números de forma segura
try:
    datos = [float(x.strip()) for x in datos_usuario.split(",") if x.strip()]
except ValueError:
    st.error("Por favor, ingrese solo números separados por comas.")
    datos = []

if len(datos) >= 2:
    res = calcular_promedio_e_incertidumbre(datos, inc_instrumental)
    
    st.markdown("<h4 style='color: #000000;'>El resultado final es:</h4>", unsafe_allow_html=True)
    
    # Formateamos el texto para que salga: Valor ± Incertidumbre Unidad
    texto_resultado = f"{res['prom']:.4f} ± {res['err_t']:.4f} {unidad}"
    
    st.markdown(f"<p class='resultado-texto'>{texto_resultado}</p>", unsafe_allow_html=True)
    
    # Opcional: Mostrar los otros errores abajo en pequeño
    st.write(f"**Error Relativo:** {res['err_r']:.4f} | **Error Porcentual:** {res['err_p']:.2f}%")
else:
    st.warning("Se necesitan al menos 2 mediciones para realizar el cálculo estadístico.")