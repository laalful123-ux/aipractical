"""Module 1 Question 10: Analyze a public dataset for class imbalance and possible bias. Display class counts and briefly discuss limitations in the data."""

from sklearn.datasets import load_iris
import pandas as pd
d=load_iris(); df=pd.DataFrame(d.data,columns=d.feature_names); df["class"]=d.target
print("Class counts:"); print(df["class"].value_counts().sort_index())
print("Missing values:"); print(df.isnull().sum())
print("Limitations: Iris is small and may not represent real-world populations.")
