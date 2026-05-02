# Calcular una progresión aritmética
import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    .titulo {
        text-align: center !important; 
        color: #0000FF !important;   
        font-family: 'Trebuchet MS', sans-serif !important; 
        font-size: 55px !important;   
        font-weight: bold !important; 
        text-shadow: 2px 2px 4px #cccccc !important; 
        margin-bottom: 30px !important;
    }
    </style>
    <h1 class="titulo">Progresión Aritmética</h1>
    """, unsafe_allow_html=True)

col_image, col_text = st.columns([1, 1])

with col_image: 
     url_directa = "https://www.canalipe.gob.pe/sites/default/files/web/users/user1743/apoyo_progresion_aritmetica-02.jpg"
     st.image(url_directa, width="stretch", caption="Ejemplo de progresión aritmética")

with col_text:
        st.header("¿Qué es exactamente?")
        
        st.write("""
        Una **progresión aritmética** es una sucesión numérica en la que la diferencia entre dos términos 
        consecutivos es siempre constante. A esta cantidad constante se le denomina **diferencia común** ($d$).
        
        A diferencia de las progresiones geométricas (donde se multiplica), aquí la progresión crece o decrece 
        de forma **lineal**. Es la base para entender conceptos más avanzados como el cálculo de intereses simples 
        o la velocidad constante en física.
        """)

st.divider() # Una línea para separar

st.markdown("<h3 style='color: #1E90FF;'>Fórmulas clave para progresiones aritméticas</h3>", unsafe_allow_html=True)

col_f1, col_f2 = st.columns(2)

with col_f1:
    st.info("**Término General ($a_n$):**")
    st.latex(r"a_n = a_1 + (n - 1) \cdot d")
    st.write("""
    Esta fórmula te permite saltar directamente a cualquier posición sin pasar por todos los números anteriores. Es útil para saber, por ejemplo, cuál será el valor en la posición 1,000.
    """)

with col_f2:
    st.info("**Cantidad de términos ($n$):**")
    st.latex(r"n = \frac{a_n - a_1}{d} + 1")
    st.write("""
    Esta es la que usamos en este programa. Nos indica cuántos números existen exactamente entre el inicio y el final basándonos en la diferencia constante que hayas elegido.
    """)

# --- SEGUNDA FILA ---
col_f3, col_f4 = st.columns(2)

with col_f3:
    st.info("**Suma de los n términos ($S_n$):**")
    st.latex(r"S_n = \frac{(a_1 + a_n) \cdot n}{2}")
    st.write("""
    Permite calcular el total acumulado de todos los valores de la serie sin sumarlos uno por uno. Es una herramienta fundamental para proyecciones financieras y ahorro progresivo.
    """)

with col_f4:
    st.info("**Diferencia Común ($d$):**")
    st.latex(r"d = a_n - a_{n-1}")
    st.write("""
    Es el valor constante que se suma en cada paso de la sucesión. Se obtiene restando cualquier término menos el anterior y define si la progresión es creciente o decreciente.
    """)

# --- TERCERA FILA ---
col_f5, col_f6 = st.columns(2)

with col_f5:
    st.info("**Media Aritmética:**")
    st.latex(r"a_k = \frac{a_{k-1} + a_{k+1}}{2}")
    st.write("""
    Establece que cualquier término intermedio es el promedio exacto de sus vecinos inmediatos. Es una propiedad única que ayuda a validar la consistencia de toda la serie numérica.
    """)

with col_f6:
    st.info("**Interpolación Lineal ($d$):**")
    st.latex(r"d = \frac{b - a}{k + 1}")
    st.write("""
    Se usa para insertar una cantidad específica de números ($k$) entre dos extremos ($a$ y $b$). Calcula la diferencia necesaria para que todos los nuevos términos queden equitativos.
    """)

st.divider() # Una línea para separar

st.markdown("""
    <style>
    /* 1. Etiquetas en AZUL y NEGRITA */
    label p {
        color: #0000FF !important; /* Azul */
        font-weight: bold !important;
        font-size: 16px !important;
    }
    
    /* 2. DISEÑO DE BARRAS: Solo laterales, fondo gris */
    .stNumberInput > div > div > div:first-child {
        border-left: 3px solid #000000 !important;
        border-right: 3px solid #000000 !important;
        border-top: none !important;
        border-bottom: none !important;
        background-color: #F0F2F6 !important;
        border-radius: 0px !important;
    }

    /* 3. ELIMINAR EL BORDE ROJO AL HACER CLIC (Focus) */
    [data-testid="stNumberInputContainer"]:focus-within {
        border: none !important;
        box-shadow: none !important;
    }
    
    /* Aseguramos que las barras se mantengan negras al escribir */
    .stNumberInput:focus-within > div > div > div:first-child {
        border-left: 3px solid #000000 !important;
        border-right: 3px solid #000000 !important;
    }

    /* 4. LIMPIEZA GENERAL */
    [data-testid="stNumberInputContainer"] {
        border: none !important;
        background-color: transparent !important;
    }

    .stNumberInput input {
        border: none !important;
        background-color: transparent !important;
        font-weight: bold !important;
        color: #000000 !important;
    }

    /* Botones fuera */
    button[data-testid="stNumberInputStepDown"], 
    button[data-testid="stNumberInputStepUp"] {
        border: none !important;
        background-color: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h3 style='color: #000000;'>Simulador de Progresión</h3>", unsafe_allow_html=True)

def mi_progresion(inicial, final, diferencia):
    i = inicial
    while i < final:
        st.write(i)
        i += diferencia
    return i

inicial = st.number_input("Ingrese el numero inicial: ", value=0.1)
final = st.number_input("Ingrese el numero final: ", value=0.1)
diferencia = st.number_input("Ingrese la diferencia: ", value=0.1)

st.markdown("<h4 style='color: #000000;'>Los números en la progresión son:</h4>", unsafe_allow_html=True)
mi_progresion(inicial, final, diferencia)
st.write("En total hay",(final - inicial) // diferencia, "numeros en la progresion")
