"""Module 1 Question 27: Implement Decision Tree regression on a suitable regression dataset and evaluate its predictions."""

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error,r2_score
d=load_diabetes(); X_train,X_test,y_train,y_test=train_test_split(d.data,d.target,test_size=0.2,random_state=42)
model=DecisionTreeRegressor(max_depth=5,random_state=42).fit(X_train,y_train); pred=model.predict(X_test)
print("Predictions:",pred[:5]); print("MAE:",mean_absolute_error(y_test,pred)); print("R2:",r2_score(y_test,pred))
