# Activity 21.1: K-Means Clustering

## Overview

This activity introduces the K-Means clustering algorithm, one of the most widely used unsupervised machine learning techniques.

The objective is to understand how K-Means groups similar observations into clusters and how cluster centers (centroids) are iteratively updated until convergence.

---

# Learning Objectives

By completing this activity, you will be able to:

- Understand clustering in machine learning.
- Explain the purpose of the K-Means algorithm.
- Create and train a K-Means model using Scikit-Learn.
- Interpret cluster assignments.
- Calculate and evaluate cluster quality.
- Use the Elbow Method to identify the optimal number of clusters.

---

# Key Concepts

## Unsupervised Learning

K-Means is an unsupervised learning algorithm.

Unlike supervised learning:

```text
Inputs + Labels
```

K-Means uses:

```text
Inputs Only
```

The algorithm discovers patterns and groups automatically.

---

## Cluster

A cluster is a group of similar observations.

Example:

```text
Customer Group A
Customer Group B
Customer Group C
```

---

## Centroid

A centroid represents the center of a cluster.

```text
Cluster
   ↓
Average Position
   ↓
Centroid
```

---

# K-Means Algorithm Workflow

```text
Choose K
    ↓
Initialize Centroids
    ↓
Assign Points
    ↓
Update Centroids
    ↓
Repeat Until Stable
```

---

# Expectation-Maximization Process

## Expectation Step

Assign each data point to its nearest centroid.

```text
Data Point
      ↓
Nearest Centroid
```

---

## Maximization Step

Recalculate centroid positions using the mean of the assigned points.

```text
Cluster Members
        ↓
Average
        ↓
New Centroid
```

---

# Python Libraries Used

```python
import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
```

---

# Creating a K-Means Model

```python
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)
```

---

# Training the Model

```python
kmeans.fit(X)
```

---

# Predicting Clusters

```python
predictions = kmeans.predict(X)
```

---

# Viewing Cluster Centers

```python
kmeans.cluster_centers_
```

---

# Feature Scaling

Feature scaling is recommended before clustering.

Example:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

Benefits:

- Prevents large values from dominating calculations.
- Improves cluster quality.
- Improves convergence.

---

# Sum of Squared Errors (SSE)

SSE measures the distance between observations and cluster centroids.

Lower values indicate:

```text
Better Cluster Fit
```

---

# Elbow Method

The Elbow Method helps determine the appropriate number of clusters.

Workflow:

```text
K = 1
K = 2
K = 3
K = 4
K = 5
```

Calculate:

```text
SSE
```

for each value of K.

---

# Elbow Point

The elbow point is where improvements in SSE begin to decrease significantly.

Example:

```text
Large Improvement
         ↓
Large Improvement
         ↓
Small Improvement
```

Choose K at the bend of the curve.

---

# Example Applications

## Customer Segmentation

```text
Customer Data
      ↓
Cluster Customers
```

---

## Market Analysis

```text
Sales Data
      ↓
Identify Customer Groups
```

---

## Recommendation Systems

```text
User Behavior
       ↓
Group Similar Users
```

---

## Healthcare

```text
Patient Data
      ↓
Patient Clusters
```

---

# Advantages

✅ Easy to Understand

✅ Fast to Train

✅ Scalable

✅ Effective for Large Datasets

✅ Widely Used

---

# Limitations

❌ Requires Choosing K

❌ Sensitive to Outliers

❌ Sensitive to Initial Centroids

❌ Not Suitable for All Data Shapes

---

# Key Takeaways

- K-Means is an unsupervised clustering algorithm.
- Data points are assigned to the nearest centroid.
- Centroids are repeatedly updated until convergence.
- SSE measures clustering performance.
- The Elbow Method helps identify the optimal number of clusters.
- Feature scaling improves clustering quality.
- K-Means is commonly used for segmentation and pattern discovery.

---

# Files

```text
Activity_21.1_KMeans_Clustering/
│
├── Activity_21.1.ipynb
├── Notes.md
└── README.md
```

---

# Module 21 Connection

This activity serves as the foundation for understanding:

```text
Unsupervised Learning
          ↓
Clustering
          ↓
Model Evaluation
          ↓
Advanced Machine Learning
```

and prepares students for later topics involving reinforcement learning and deep neural networks.
