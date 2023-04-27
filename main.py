# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd

import model.calculadora as model
import view.calculadoraView as view
import controller.calculadoraController as controller

def mostrar_calculadora():
    modelo = model.Calculadora()
    vista = view.CalculadoraView()
    controlador = controller.CalculadoraController(modelo, vista)

    operacion = input("Seleccione la operación (S - suma, R - resta): ")

    if operacion == "S":
        controlador.sumar()
    elif operacion == "R":
        controlador.restar()
    else:
        print("Operación no válida")

def mostrar_GUI():
    st.set_page_config(
        page_title="JaveZOO",
        page_icon="🐅",
        layout="wide",
        menu_items={
            'Get Help': 'https://github.com/300CIS017-Object-Oriented-Programming/git-githubfundamentals-JebUser',
            'About': "Proyecto desarrollado por: Estudiante ABC"
        }
    )

    add_selectbox = st.sidebar

    add_selectbox.header("Evolución del dolar 2023")

    st.header("Cuadro de comparación de los valores en USD")

    with st.container():
        # Creo las 2 columnas de la página
        col1, col2 = st.columns([1, 3])

        # Contenido de la columna 1
        col2.table(pd.DataFrame(
            [["$4,650", "$4,720", "$4,346", "$4,238"], ["$4,789", "$4,965", "$4,147", "$4,620"]],
            index=["Primera quincena", "Segunda quincena"],
            columns=["Enero", "Febrero", "Marzo", "Abril"]
        ))

        # Contenido de la columna 2
        col1.metric(label="Valor promedio", value="$4,650", delta="$0,82")

    with st.container():
        update_button = st.button("Actualizar información")

        if update_button:
            st.success("Se actualizó la información", icon="✅")


if __name__ == "__main__":
    #Para ejecutar el ejemplo de MVC
    #mostrar_calculadora()

    # Para ejecutar el ejemplo Streamlit (ejecutar con el comando streamlit run main.py)
    mostrar_GUI()
