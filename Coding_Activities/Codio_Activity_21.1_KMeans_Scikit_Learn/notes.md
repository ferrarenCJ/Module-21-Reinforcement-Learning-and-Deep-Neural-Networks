# Required Codio Activity 21.1: Coding K-Means Using Scikit-Learn

## Activity Overview

**Learning Outcome Addressed**

- Implement K-Means using Scikit-Learn.

**Points:** 20  
**Platform:** Codio  
**Activity Type:** Required

---

# Objective

This activity provides hands-on experience implementing the K-Means clustering algorithm using the Scikit-Learn library.

The activity focuses on:

- Generating synthetic datasets
- Visualizing data clusters
- Standardizing feature values
- Implementing K-Means clustering
- Determining the optimal number of clusters using the Elbow Method

---

# Concepts Practiced

## K-Means Clustering

K-Means is an unsupervised machine learning algorithm that partitions data into a predefined number of clusters.

The algorithm attempts to:

- Minimize within-cluster variation
- Maximize separation between clusters
- Identify naturally occurring groups in data

---

## Feature Scaling

Before clustering, data should be standardized so that all variables contribute equally to the analysis.

### Scikit-Learn Example

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

Benefits:

- Removes scale bias
- Improves clustering accuracy
- Accelerates convergence

---

## K-Means Implementation

### Scikit-Learn Example

```python
from sklearn.cluster import KMeans

kmeans = KMeans(
    init="random",
    n_clusters=4,
    random_state=42
)

kmeans.fit(X_scaled)
```

After fitting:

```python
y_pred = kmeans.predict(X_scaled)
```

The model assigns each observation to a cluster.

---

# Activity Questions Summary

## Question 1

### Generate Synthetic Data

Used:

```python
X, y_true = make_blobs(
    n_samples=300,
    centers=3,
    cluster_std=0.60,
    random_state=0
)
```

---

## Question 2

### Visualize Raw Features

Created a scatterplot using:

```python
plt.scatter(X[:, 0], X[:, 1], s=50)
```

Purpose:

- Observe natural cluster formation
- Explore feature distribution

---

## Question 3

### Standardize Features

Used:

```python
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

Purpose:

- Normalize feature scales
- Improve clustering accuracy

---

## Question 4

### Visualize Scaled Features

Created a scatterplot of:

```python
X_scaled
```

Observation:

- Overall structure remained similar
- Data became standardized around common scales

---

## Question 5

### Train K-Means Model

Implemented:

```python
kmeans = KMeans(
    init="random",
    n_clusters=4,
    random_state=42
)

kmeans.fit(X_scaled)

y_means = kmeans.predict(X_scaled)
```

Note:

The provided notebook visualization referenced:

```python
y_kmeans
```

while the instructions required:

```python
y_means
```

A workaround was:

```python
y_kmeans = y_means
```

---

## Question 6

### Determine Optimal Number of Clusters

Answer:

```python
ans6 = 3
```

Reasoning:

The synthetic dataset was generated with:

```python
centers=3
```

The Elbow Method confirmed that:

```text
K = 3
```

was the optimal number of clusters.

---

# Key Concepts Reinforced

## Cluster

A group of similar observations.

---

## Centroid

The center point of a cluster.

---

## Feature Scaling

Transforming variables so they use a comparable scale.

---

## StandardScaler

A Scikit-Learn utility used to standardize feature values.

---

## Sum of Squared Errors (SSE)

Measures the total distance between observations and their cluster centroids.

Goal:

```text
Minimize SSE
```

---

## Elbow Method

Technique used to determine the optimal number of clusters.

Process:

```text
Calculate SSE
for many K values

      ↓

Plot K vs SSE

      ↓

Find Elbow Point

      ↓

Select Optimal K
```

---

# Lessons Learned

- K-Means is one of the most widely used clustering algorithms.
- Data should typically be standardized before clustering.
- The choice of K significantly impacts clustering quality.
- The Elbow Method helps identify the best number of clusters.
- Scikit-Learn provides a straightforward implementation of K-Means.
- Visualizing cluster assignments helps validate clustering performance.

---

# Real-World Applications

K-Means clustering is commonly used for:

- Customer segmentation
- Marketing analytics
- Fraud detection
- Image processing
- Pattern recognition
- Predictive maintenance
- Fleet operations analytics
- Utility asset analysis

---

# Key Takeaways

- K-Means is an unsupervised learning algorithm.
- Clustering organizes similar observations into groups.
- Standardization is critical before clustering.
- SSE measures clustering error.
- The Elbow Method helps identify the optimal number of clusters.
- Scikit-Learn makes clustering implementation simple and efficient.