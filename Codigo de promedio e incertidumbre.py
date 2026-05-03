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

# --- PRIMERA FILA DE FÓRMULAS ---
col_f1, col_f2 = st.columns(2)

with col_f1:
    st.success("**Valor Promedio ($\overline{x}$):**")
    st.latex(r"\overline{x} = \frac{\sum_{i=1}^{n} x_i}{n}")
    st.write("""
    Es la media aritmética de todas tus mediciones. Representa el valor más probable 
    dentro del conjunto de datos y sirve como base central para el cálculo de 
    cualquier tipo de desviación o error posterior.
    """)

with col_f2:
    st.success("**Desviación Estándar ($s$):**")
    st.latex(r"s = \sqrt{\frac{\sum (x_i - \overline{x})^2}{n-1}}")
    st.write("""
    Mide qué tan alejados están los datos respecto al promedio. Una desviación 
    baja indica que los datos están muy agrupados (alta precisión), mientras 
    que una alta sugiere gran dispersión en las medidas tomadas.
    """)

# --- SEGUNDA FILA DE FÓRMULAS ---
col_f3, col_f4 = st.columns(2)

with col_f3:
    st.success("**Error Aleatorio ($e_a$):**")
    st.latex(r"e_a = \frac{s}{\sqrt{n}}")
    st.write("""
    También llamado error de la media, cuantifica la incertidumbre debida a 
    factores ambientales o humanos. Disminuye a medida que aumentas el número 
    de mediciones ($n$), mejorando la confianza del experimento.
    """)

with col_f4:
    st.success("**Error Total Combinado ($e_t$):**")
    st.latex(r"e_t = \sqrt{e_a^2 + e_i^2}")
    st.write("""
    Es la incertidumbre final del proceso. Combina el error aleatorio con la 
    apreciación del instrumento ($e_i$) mediante cuadratura, entregando el 
    margen de error absoluto que se debe reportar en el informe.
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