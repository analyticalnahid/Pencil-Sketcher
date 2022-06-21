import streamlit as st
import numpy as np
from PIL import Image
import cv2

st.title("Pencil Sketcher")

def dodgev2(x, y):
    return cv2.divide(x, 255 - y, scale=256)


def pencilsktech(inp_img):
    img_gray = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
    final_img = dodgev2(img_gray, img_smoothing)
    return(final_img)


file_image = st.sidebar.file_uploader("Upload your photos", type=['jpeg','jpg','PNG'])

if file_image is None:
    st.write("You haven't upload any image")
else:
    input_img = Image.open(file_image)
    final_sketch = pencilsktech(np.array(input_img))
    st.write("**Input Photo**")
    st.image(input_img, use_column_width=True)
    st.write("**Output Pencil Sketch**")
    st.image(final_sketch, use_column_width=True) 
