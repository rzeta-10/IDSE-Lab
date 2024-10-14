import pandas as pd
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import combinations

# Load the dataset
df = pd.read_csv("clustering_samples.csv")

# Convert the DataFrame to a list of lists
data = df.values.tolist()

# Function to calculate the Euclidean distance
def euclidean_distance(point1, point2):
    return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))

# Initialize K centroids randomly from the data points
def initialize_centroids(data, k):
    return random.sample(data, k)

# Assign each data point to the nearest centroid
def assign_clusters(data, centroids):
    clusters = []
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        cluster = distances.index(min(distances))
        clusters.append(cluster)
    return clusters

# Update centroids as the mean of all data points assigned to each cluster
def update_centroids(data, clusters, k):
    new_centroids = []
    for i in range(k):
        # Collect all points in the current cluster
        cluster_points = [data[j] for j in range(len(data)) if clusters[j] == i]
        if cluster_points:
            # Calculate the mean for each dimension
            new_centroid = [sum(dim) / len(cluster_points) for dim in zip(*cluster_points)]
        else:
            # If a cluster has no points, reinitialize a random centroid
            new_centroid = random.choice(data)
        new_centroids.append(new_centroid)
    return new_centroids

# K-means algorithm
def k_means_clustering(data, k, max_iterations=100, tolerance=1e-4):
    centroids = initialize_centroids(data, k)
    for _ in range(max_iterations):
        old_centroids = centroids
        clusters = assign_clusters(data, centroids)
        centroids = update_centroids(data, clusters, k)
        
        # Check for convergence (if centroids don't change significantly)
        converged = all(
            euclidean_distance(c1, c2) < tolerance
            for c1, c2 in zip(centroids, old_centroids)
        )
        if converged:
            break
    return clusters, centroids

# Run K-means clustering with K=3
k = 3
clusters, centroids = k_means_clustering(data, k)

# Define colors for plotting clusters
colors = ['r', 'g', 'b']  # Red, Green, Blue for 3 clusters

# Plotting all combinations of features in 3D
features = df.columns.tolist()

# Create a 3D plot for each combination of three features
fig = plt.figure(figsize=(15, 10))
for i, (f1, f2, f3) in enumerate(combinations(features, 3)):
    ax = fig.add_subplot(2, 2, i + 1, projection='3d')
    
    for j, point in enumerate(data):
        ax.scatter(point[features.index(f1)], point[features.index(f2)], point[features.index(f3)],
                   color=colors[clusters[j]], label=f"Cluster {clusters[j]}" if j == 0 else "")
    
    # Plot the centroids in the 3D space
    for centroid in centroids:
        ax.scatter(centroid[features.index(f1)], centroid[features.index(f2)], centroid[features.index(f3)],
                   color='black', marker='x', s=100, label='Centroid')

    ax.set_title(f"K-means Clustering of {f1}, {f2}, {f3} (K={k})")
    ax.set_xlabel(f1)
    ax.set_ylabel(f2)
    ax.set_zlabel(f3)
    ax.legend()

plt.tight_layout()
plt.show()
