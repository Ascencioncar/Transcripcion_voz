from streamlit_mic_recorder import speech_to_text
import streamlit as st

st.title("Asistente de voz")
st.write()

text= speech_to_text(language="es-ES", use_container_width=True, just_once=False, key="SST")

if text:
    st.write("Tu audio subido: " + text)
else:
    st.write("No se ha grabado audio aún")