# CS22B1093 ROHAN G

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("./clustering_samples.csv")

print(df.info)
print(df.describe)
print(df.head())

kmeans = KMeans(n_clusters=4, random_state=42) # 4-classes

kmeans.fit(df)

labels = kmeans.labels_


plt.figure(figsize=(8,6))
plt.scatter(df['A'],df['B'], c=labels, cmap='viridis')
plt.xlabel("A")
plt.ylabel("B")
plt.title("K-Means Clustering (k=4)")
plt.show()