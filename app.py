import numpy as np
import pandas as pd

import pickle 
#loading the model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))
age=[41]
sex=[0]
cp=[1]
trestbps=[105]
chol=[198]
fbs=[0]
restecg=[1]
thalach=[168]
exang=[0]
oldpeak=[0.0]
slope=[2]
ca=[1]
thal=[2]
dic={'age':age, 'sex':sex, 'cp':cp, 'trestbps':trestbps, 'chol':chol, 'fbs':fbs, 'restecg':restecg, 'thalach':thalach, 'exang':exang, 'oldpeak':oldpeak, 'slope':slope, 'ca':ca, 'thal':thal}

df = pd.DataFrame(dic)