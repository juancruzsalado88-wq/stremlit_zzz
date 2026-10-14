import pandas as pd
import plotly.express as px
import streamlit as st

felinos = pd.read_csv("felinos_filtrado.csv", index_col=0)

st.title("Gráficos")

# 1) Avistamientos por especie (barras)
st.subheader("1) ¿Cuántos avistamientos hay por especie?")
f_s = felinos["species"].value_counts()
fig = px.bar(
    x=f_s.index,
    y=f_s.values,
    labels={"x": "Especie", "y": "Cantidad de avistamientos"},
    title="Cantidad de felinos por especie en gráfico de barra",
)
st.plotly_chart(fig)

# 2) Porcentaje de cada especie (torta)
st.subheader("2) ¿Qué porcentaje representa cada especie?")
fig = px.pie(
    values=f_s.values,
    names=f_s.index,
    title="Porcentaje de cada especie de avistajes",
)
st.plotly_chart(fig)

# 3) Avistamientos por provincia (barras)
st.subheader("3) ¿Qué provincias tienen más avistamientos?")
f_s_p = felinos["stateProvince"].value_counts()
fig = px.bar(
    x=f_s_p.index,
    y=f_s_p.values,
    labels={"x": "Provincia", "y": "Cantidad de avistamientos"},
    title="Cantidad de felinos por provincia en gráfico de barra",
)
st.plotly_chart(fig)

# 6) Especies en Misiones (torta)
st.subheader("4) ¿Cómo están distribuidas las especies en Misiones?")
misiones = felinos[felinos["stateProvince"] == "Misiones"]
especies_misiones = misiones["species"].value_counts()
fig = px.pie(
    values=especies_misiones.values,
    names=especies_misiones.index,
    title="Especies en Misiones",
)
st.plotly_chart(fig)