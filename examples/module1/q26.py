"""Module 1 Question 26: Implement a Decision Tree classifier using the Iris dataset or another suitable dataset."""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
d=load_iris(); X_train,X_test,y_train,y_test=train_test_split(d.data,d.target,test_size=0.2,random_state=42,stratify=d.target)
model=DecisionTreeClassifier(random_state=42).fit(X_train,y_train); pred=model.predict(X_test)
print("Predictions:",pred); print("Accuracy:",accuracy_score(y_test,pred))
