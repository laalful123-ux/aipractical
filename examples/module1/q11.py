"""Module 1 Question 11: Implement Naïve Bayes classification using a small dataset, and show how the dataset is divided into training and testing sets."""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
d=load_iris(); X_train,X_test,y_train,y_test=train_test_split(d.data,d.target,test_size=0.2,random_state=42,stratify=d.target)
print("Training samples:",len(X_train)); print("Testing samples:",len(X_test))
model=GaussianNB().fit(X_train,y_train); pred=model.predict(X_test)
print("Predictions:",pred); print("Accuracy:",accuracy_score(y_test,pred))
