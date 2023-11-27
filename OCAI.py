import streamlit as st
from PIL import Image

import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers

def main():
    st.title('Overcut AI')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        #image classification

        a='model.h5'
        from keras.models import load_model
        x = load_model(a)
    
        test_photo = uploaded_file
        img = cv2.imread(test_photo)
    
        size=(250,250)
        background_color="white"
        resized = cv2.resize(img, size, interpolation = cv2.INTER_AREA)
        print('Resized Dimensions : ',resized.shape)
    
        print(resized.shape)
        img2 = (np.expand_dims(resized,0))
    
        print(img2.shape)
        predictions_single = x.predict(img2)
    
        print(predictions_single)
        if (predictions_single[0][0]>predictions_single[0][1]):
            print('Predicted class is Accident')
        else:
            print('Predicted class is Non Accident')
                #trained model and prediction ends
    else:
        st.info('Please upload an image.')

if __name__ == '__main__':
    main()
