import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input("pH",value=6.5)

temperatura = st.number_input("Temperatura (°C)",value=23.0)

   if pH<60 or pH>70:
    st.write("revisar pH")
 elif temperatura <20 or temperatura>25:
 clasificacion=("revisar temperatura")
  else:
clasificacion = ("lote aceptable")

if st.button("Evaluar"):


    st.write(f"Resultado: {resultado}")
