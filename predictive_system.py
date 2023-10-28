# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle 

#loading the saved model
loaded_model = pickle.load(open('C:/Users/SRI LAVANYA/Downloads/trained_model.sav','rb'))


input_data = np.array([1,189,60,23,846,30.1,0.398,59])
input_data1 = input_data.reshape(1,-1)
prediction = loaded_model.predict(input_data1)
print(prediction)
if prediction[0]==1:
    print('person having the diabetes')
else:
    print('person does not have diabetes')