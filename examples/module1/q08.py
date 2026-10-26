"""Module 1 Question 8: Implement a k-Nearest Neighbors (kNN) classifier using scikit-learn. Split the dataset and display test accuracy."""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
d=load_iris(); X_train,X_test,y_train,y_test=train_test_split(d.data,d.target,test_size=0.2,random_state=42,stratify=d.target)
sc=StandardScaler(); X_train=sc.fit_transform(X_train); X_test=sc.transform(X_test)
model=KNeighborsClassifier(n_neighbors=5).fit(X_train,y_train)
print("Accuracy:",accuracy_score(y_test,model.predict(X_test)))
