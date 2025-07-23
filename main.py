import streamlit as st
import cv2
import easyocr
from PIL import Image
import numpy as np

st.title("AgusVision 🔍")

uploaded_file = st.file_uploader("Subí una imagen", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen cargada", use_column_width=True)

    # Convertir a array de OpenCV
    img_array = np.array(image.convert('RGB'))
    gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

    # OCR con EasyOCR
    reader = easyocr.Reader(['en', 'es'])  # Idiomas configurables
    result = reader.readtext(gray)

    st.write("📝 Texto detectado:")
    for detection in result:
        st.write(f"- {detection[1]}")
