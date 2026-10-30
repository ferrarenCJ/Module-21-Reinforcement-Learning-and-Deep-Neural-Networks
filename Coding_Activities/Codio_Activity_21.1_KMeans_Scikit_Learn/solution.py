"""
Module 21
Codio Activity 21.1
Coding K-Means Using Scikit-Learn
"""

import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# ============================================================
# Question 1
# Generate synthetic dataset
# ============================================================

X, y_true = make_blobs(
    n_samples=300,
    centers=3,
    cluster_std=0.60,
    random_state=0
)

# ============================================================
# Question 2
# Plot original features
# ============================================================

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("A plot of my features")
plt.show()

# ============================================================
# Question 3
# Standardize features
# ============================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# ============================================================
# Question 4
# Plot scaled features
# ============================================================

plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], s=50)
plt.title("A plot of my scaled features")
plt.show()

# ============================================================
# Question 5
# K-Means Clustering
# ============================================================

kmeans = KMeans(
    init="random",
    n_clusters=4,
    random_state=42
)

kmeans.fit(X_scaled)

y_means = kmeans.predict(X_scaled)

# Notebook visualization compatibility
y_kmeans = y_means

# Plot clusters and centroids

plt.figure(figsize=(8, 6))
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=y_kmeans,
    s=50,
    cmap="viridis"
)

centers = kmeans.cluster_centers_

plt.scatter(
    centers[:, 0],
    centers[:, 1],
    c="red",
    s=200,
    alpha=0.5
)

plt.title("K-Means Clustering Results")
plt.show()

# ============================================================
# Question 6
# Optimal Number of Clusters
# ============================================================

ans6 = 3

print(f"Optimal Number of Clusters: {ans6}")