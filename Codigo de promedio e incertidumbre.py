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

def calcular_incertidumbre(mediciones, inc_instrumental):
    n = len(mediciones)
    
    # 1. Valor promedio
    promedio = np.mean(mediciones)
    
    # 2. Desviación estándar muestral (s)
    desviacion = np.std(mediciones, ddof=1)
    
    # 3. Error aleatorio (Incertidumbre estadística)
    error_aleatorio = desviacion / np.sqrt(n)
    
    # 4. Error total (Combinación por cuadratura)
    error_total = np.sqrt(error_aleatorio**2 + inc_instrumental**2)
    
    return promedio, error_aleatorio, error_total


# Ejemplo de uso con tus inputs de Streamlit:
# prom, err_a, err_t = calcular_incertidumbre(lista_de_datos, instrumento)