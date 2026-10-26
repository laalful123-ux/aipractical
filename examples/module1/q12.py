"""Module 1 Question 12: Implement a machine-learning workflow using a suitable dataset: load with Pandas, handle missing values or scale features, split into training and testing sets, train a classifier, and display training and testing accuracy."""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
d=load_iris(); df=pd.DataFrame(d.data,columns=d.feature_names); df["target"]=d.target
X,y=df.drop(columns="target"),df["target"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
model=make_pipeline(SimpleImputer(strategy="median"),DecisionTreeClassifier(random_state=42)).fit(X_train,y_train)
print("Training accuracy:",accuracy_score(y_train,model.predict(X_train)))
print("Testing accuracy:",accuracy_score(y_test,model.predict(X_test)))
