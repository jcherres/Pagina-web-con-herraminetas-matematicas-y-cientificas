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
    st.error("**Ecuación de la Recta ($Y$):**")
    st.latex(r"Y = \beta_0 + \beta_1 X")
    st.write("""
    Es la función lineal que representa la relación entre las variables. Permite predecir el valor de la variable dependiente para cualquier valor de la independiente.
    """)
with col_f2:
    st.error("**Pendiente de la Recta ($\beta_1$):**")
    st.latex(r"\beta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}")
    st.write("""
    Indica la inclinación de la recta. Representa cuánto cambia la variable dependiente por cada unidad que aumenta la variable independiente en el modelo.
    """)

# --- FILA 2 ---
col_f3, col_f4 = st.columns(2)
with col_f3:
    st.error("**Intercepto u Origen ($\beta_0$):**")
    st.latex(r"\beta_0 = \bar{y} - \beta_1 \bar{x}")
    st.write("""
    Es el valor donde la recta corta el eje vertical. Indica el punto de partida del modelo matemático cuando la variable independiente es igual a cero.
    """)
with col_f4:
    st.error("**Coeficiente Determinación ($R^2$):**")
    st.latex(r"R^2 = \frac{[\sum(x - \bar{x})(y - \bar{y})]^2}{\sum(x - \bar{x})^2 \sum(y - \bar{y})^2}")
    st.write("""
    Mide la calidad del ajuste. Un valor cercano a 1 indica que la recta explica casi perfectamente la relación de dependencia entre los puntos de datos analizados.
    """)

# --- FILA 3 ---
col_f5, col_f6 = st.columns(2)
with col_f5:
    st.error("**Error Estándar ($S_{yx}$):**")
    st.latex(r"S_{yx} = \sqrt{\frac{\sum(y_i - \hat{y}_i)^2}{n - 2}}")
    st.write("""
    Cuantifica la desviación promedio de los puntos respecto a la recta. Un error bajo garantiza que las predicciones del simulador sean estadísticamente confiables.
    """)
with col_f6:
    st.error("**Covarianza ($S_{xy}$):**")
    st.latex(r"S_{xy} = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{n - 1}")
    st.write("""
    Mide la dirección de la relación lineal. Si es positiva, ambas variables crecen juntas; si es negativa, una disminuye mientras la otra aumenta sistemáticamente.
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