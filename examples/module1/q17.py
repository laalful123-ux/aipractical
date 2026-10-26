"""Module 1 Question 17: Use the MNIST dataset to build a binary classifier for digit versus not-digit and evaluate its performance."""

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report
d=load_digits(); X=d.data; y=(d.target==5).astype(int)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42,stratify=y)
model=LogisticRegression(max_iter=5000).fit(X_train,y_train); pred=model.predict(X_test)
print("Accuracy:",accuracy_score(y_test,pred)); print(classification_report(y_test,pred))
