# CS22B1093 ROHAN G

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report

df = pd.read_csv("shopping_trends.csv")

print(df.info())
print(df.head())
print(df.describe())

X = df.drop(columns='Frequency of Purchases')
y = df['Frequency of Purchases']

categorical_cols = ['Gender', 'Item Purchased', 'Category', 'Color', 'Season', 'Promo Code Used']

encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded_features = encoder.fit_transform(X[categorical_cols])

encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(categorical_cols))

X = X.drop(columns=categorical_cols)

X = pd.concat([X.reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(f"Training set shape: {X_train.shape}")
print(f"Testing set shape: {X_test.shape}")

knn = KNeighborsClassifier(n_neighbors=100)

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

print(classification_report(y_test, y_pred))

conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
