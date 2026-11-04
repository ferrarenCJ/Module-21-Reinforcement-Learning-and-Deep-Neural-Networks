# K-Means Cheat Sheet

## What is K-Means?

K-Means is an unsupervised machine learning algorithm used to group similar data points into clusters.

Primary Goal:

```text
Identify Patterns
and
Group Similar Records
```

---

# Key Concepts

## Cluster

A group of similar data points.

Example:

```text
Cluster 1 = Customers
Cluster 2 = Products
Cluster 3 = Regions
```

---

## Centroid

The center of a cluster.

```text
Cluster
   ↓
Calculate Mean
   ↓
New Centroid
```

---

## K

Represents:

```text
Number of Clusters
```

Example:

```python
K = 3
```

Three clusters will be created.

---

# K-Means Workflow

```text
Choose K
    ↓
Create Initial Centroids
    ↓
Assign Data Points
    ↓
Calculate New Centroids
    ↓
Repeat Until Stable
```

---

# The K-Means Algorithm

## Step 1

Choose the number of clusters.

```python
K = 2
```

---

## Step 2

Randomly initialize centroids.

```text
Cluster Centers Created
```

---

## Step 3

Assign each point to the nearest centroid.

```text
Data Point
      ↓
Nearest Centroid
      ↓
Assigned Cluster
```

---

## Step 4

Calculate new centroids.

```text
Cluster Members
        ↓
Compute Mean
        ↓
New Centroid
```

---

## Step 5

Repeat until centroid locations stop changing.

```text
Convergence Achieved
```

---

# Expectation-Maximization Process

## Expectation Step

Assign records to nearest centroid.

```text
Point
  ↓
Closest Centroid
```

---

## Maximization Step

Recalculate centroids.

```text
Current Cluster
        ↓
Average Coordinates
        ↓
New Centroid
```

---

# Python Example

Import:

```python
from sklearn.cluster import KMeans
```

Create Model:

```python
kmeans = KMeans(
    n_clusters=2
)
```

Train Model:

```python
kmeans.fit(X)
```

---

# Predict Clusters

```python
predictions = kmeans.predict(X)
```

---

# View Cluster Centers

```python
kmeans.cluster_centers_
```

---

# Example Dataset

```text
Height
Weight
```

Possible Result:

```text
Cluster 1
Tall Individuals

Cluster 2
Short Individuals
```

---

# Sum of Squared Errors (SSE)

Measures cluster quality.

Formula Concept:

```text
Distance
Between Points
and Centroids
```

Lower SSE:

```text
Better Clustering
```

---

# Elbow Method

Used to determine the optimal number of clusters.

---

# Elbow Method Workflow

```text
K=1
K=2
K=3
K=4
K=5
```

Compute:

```text
SSE for Each K
```

Plot:

```text
K vs SSE
```

---

# Elbow Point

The point where SSE begins to level off.

```text
Large Improvement
         ↓
Small Improvement
         ↓
Elbow Point
```

This is usually the optimal K.

---

# Feature Scaling

Important before K-Means.

Reason:

```text
Large Numbers
Can Dominate Distance Calculations
```

---

# StandardScaler

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

---

# Distance Calculation

K-Means usually uses:

```text
Euclidean Distance
```

Formula Concept:

```text
Shortest Straight-Line Distance
Between Two Points
```

---

# Advantages

✅ Easy to Understand

✅ Fast

✅ Scalable

✅ Works Well on Large Datasets

✅ Widely Used

---

# Disadvantages

❌ Must Choose K

❌ Sensitive to Outliers

❌ Sensitive to Initial Centroids

❌ Not Ideal for Complex Shapes

---

# Real-World Applications

## Customer Segmentation

```text
Group Similar Customers
```

---

## Market Analysis

```text
Identify Customer Groups
```

---

## Recommendation Systems

```text
Group Similar Users
```

---

## Fraud Detection

```text
Identify Unusual Clusters
```

---

## Healthcare

```text
Patient Segmentation
```

---

# Titanic Assignment Example

Target:

```text
Survived
Not Survived
```

K Value:

```python
n_clusters = 2
```

---

# Common Functions

Display Statistics:

```python
df.describe()
```

Check Missing Values:

```python
df.isna().sum()
```

Fill Missing Values:

```python
df.fillna(
    df.mean(),
    inplace=True
)
```

Train Model:

```python
kmeans.fit(X_train)
```

Predict:

```python
kmeans.predict(X_test)
```

---

# K-Means Exam Facts

### Learning Type

```text
Unsupervised Learning
```

---

### Uses

```text
Clustering
```

---

### Center of Cluster

```text
Centroid
```

---

### Quality Metric

```text
SSE
```

---

### Optimal K Method

```text
Elbow Method
```

---

### Main Process

```text
Assign
 ↓
Update
 ↓
Repeat
```

---

# Quick Review

```text
Choose K
    ↓
Initialize Centroids
    ↓
Assign Points
    ↓
Update Centroids
    ↓
Repeat
    ↓
Clusters Created
```