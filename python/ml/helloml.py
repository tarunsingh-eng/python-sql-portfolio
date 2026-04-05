import os

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, classification_report

# 2. LOAD DATA
BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "data.csv")
df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())

print("\nInfo:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nClass distribution:")
print(df['purchased'].value_counts()) 

df = df.dropna()

X = df.drop('purchased', axis=1)
Y = df['purchased']


X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

pipeline = Pipeline ([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

pipeline.fit(X_train, Y_train)

Y_pred = pipeline.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)
f1 = f1_score(Y_test, Y_pred, average='weighted')

print("\nAccuracy:", accuracy)
print("F1 Score:", f1)

print("\nClassification Report:")
print(classification_report(Y_test, Y_pred))
