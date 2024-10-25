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

df = pd.read_csv("./diabetes.csv")

print(df.info)
print(df.head())
print(df.describe)

X = df.drop(columns='Outcome')
y = df['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)

print(f"Training set shape : {X_train.shape}")
print(f"Testing set shape : {X_test.shape}")

knn = KNeighborsClassifier(n_neighbors=60)

knn.fit(X_train,y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy : {accuracy:.2f}")

# sample = X_test[0].reshape(1,-1)
# prediction = knn.predict(sample)
# print(f"\nSample Predcition : {df[prediction[0]]}")

cm = confusion_matrix(y_test,y_pred)
print(cm)
cm_df = pd.DataFrame(cm,index=['True','False'],columns=['True','False'])
plt.figure(figsize=(10,5))
sns.heatmap(cm_df,annot=True,cmap="Blues",fmt='g')
plt.title("Confusion Matrix")
plt.ylabel("True Label")
plt.xlabel("Predicted Label")
plt.show()