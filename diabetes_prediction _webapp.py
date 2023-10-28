# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:06:50 2023

@author: SRI LAVANYA
"""

import numpy as np
import pickle
import streamlit as st


#loading the saved model
loaded_model = pickle.load(open('C:/Users/SRI LAVANYA/Downloads/trained_model.sav','rb'))


#creating a function for prediction
def diabetes_prediction(input_data):
    
    input_data_as_array = np.asarray(input_data)
    input_data1 = input_data_as_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data1)
    print(prediction)
    if prediction[0]==1:
        return 'person having the diabetes'
    else:
        return 'person does not have diabetes'
    
    
    
    
def main():
    
    #giving a title
    st.title('Diabetes prediction web app')
    
    #getting the input data from the user
    
    Pregnancies = st.text_input('enter the number of pregnancies')
    Glucose = st.text_input('enter the glucose level')
    BloodPressure = st.text_input('enter the blood pressure level')
    SkinThickness = st.text_input('enter the skinthickness value')
    Insulin = st.text_input('enter the insulin level')
    BMI = st.text_input('bmi value')
    DiabetesPedigreeFunction = st.text_input('Diabetes pedigree Function value')
    Age = st.text_input('Age of the person')
    
    
    
    #code for prediction
    diagnosis = ''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    