import streamlit as st
import pandas as pd
import altair as alt

st.header("Lieblingswetter der Deutschen")
st.subheader("")

source = pd.DataFrame({
        'Anteil(%)': [7, 3, 70, 6, 8, 6],
        'Wetter': ['Schnee', 'Regen', 'Sonne', 'Gewitter', 'Ein anderes Wetter', 'Weiß nicht']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Wetter:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n=3273; 2023; in Deutschland
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: YouGov")