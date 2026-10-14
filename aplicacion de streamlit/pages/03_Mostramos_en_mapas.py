import folium
import streamlit as st
from streamlit_folium import st_folium
import pandas as pd


def generar_mapa():
    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )
    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=4,
        name='es',
        tiles=tiles,
        attr=attr
    )
    return m


felinos = pd.read_csv('felinos_filtrado.csv', index_col=0)
st.title("Mapa")
mapa = generar_mapa()

# Un color por especie
colores = {
    'Puma concolor': 'orange',
    'Puma yagouaroundi': 'gray',
    'Panthera onca': 'red',
    'Leopardus pardalis': 'green',
    'Leopardus geoffroyi': 'blue',
    'Leopardus guigna': 'purple',
    'Leopardus tigrinus': 'pink',
    'Leopardus wiedii': 'darkgreen',
    'Leopardus pajeros': 'lightblue',
}


def agregar_marca(row):
    anio = '' if pd.isna(row['year']) else f" ({int(row['year'])})"
    folium.Marker(
        [row['lat'], row['lng']],
        popup=f"{row['ScientificName']}{anio}",
        icon=folium.Icon(color=colores.get(row['ScientificName'], 'cadetblue'))
    ).add_to(mapa)


ac1, ac2 = st.columns([0.3, 0.7])

ac1.write("**Especies a mostrar**")
for especie in sorted(felinos['ScientificName'].unique()):
    if ac1.checkbox(especie, key=especie):
        # Máximo 300 marcadores por especie para que el mapa no se ponga lento
        datos = felinos[felinos['ScientificName'] == especie].head(300)
        datos.apply(agregar_marca, axis=1)

with ac2:
    st_folium(mapa, key='felinos', width=700, height=550)
