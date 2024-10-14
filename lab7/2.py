# CS22B1093 ROHAN G

import pandas as pd
import math 
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import combinations

# i - k-means clustering
df = pd.read_csv("clustering_samples.csv")

data = df.values.tolist()
features = df.columns.tolist()

def euclidean_distance(p1,p2):
    return math.sqrt(sum((point1-point2)**2 for point1,point2 in zip(p1,p2))) # zip combines into pairs ex : l = [1,2,3]
                                                                            # zip -> [(1,2),(2,3),(3,1)]
def init_centroids(data, k):
    return random.sample(data,k)
    
def assign_clusters(data, centroids):
    clusters = []
    for i in data:
        dist = [euclidean_distance(i,centroid) for centroid in centroids]
        cluster = dist.index(min(dist))
        clusters.append(cluster)
    
    return clusters
    
def update(data, clusters, k):
    new_centroids = []
    for i in range(k):
        cluster_point = [data[j] for j in range(len(data)) if clusters[j]==i]
        if cluster_point:
            new_centroid = [sum(dim)/len(cluster_point) for dim in zip(*cluster_point)]
        else:
            new_centroid = random.choice(data)
        new_centroids.append(new_centroid)
        
    return new_centroids
    
def k_means(data, k, epochs=100, tolerance = 1e-4):
    centroids = init_centroids(data, k)
    for _ in range(epochs):
        old_centroids = centroids
        clusters = assign_clusters(data, centroids)
        centroids = update(data, clusters, k)
        
        converge = all(euclidean_distance(c1,c2) < tolerance for c1,c2 in zip(centroids,old_centroids))
        if converge:
            break
    
    return clusters, centroids
    
k = 3
clusters, centroids = k_means(data, k)

# ii - visualization
colors = ['r','g','b'] # colors for the different cluster points

fig = plt.figure(figsize=(15,10))

for i,(f1,f2,f3) in enumerate(combinations(features, 3)):
    ax = fig.add_subplot(2,2, i+1, projection='3d')
    
    for j,p in enumerate(data):
        ax.scatter(p[features.index(f1)], p[features.index(f2)], p[features.index(f3)], color=colors[clusters[j]]
                    , label=f"Cluster {clusters[j]}" if j==0 else "")
    
    for k in centroids:
        ax.scatter(k[features.index(f1)], k[features.index(f2)], k[features.index(f3)], color='black'
                    , marker='X', s=100, label='centroid')
                    
    ax.set_title(f"K-Means Clustering of {f1}, {f2}, {f3} (k=3)")
    ax.set_xlabel(f1)
    ax.set_ylabel(f2)
    ax.set_zlabel(f3)

plt.tight_layout()
plt.show()