'''
1.Train Model
2. Webapp create in flask
3. commit code in github
4. Create Heroku AC (PAAS)
5. Link Git to Heroku
6. Deploy the model
Web app ready
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

'''
import os
os.chdir("C:\\Users\\kunjeshparekh\\Desktop\\KP\\App_Flask")
'''
dataset=pd.read_excel("Heart_Disease_1.xlsx")#, engine='python')
dataset.info()
X_train=dataset.iloc[:,:4]
y_train=dataset.iloc[:,-1]
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(class_weight="balanced")
lr.fit(X_train,y_train)

pickle.dump(lr,open('model.pkl','wb'))

#y_pred = lr.predict(X_train)
model=pickle.load(open('model.pkl','rb'))
model.predict([[60,70,80,90]])

'''
If you locally want to chech the app go to->Anaconda prompt
then change the directory by

command 1
cd C:\Users\kunjeshparekh\Desktop\KP\App_Flask
command 2
python App.py

Then copy url and check the app
'''