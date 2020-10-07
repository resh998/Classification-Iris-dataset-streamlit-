# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:31:45 2020

@author: Lenovo
"""


import streamlit as st
import pandas as pd
import pickle

model = open("data//iris.pkl","rb")
classify=pickle.load(model)
iris_data=pd.read_csv("data//iris.csv")

st.title("IRIS FLOWER SPECIES")
st.image("data//iris.jpg",width=750)
nav=st.sidebar.radio("Navigation",["Home","Prediction"])
html_temp = """
       <div>
       <h1>IRIS FLOWER</h1>
       <p style="font-size:150%"><b>Iris</b> is a popular garden flower that takes its name from the Greek word for a rainbow. It is also the name for the Greek goddess of the rainbow, Iris who is the messenger of Love.
       The name refers to the wide variety of flower colors found among the many species. The genus Iris has about 260-300 species and is native to the North Temperate regions of the world. The habitat of irises also varies a lot. Some irises grow in deserts, some in swamps, some in the cold far north, and many in temperate climates. Bearded Iris and Siberian Iris are two of the most common types of irises grown.
       Irises come in many colors such as blue and purple, white and yellow, pink and orange, brown and red, and even black.
       Since Iris is the Greek goddess for the Messenger of Love, the flower is considered as the symbol of communication and messages. Therefore the flower iris in the language of flowers symbolizes eloquence. Based on their color, irises convey varied messages that can be gifted to convey many emotions. A purple iris symbolizes wisdom and compliments where as a blue iris symbolizes faith and hope. A yellow iris symbolizes passion while white iris symbolizes purity.
       </p>
       </div>
       """
st.markdown(html_temp,unsafe_allow_html=True)
st.image('data//iris_images.jpg',width=700)
if nav=="Home":
    if st.checkbox("Show Data"):
        st.table(iris_data)   
            
if nav=="Prediction":
    st.text('if output =0 : IRIS-Setosa')
    st.text('if ouput =1 : IRIS-Versicolor')
    st.text('if output =2 : IRIS-Virginica')
    st.header("Prediction of Species")
    SepalLength=st.text_input("Sepal length")
    SepalWidth=st.text_input("Sepal Width ")
    PetalLength=st.text_input("Petal Length")
    PetalWidth=st.text_input("Petal Width")
    result=""
    if st.button("Predict"):
        result=classify.predict([[SepalLength,SepalWidth,PetalLength,PetalWidth]])
        print(result)
    st.success('The output is {}'.format(result))
        
