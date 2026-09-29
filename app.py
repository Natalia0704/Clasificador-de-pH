import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input("pH", value=6.5)
temperatura = st.number_input("Temperatura (°C)", value=23.0)

if st.button("Evaluar"):
    
    if pH < 6 or pH > 7:
        st.write("Revisar pH")
    else:
        st.write("pH adecuado")
        
    
    if temperatura < 20 or temperatura > 30:
        st.write("Revisar temperatura")
    else:
        st.write("Temperatura adecuada")
st.sidebar.title("medidor de pH")
st.sidebar.write("Natalia Espino Valles")
st.sidebar.write("3-O")
st.sidebar.write("Facultad de ciencias Quimicas")
