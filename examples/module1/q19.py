"""Module 1 Question 19: Perform multiclass classification using Logistic Regression or a Decision Tree on a suitable dataset."""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
d=load_iris(); X_train,X_test,y_train,y_test=train_test_split(d.data,d.target,test_size=0.2,random_state=42,stratify=d.target)
model=LogisticRegression(max_iter=2000).fit(X_train,y_train); pred=model.predict(X_test)
print("Predictions:",pred[:10]); print("Accuracy:",accuracy_score(y_test,pred))
