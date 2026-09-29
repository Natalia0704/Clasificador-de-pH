import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input("pH",value=6.5)

temperatura = st.number_input("Temperatura (°C)",value=23.0)
if st.button("Evaluar"):
   if pH<6 or pH>7:
    st.write("revisar pH")
   else:
    st.write(" pH adecuado")
      if pH > = 6 and pH <7
      st.write ("pH adecuado")
      
   

