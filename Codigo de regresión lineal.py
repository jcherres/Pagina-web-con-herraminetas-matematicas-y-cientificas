# Calcular una regresion aritmetica
import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    .titulo {
        text-align: center !important; 
        color: #FF0000 !important;   
        font-family: 'Trebuchet MS', sans-serif !important; 
        font-size: 55px !important;   
        font-weight: bold !important; 
        text-shadow: 2px 2px 4px #cccccc !important; 
        margin-bottom: 30px !important;
    }
    </style>
    <h1 class="titulo">Regresión Lineal</h1>
    """, unsafe_allow_html=True)

col_image, col_text = st.columns([1, 1.2])

with col_image:
    url_directa = "https://d31dn7nfpuwjnm.cloudfront.net/images/valoraciones/0061/1095/Regresi%C3%B3n_lineal4_foro.jpg?1713260485"
    
    # TRUCO: Este código recorta los bordes blancos de la imagen (object-fit: cover)
    st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <img src="{url_directa}" style="width: 100%; height: 320px; object-fit: cover; border-radius: 5px;">
        </div>
        <p style="text-align: center; color: gray; font-size: 14px;">Ejemplo de regresión lineal</p>
    """, unsafe_allow_html=True)

with col_text:
    # Eliminamos el espacio de arriba para que el header suba
    st.markdown("<h2 style='margin-top: 0;'>¿Qué es exactamente?</h2>", unsafe_allow_html=True)
    
    st.write("""
    La **regresión lineal** es un modelo estadístico que busca la relación entre una variable dependiente ($Y$) y una independiente ($X$). A través de este análisis, se intenta determinar cómo el cambio en una variable afecta directamente a la otra.
    """)
    
    st.write("""
    Su objetivo principal es trazar la **recta de mejor ajuste** para predecir valores y entender tendencias futuras. Es una herramienta fundamental en la ciencia de datos para realizar proyecciones precisas basadas en el comportamiento de datos históricos.
    """)

st.divider() # Una línea para separar

st.markdown("<h3 style='color: #F0394D;'> Fórmulas clave para regresiones lineales</h3>", unsafe_allow_html=True)

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

st.divider() # Una línea para separar

st.markdown("""
    <style>
    /* Etiquetas en rojo */
    label p { color: #FF0000 !important; font-weight: bold !important; }
    
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


st.markdown("<h3 style='color: #000000;'>Simulador de Regresión</h3>", unsafe_allow_html=True)


def mi_regresion(inicial, pendiente, tiempo):
    resultado = (pendiente * tiempo) + inicial
    return resultado

inicial = st.number_input("Ingrese el numero inicial: ", value=0.0)
pendiente = st.number_input("Ingrese la pendiente: ", value=0.0)
tiempo = st.number_input("Ingrese el tiempo trascurrido: ", value=0.0)
unidad = st.text_input("¿En qué unidad se mide el resultado?: ")

resultado = mi_regresion(inicial, pendiente, tiempo,)
st.markdown("<h4 style='color: #000000;'>La predicción es de:</h4>", unsafe_allow_html=True)
st.markdown(f"<p class='resultado-texto'>{resultado}</p>", unsafe_allow_html=True)