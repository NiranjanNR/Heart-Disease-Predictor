import numpy as np
import pandas as pd
import pickle
import streamlit as st

#loading the model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

#creating a prediciton function
def pred(input_data):
    inp = np.array(input_data)
    op = inp.reshape(1,-1)
    df = pd.DataFrame(op, columns = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'])
    prediction = loaded_model.predict(df)
    print(prediction)
    if (prediction[0]==1):
        return "Heart disease detected"
    else:
        return "No heart disease detected"
    
def main():
    st.title("See if You have Heart Disease")
    
    age = st.text_input("Your Age")
    sex	= st.text_input("Your Sex")
    cp	= st.text_input("Chest pain type (0:Typical angina ,1: Atypical angina ,2: Non-anginal pain ,3: Asymptomatic) ")
    trestbps = st.text_input("Your resting blood pressure")
    chol = st.text_input("Your serum cholestoral in mg/dl")
    fbs	= st.text_input("Your fasting blood sugar ")
    restecg	= st.text_input("Your resting electrocardiographic results")
    thalach	= st.text_input("Your maximum heart rate achieved")
    exang = st.text_input("Your exercise induced angina")
    oldpeak	= st.text_input("Your oldpeak")
    slope = st.text_input("Your slope of the peak exercise ST segmen")
    ca	= st.text_input("Number of major vessels (0-3) colored by flourosopy")
    thal = st.text_input("Thalium stress result")

    #code for prediction
    diagnosis = ''

    #button for prediction

    if st.button('Heart Disease Result'):
        diagnosis = pred([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])


    st.success(diagnosis)

if __name__ == '__main__':
    main()