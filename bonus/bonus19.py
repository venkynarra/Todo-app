import  streamlit as st
from  PIL import Image
with st.expander("start camera"): # camera is hidden under the expander , that is what this line iss.
    uploaded_image = st.file_uploader("Upload Image")
    camera_image = st.camera_input("camera") # this is for starting the camera
    # if wwe not caputure the below code does not run , the capture is MUST
    if camera_image:


        img = Image.open(camera_image) # creating pillow instace , pillow is a library
        gray_img = img.convert("L") # converting the pillow image to grayscale
        st.image(gray_img) # rendering the greyscale

    if uploaded_image:
        img = Image.open(uploaded_image)
        gray_uploaded = img.convert("L")
        st.image(gray_uploaded)