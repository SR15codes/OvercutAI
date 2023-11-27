import streamlit as st
from PIL import Image

def main():
    st.title('Film Club - Image Uploader')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
    else:
        st.info('Please upload an image.')

if __name__ == '__main__':
    main()
