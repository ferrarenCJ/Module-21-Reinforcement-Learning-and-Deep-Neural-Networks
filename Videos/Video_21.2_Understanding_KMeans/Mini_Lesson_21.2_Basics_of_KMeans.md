# Mini-Lesson 21.2: Basics of K-Means

---

# Overview

K-Means is one of the most widely used unsupervised machine learning algorithms for clustering data.

The goal of K-Means is to partition data into groups called **clusters**, where data points within a cluster are more similar to each other than to points in other clusters.

Because of its simplicity and effectiveness, K-Means is often one of the first clustering algorithms learned in machine learning and data science.

---

# What is Clustering?

Clustering is a collection of techniques used to organize data into groups based on similarity.

A cluster is a collection of data points that are more similar to one another than to data points in other clusters.

## Example

```text
Customer Data

Cluster 1 → Frequent Buyers

Cluster 2 → Occasional Buyers

Cluster 3 → New Customers
```

The algorithm identifies these groups automatically without requiring labeled data.

---

# K-Means Clustering

K-Means is an unsupervised learning algorithm because it does not require an answer key or labeled training data.

The algorithm attempts to find naturally occurring groups within a dataset.

---

# K-Means Pseudo-Algorithm

The K-Means algorithm follows five basic steps.

## Step 1: Specify Number of Clusters (K)

Choose the number of clusters to create.

```text
K = 3
```

means the algorithm will build three groups.

---

## Step 2: Initialize Centroids

Randomly select the initial centroid positions.

A centroid represents the center of a cluster.

```text
Cluster A → Centroid A

Cluster B → Centroid B

Cluster C → Centroid C
```

---

## Step 3: Expectation Step

Assign each data point to the nearest centroid.

```text
Point 1 → Cluster A

Point 2 → Cluster B

Point 3 → Cluster A
```

Each observation joins the cluster whose centroid is closest.

---

## Step 4: Maximization Step

Calculate a new centroid for each cluster.

The new centroid becomes:

```text
Average Position
of All Points
within the Cluster
```

This is why the algorithm is called K-Means.

The centroid is the mean of all points inside the cluster.

---

## Step 5: Repeat

Repeat:

1. Assign points to clusters
2. Recalculate centroids

until the centroid locations stop changing significantly.

This state is called **convergence**.

---

# Expectation-Maximization (EM)

The core of K-Means relies on a process called:

## Expectation Step

```text
Assign data points
to nearest centroid
```

## Maximization Step

```text
Calculate new centroid
based on assigned points
```

The algorithm repeatedly alternates between these two steps until convergence is achieved.

---

# Visual Example

```text
Initial State

x      x

    o

x           x

o = centroid
```

After several iterations:

```text
Cluster 1       Cluster 2

x x x           x x x
x x             x x

  ●               ●

● = centroid
```

The data naturally separates into groups.

---

# Importance of Standardizing Data

Real-world datasets frequently contain measurements that use different units and scales.

## Example

```text
Height = Inches

Weight = Pounds
```

A machine learning algorithm may incorrectly treat weight as more important than height because weight values typically have a larger numerical range.

---

# Feature Scaling

Feature Scaling is the process of transforming variables so they share a common scale.

Benefits include:

- Improved clustering accuracy
- Reduced bias toward large values
- Better model performance
- Faster convergence

---

# StandardScaler

Scikit-Learn provides the StandardScaler class for standardization.

## Example

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaled_features = scaler.fit_transform(features)
```

### Explanation

```python
StandardScaler()
```

Creates a scaling object.

```python
fit_transform()
```

Calculates scaling parameters and transforms the data.

Result:

```text
Original Features
        ↓
StandardScaler
        ↓
Scaled Features
```

All variables are placed on approximately the same scale.

---

# Choosing the Correct Number of Clusters

One of the most challenging parts of K-Means is determining the optimal number of clusters.

The value of:

```text
K
```

must usually be selected before training.

---

# Sum of Squared Errors (SSE)

A common method for evaluating clusters is the:

## SSE (Sum of Squared Errors)

SSE measures how far points are from their assigned centroids.

### Goal

```text
Minimize SSE
```

Lower values indicate tighter and more consistent clusters.

---

# SSE Interpretation

### Low SSE

```text
Points are close
to centroids
```

Good clustering.

### High SSE

```text
Points are spread far
from centroids
```

Poor clustering.

---

# Elbow Method

A popular approach for selecting the optimal number of clusters.

## Process

Calculate SSE for multiple values of K.

Example:

```text
K = 1
K = 2
K = 3
K = 4
K = 5
...
```

Plot:

```text
K vs SSE
```

---

## Example

```text
SSE
│
│\
│ \
│  \
│   \
│    \__
│       \_
│         \_
└─────────────
    K
```

The curve decreases as K increases.

Eventually the improvement becomes very small.

The point where the curve bends is called the:

## Elbow Point

---

# Optimal Number of Clusters

The elbow point represents the best balance between:

- Cluster quality
- Model complexity

Choosing additional clusters beyond this point generally provides little benefit.

---

# Why Not Always Increase K?

Increasing K often reduces SSE.

However:

```text
More Clusters
≠
Better Solution
```

Too many clusters may:

- Overcomplicate results
- Increase computation
- Reduce interpretability

The elbow method helps avoid overfitting.

---

# Real-World Applications

## Customer Segmentation

Group customers based on purchasing behavior.

---

## Marketing Analytics

Identify target audiences.

---

## Fraud Detection

Discover unusual transaction groups.

---

## Fleet Operations

Cluster vehicles based on:

- Mileage
- Fuel usage
- Utilization rates

---

## Utility Operations

Cluster assets based on:

- Failure history
- Maintenance patterns
- Operational characteristics

---

# Scikit-Learn Workflow

Typical K-Means process:

```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Scale data
scaled_features = StandardScaler().fit_transform(features)

# Create model
kmeans = KMeans(n_clusters=3)

# Train model
kmeans.fit(scaled_features)
```

---

# Key Takeaways

- K-Means is an unsupervised clustering algorithm.
- Clustering groups similar observations together.
- Centroids represent the center of each cluster.
- The algorithm uses Expectation-Maximization.
- Feature scaling is critical before applying K-Means.
- StandardScaler is commonly used for data standardization.
- SSE measures clustering error.
- The objective is to minimize SSE.
- The Elbow Method helps determine the optimal number of clusters.
- K-Means is widely used for customer segmentation, analytics, and pattern discovery.

---

# Study Notes

## K-Means Workflow

```text
Choose K
    ↓
Initialize Centroids
    ↓
Assign Points
(Expectation)
    ↓
Recalculate Centroids
(Maximization)
    ↓
Repeat Until Convergence
```

## Remember

```text
Standardize Data First

    ↓

Run K-Means

    ↓

Calculate SSE

    ↓

Use Elbow Method

    ↓

Determine Optimal K
```