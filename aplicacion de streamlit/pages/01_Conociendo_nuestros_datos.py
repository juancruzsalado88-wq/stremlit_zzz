import pandas as pd
import streamlit as st

# index_col=0 usa la primera columna (el número de fila) como índice
felinos = pd.read_csv("felinos_filtrado.csv", index_col=0)

st.title("Parte 1")
st.header("Datos que encontraron")

with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = felinos.shape
    st.write(f"Tiene {filas} filas y {columnas} columnas")

with st.expander("¿Cuáles son los nombres de las columnas?"):
    st.write(felinos.columns)

with st.expander("¿Cuántos son los valores únicos de la columna **species**?"):
    st.write(felinos["species"].nunique())

with st.expander("¿Cuáles son los valores únicos de la columna **species**?"):
    st.write(felinos["species"].unique())

with st.expander("¿Cuál es la especie con más avistamientos y la que menos tiene?"):
    por_especie = felinos["species"].value_counts()
    st.write(por_especie)
    st.write(
        f"La especie con más avistamientos es **{por_especie.idxmax()}** ({por_especie.max()}) "
        f"y la que menos tiene es **{por_especie.idxmin()}** ({por_especie.min()})."
    )

with st.expander("¿Cuántos avistamientos hay de la especie Puma concolor?"):
    puma = felinos[felinos["species"] == "Puma concolor"]
    st.write(f"Hay {len(puma)} avistamientos de Puma concolor.")

with st.expander("¿Cuántos avistamientos hay de Panthera onca por provincia?"):
    panthera = felinos[felinos["species"] == "Panthera onca"]
    por_prov = panthera["stateProvince"].value_counts()
    st.write(f"Hay {len(panthera)} avistamientos en total.")
    st.write(por_prov)
    st.write(f"La provincia con más avistamientos es **{por_prov.idxmax()}** ({por_prov.max()}).")
    st.caption(f"{panthera['stateProvince'].isna().sum()} registros no tienen provincia.")

with st.expander("¿Cuál es la provincia con menos avistamientos?"):
    provincias = felinos["stateProvince"].value_counts()
    menos = provincias[provincias == provincias.min()]
    st.write(provincias)
    st.write(
        f"Las provincias con menos avistamientos ({provincias.min()} cada una) son: "
        + ", ".join(menos.index) + "."
    )
    st.caption("«Neuquen» y «Santa cruz» parecen errores de escritura de «Neuquén» y «Santa Cruz».")

with st.expander("¿Cuál fue el año del primer y del último avistamiento?"):
    st.write(
        f"El primer avistamiento fue en {int(felinos['year'].min())} "
        f"y el último en {int(felinos['year'].max())}."
    )
    st.caption(f"{felinos['year'].isna().sum()} registros no tienen fecha.")

with st.expander("Muestra de los datos"):
    st.dataframe(felinos.head(20))
