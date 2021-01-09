import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from flask import Flask, request, render_template
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

crops=['wheat','mungbean','Tea','millet','maize','lentil','jute','cofee',
       'cotton','ground nut','peas','rubber','sugarcane','tobacco',
       'kidney beans','moth beans','coconut','blackgram','adzuki beans',
       'pigeon peas','chick peas','banana','grapes','apple','mango',
       'muskmelon','orange','papaya','watermelon','pomegranate']

data=pd.read_csv('crop_dataset.csv')
label=pd.get_dummies(data.label).iloc[:,1:]
data=pd.concat([data,label],axis=1)
data.drop('label',axis=1,inplace=True)

X=data.iloc[:,0:4].values
Y=data.iloc[:,4:].values

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)


sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.fit_transform(X_test)

classifier=KNeighborsClassifier(5)
classifier.fit(X_train,Y_train)

pred=classifier.predict(X_test)
a=accuracy_score(Y_test,pred)

@app.route('/') 
def my_form():
  return render_template('crop.html')

@app.route('/',methods=['POST'])
def my_form_post():
  temp=request.form['temp']
  humidity=request.form['humidity']
  ph=request.form['ph']
  rainfall=request.form['rainfall']
  text=classifier.predict(sc.transform([[temp,humidity,ph,rainfall]]))
  count=0
  for i in range(0,30):
    if(mad[0][i]==1):
        c=crops[i]
        count=count+1
        break;
    i=i+1
  if (count==0):
    print('The predicted crop is %s'%c)
  else:
    print('The predicted crop is %s'%c)
  
  processed_text=c.upper()
  return (processed_text)

if __name__=="__main__":
  app.run()
