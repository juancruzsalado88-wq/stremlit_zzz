import streamlit as st

st.image('images/banner.png')

st.title("Análisis de Datos en la Facultad de Informática")
st.subheader("Con Python🐍")
st.write("¿Qué sabemos de los felinos de Argentina? 🐆")
st.write(
    "En esta aplicación exploramos un dataset de registros de **felinos silvestres "
    "observados en Argentina** (pumas, yaguaretés, ocelotes, gatos monteses, etc.), "
    "con datos como la especie, la provincia, la ubicación (latitud y longitud), "
    "la altura y la fecha del avistamiento."
)
st.write("Usá el menú de la izquierda para navegar por las páginas: "
         "conocer los datos, ver gráficos y explorar mapas.")
