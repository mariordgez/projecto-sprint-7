import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv(
    "C:\\Users\Mario\\Dev\\projecto-sprint-7\\vehicles_us.csv"
)  # leer los datos
build_histogram = st.checkbox('Construir un histograma') # crear una casilla de verificacion para el histograma
build_dispersion = st.checkbox('Construir una grafica de dispersion') # crear una casilla de verificacion para la grafica de dispersion

if build_histogram: # al hacer clic en la casilla
    # escribir un mensaje
    st.write('Creación de un histograma basandonos en el color del vehiculo asi como en el tipo de vehiculo')
    
    # crear un histograma
    fig = px.histogram(car_data, x="paint_color", labels = {"paint_color": "Pintura del vehiculo"} , color= 'type')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_dispersion: # al hacer clic en la casilla
    # escribir un mensaje
    st.write('Creación de una grafica de dispersion basandonos en la correlacion entre el kilometraje y el precio del vehiculo')
    
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price", labels = {"odometer": "Kilometraje", "price": "Precio"}) # crear un gráfico de dispersión

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
