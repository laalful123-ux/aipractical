"""Module 1 Question 28: Select a public dataset and analyze possible bias and class imbalance. Report the class distribution and observations."""

from sklearn.datasets import load_iris
import pandas as pd
d=load_iris(); df=pd.DataFrame(d.data,columns=d.feature_names); df["class"]=d.target
print("Class counts:"); print(df["class"].value_counts().sort_index())
print("Missing values:"); print(df.isnull().sum())
print("Limitations: Iris is small and may not represent real-world populations.")
