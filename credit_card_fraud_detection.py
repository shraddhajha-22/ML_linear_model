# -*- coding: utf-8 -*-
"""credit_card_fraud_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gOESEOL18PNbvmxw71kQekeoOZbMaTMf
"""

import numpy as np
import pandas as pd

"""**Data preprocessing and data collection**"""

credit = pd.read_csv('/content/creditcard.csv') # convert csv file into pandas dataframe
credit

credit.head() # shows the first 5 entries of dataset

credit.tail() # shows the first 5 entries of dataset

credit.shape # gives the no of columns and rows

credit.describe() # gives the statistic values of dataset

credit['Class'].value_counts() # gives no of each label present

credit.groupby('Class').mean()

credit.info() # gives the null count and datatype of each column

"""**process to convert unbalanced data into balanced data**

1. separating data into data & labels
"""

legit= credit[credit.Class==0] # 0---> legit transactions
fraud= credit[credit.Class==1] # 0---> fraud transactions

print(legit,fraud)

"""2. calculate all the statistical values for legit and fraud transactions

"""

legit.Amount.describe() # describe statistical values of all legit transaction

fraud.Amount.describe() # describe statistical values of all fraud transaction

"""3. Unsampling : building a sample dataset containing similar distribution of both labels as we can see there is large difference in legit and fraud count thus this highly unbalanced dataset thus we will use undersampling and create a new dataset

"""

legit_sample = legit.sample(n=81)

legit_sample

"""4. concating the both legit_sample and fraud and create a balanced dataset"""

new_credit= pd.concat([legit_sample,fraud],axis=0)
new_credit

"""5. seperating lables and data"""

X= new_credit.drop(columns='Class', axis=1)
Y= new_credit['Class']
print(X,Y)

"""**Training and testing of data**"""

from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=1)

print(X_train,X_test,Y_train,Y_test)

"""**Model training**"""

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train,Y_train)

"""**Accuracy of training data**"""

from sklearn.metrics import accuracy_score

X_train_prediction =model.predict(X_train)
training_accuracy = accuracy_score(X_train_prediction,Y_train)

print(training_accuracy)

"""**predictive system**"""

inputdata= (0,-1.3598071336738,-0.0727811733098497,2.53634673796914,1.37815522427443,-0.338320769942518,0.462387777762292,0.239598554061257,0.0986979012610507,0.363786969611213,0.0907941719789316,-0.551599533260813,-0.617800855762348,-0.991389847235408,-0.311169353699879,1.46817697209427,-0.470400525259478,0.207971241929242,0.0257905801985591,0.403992960255733,0.251412098239705,-0.018306777944153,0.277837575558899,-0.110473910188767,0.0669280749146731,0.128539358273528,-0.189114843888824,0.133558376740387,-0.0210530534538215,149.62)

inpudata_np = np.asarray(inputdata)

inputdata_reshape= inpudata_np.reshape(1,-1)

prediction = model.predict(inputdata_reshape)
print(prediction)
if prediction==0:
  print("the transaction is legitmate")
else:
  print("the transaction is fraudlent")