# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

df = pd.read_csv('Employee-Attrition.csv')

x=df.iloc[:,0:49].values
y=df.iloc[:,1].values
features = list((df.drop(['Attrition'],axis=1)).columns)
target = 'Attrition'

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
l = LabelEncoder() 
for i in df[1:]:
    if df[i].dtype == 'object':
        if len(list(df[i].unique())) >= 1:
            l.fit(df[i])
            df[i] = l.transform(df[i])

df = pd.get_dummies(df, drop_first = True)
            
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df[features],df[target],test_size=0.3,random_state=1)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=35,criterion="entropy")
rf.fit(x_train,y_train)