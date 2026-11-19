"""Interfaz Streamlit para la calculadora."""

import streamlit as st

from src.calculator import add, divide, multiply, subtract

st.set_page_config(page_title="Calculadora", page_icon="🧮")
st.title("🧮 Calculadora")

col_a, col_b = st.columns(2)
a = col_a.number_input("Primer número", value=0.0, format="%g", key="a")
b = col_b.number_input("Segundo número", value=0.0, format="%g", key="b")

operaciones = {
    "➕ Sumar": ("+", add),
    "➖ Restar": ("−", subtract),
    "✖️ Multiplicar": ("×", multiply),
    "➗ Dividir": ("÷", divide),
}

columnas = st.columns(len(operaciones))
resultado = None

for col, (etiqueta, (simbolo, funcion)) in zip(columnas, operaciones.items()):
    if col.button(etiqueta, use_container_width=True):
        try:
            resultado = (f"{a:g} {simbolo} {b:g}", funcion(a, b))
        except ValueError:
            st.error("⚠️ No se puede dividir por cero. Cambia el segundo número e inténtalo de nuevo.")

if resultado:
    expresion, valor = resultado
    st.caption(expresion)
    st.markdown(f"<h1 style='text-align:center; font-size:4rem;'>= {valor:g}</h1>", unsafe_allow_html=True)
