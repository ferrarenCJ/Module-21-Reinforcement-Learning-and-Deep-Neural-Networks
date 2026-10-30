# Video 21.2: Understanding K-Means

**Duration:** 07:49

---

# Overview

This video introduces the **K-Means Clustering Algorithm**, one of the most popular unsupervised machine learning algorithms.

K-Means is used to group similar data points into clusters based on shared characteristics and proximity within a dataset.

Unlike supervised learning, K-Means does not require labeled training data. Instead, it discovers patterns and structures that already exist within the data.

---

# What is K-Means?

K-Means is an **unsupervised learning algorithm** used for clustering.

The objective is to partition data into a specified number of clusters (**K**) where:

- Data points within a cluster are similar.
- Data points in different clusters are dissimilar.
- Each cluster is represented by a centroid.

---

# Why Use K-Means?

K-Means helps identify hidden patterns in data without requiring predefined labels.

Common applications include:

- Customer segmentation
- Image classification
- Pattern recognition
- Recommendation systems
- Anomaly detection
- Data exploration

---

# How K-Means Works

The algorithm follows a series of iterative steps.

## Step 1: Select K

Determine the number of clusters to create.

Example:

```text
K = 3
```

The algorithm will attempt to divide the dataset into three groups.

---

## Step 2: Initialize Centroids

Random starting points are selected.

These points act as the center of each cluster.

```text
Cluster A → Centroid A
Cluster B → Centroid B
Cluster C → Centroid C
```

---

## Step 3: Assign Data Points

Each data point is assigned to the nearest centroid.

```text
Point 1 → Cluster A

Point 2 → Cluster B

Point 3 → Cluster A
```

The assignment is typically based on Euclidean distance.

---

## Step 4: Recalculate Centroids

After assigning points, the centroid position is recalculated.

The new centroid becomes:

```text
Average position of all points
within the cluster
```

---

## Step 5: Repeat

The algorithm repeatedly:

1. Assigns points to clusters
2. Recalculates centroids

until the centroids stop moving significantly.

This is called **convergence**.

---

# Visual Representation

```text
Initial State

     x       x

x

             x

      o

x              x

o = centroid
x = data point
```

After several iterations:

```text
Cluster 1        Cluster 2

x x x            x x x
x x              x x

   ●                ●

● = centroid
```

The data naturally forms groups.

---

# K-Means with Scikit-Learn

The video demonstrates the use of the Scikit-Learn implementation of K-Means.

Typical workflow:

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=10)

kmeans.fit(data)
```

After training:

```python
kmeans.labels_
```

returns the cluster assignment for each data point.

---

# Digit Classification Example

The video demonstrates K-Means using handwritten digit data.

The algorithm:

1. Receives image data
2. Groups similar digit images
3. Creates clusters containing similar patterns

Although K-Means is unsupervised and does not know the actual digit labels, it can often group similar digits together effectively.

Example:

```text
Cluster 1 → Mostly digit 0

Cluster 2 → Mostly digit 1

Cluster 3 → Mostly digit 7
```

---

# Advantages of K-Means

## Simple to Implement

The algorithm is straightforward and computationally efficient.

## Fast Training

Works well for many medium-sized datasets.

## Unsupervised Learning

Does not require labeled training data.

## Pattern Discovery

Can uncover hidden relationships and structures in data.

---

# Limitations of K-Means

## Choosing K

The number of clusters must be specified beforehand.

Choosing the wrong K can produce poor results.

---

## Sensitive to Initialization

Different starting centroids can lead to different solutions.

---

## Assumes Spherical Clusters

K-Means performs best when clusters are reasonably compact and evenly distributed.

---

## Outlier Sensitivity

Extreme values can distort centroid locations.

---

# Key Concepts

## Cluster

A collection of similar data points.

---

## Centroid

The center point of a cluster.

---

## Convergence

The point at which centroid locations no longer change significantly.

---

## Distance Metric

A mathematical method used to determine similarity between data points.

Commonly:

```text
Euclidean Distance
```

---

# Real-World Applications

### Customer Analytics

Group customers based on purchasing behavior.

### Marketing

Create targeted campaigns for different customer groups.

### Image Processing

Group images with similar characteristics.

### Fraud Detection

Identify unusual transaction patterns.

### Industrial Analytics

Group equipment based on operational behavior.

---

# Connection to Data Engineering

K-Means commonly appears in data engineering workflows when processing large volumes of data.

Examples include:

- Customer segmentation
- Log analysis
- Sensor clustering
- Asset utilization analysis
- Predictive maintenance preparation

For utility and fleet operations, clustering could be used to:

- Group vehicles by utilization patterns
- Group equipment by maintenance history
- Identify abnormal fuel consumption behavior
- Discover operational trends

---

# Key Takeaways

- K-Means is an unsupervised machine learning algorithm.
- Data is grouped into K clusters.
- Each cluster is represented by a centroid.
- The algorithm iteratively assigns points and recalculates centroids.
- K-Means is widely used for pattern discovery and data segmentation.
- Scikit-Learn provides a simple implementation of K-Means.
- The algorithm can classify similar handwritten digits through clustering.
- Choosing the correct value of K is critical for good results.

---

# Study Notes

## Remember

```text
K-Means
    ↓
Unsupervised Learning
    ↓
Choose K Clusters
    ↓
Assign Points
    ↓
Recalculate Centroids
    ↓
Repeat Until Convergence
```

## Important Formula

Distance between points is commonly measured using:

```text
Euclidean Distance
```

The nearest centroid determines cluster membership.

---

# Next Topic

Mini-Lesson 21.2: Basics of K-Means

Topics:

- Selecting K
- Cluster Evaluation
- K-Means Implementation
- Practical Clustering Considerations