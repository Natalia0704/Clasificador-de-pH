import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input("pH",value=6.5)

temperatura = st.number_input("Temperatura (°C)",value=23.0)
if st.button("Evaluar"):
   if pH<6 or pH>7:
    st.write("revisar pH")
   else:
    st.write(" pH adecuado")
   if temperatura < 20 or temperatura >25:
      st.write ("revisar temperatura")
   else:
      st.write("lote aceptable")
      
   st.sidebar.title("medidor de pH")
   st.sidebar.write("Natalia Espino Valles")

