# -*- coding: utf-8 -*-
"""sonar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AKQJdGGceG7gmRCTgkcsflaHIa2m4THY
"""

import numpy as np  # used for n dimensional arrays
import pandas as pd # used to perform operations on dataframes

"""data preprocessing

"""

df=pd.read_csv('/sonar.csv', header=None) # reading csv dataset into pandas dataframe

df.describe() # gives statisical information abt dataset

df

df[60].value_counts() # counts the no of each labels present in dataframe

df.groupby(60).mean() # gives the mean of each of each column for rocks and mines

X=df.drop(columns=60,axis=1) # separation of training set stored in value X
Y=df[60] # separation of testing set from dataset and storing in Y

print(X,Y)

"""TRAING & TESTING

"""

from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=1)
# splitting X,Y in the test size 0.1 = 10 % of data into testing considering equal no each label entity

print(X_train,X_test,Y_train,Y_test)

"""model training

"""

from sklearn.linear_model import LogisticRegression

model= LogisticRegression()

model.fit(X_train,Y_train) # training logstic regression model with training data training labels

"""model evaluation"""

from sklearn.metrics import accuracy_score

X_prediction= model.predict(X_train) # calculating accuracy >70% is considered good
X_accuracy=accuracy_score(X_prediction,Y_train)

"""predictive system"""

input_data=(0.0207,0.0535,0.0334,0.0818,0.0740,0.0324,0.0918,0.1070,0.1553,0.1234,0.1796,0.1787,0.1247,0.2577,0.3370,0.3990,0.1647,0.2266,0.3219,0.5356,0.8159,1.0000,0.8701,0.6889,0.6299,0.5738,0.5707,0.5976,0.4301,0.2058,0.1000,0.2247,0.2308,0.3977,0.3317,0.1726,0.1429,0.2168,0.1967,0.2140,0.3674,0.2023,0.0778,0.0925,0.2388,0.3400,0.2594,0.1102,0.0911,0.0462,0.0171,0.0033,0.0050,0.0190,0.0103,0.0121,0.0042,0.0090,0.0070,0.0099)
input_data_np=np.asarray(input_data) # converting input data into numpy array for fast and convient
input_data_reshape=input_data_np.reshape(1,-1) # (1,-1) is used for choosing one label for one input
prediction=model.predict(input_data_reshape)
print(prediction)