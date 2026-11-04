# Supervised vs Unsupervised Learning Cheat Sheet

## Machine Learning Categories

Machine Learning is commonly divided into two major categories:

```text
Machine Learning
       │
       ├── Supervised Learning
       │
       └── Unsupervised Learning
```

---

# Supervised Learning

## Definition

Supervised learning uses labeled data.

The correct answer already exists in the dataset and is used to train the model.

```text
Input Data
     +
Known Outcome
```

---

# How It Works

```text
Training Data
      ↓
Features + Labels
      ↓
Model Learns Relationship
      ↓
Predict New Data
```

---

# Example

House Price Prediction

Training Data:

```text
Square Feet
Bedrooms
Bathrooms
Price
```

The model learns:

```text
Features → Price
```

---

# Common Supervised Learning Tasks

## Classification

Predict a category.

Examples:

```text
Spam / Not Spam
Survived / Not Survived
Fraud / Not Fraud
```

---

## Regression

Predict a numeric value.

Examples:

```text
House Price
Sales Forecast
Temperature
```

---

# Common Supervised Algorithms

## Logistic Regression

```text
Classification
```

---

## Decision Trees

```text
Classification
Regression
```

---

## Random Forest

```text
Classification
Regression
```

---

## Neural Networks

```text
Classification
Regression
```

---

# Advantages

✅ High Predictive Accuracy

✅ Clear Performance Metrics

✅ Works Well with Labeled Data

✅ Easy to Evaluate

---

# Disadvantages

❌ Requires Labeled Data

❌ Data Labeling Can Be Expensive

❌ May Overfit

---

# Unsupervised Learning

## Definition

Unsupervised learning uses unlabeled data.

There are no known answers provided to the model.

```text
Input Data
Only
```

The algorithm discovers patterns automatically.

---

# How It Works

```text
Raw Data
     ↓
Pattern Discovery
     ↓
Group Similar Data
```

---

# Example

Customer Segmentation

Dataset:

```text
Age
Income
Purchases
```

No customer groups are provided.

The model discovers the groups automatically.

---

# Common Unsupervised Learning Tasks

## Clustering

Group similar records.

Examples:

```text
Customer Segments
Product Categories
Behavior Groups
```

---

## Association Analysis

Identify relationships.

Example:

```text
Market Basket Analysis
```

---

## Dimensionality Reduction

Reduce feature count while preserving information.

Examples:

```text
PCA
t-SNE
```

---

# Common Unsupervised Algorithms

## K-Means

```text
Clustering
```

---

## Hierarchical Clustering

```text
Cluster Discovery
```

---

## DBSCAN

```text
Density-Based Clustering
```

---

## PCA

```text
Dimensionality Reduction
```

---

# Advantages

✅ No Labels Required

✅ Finds Hidden Patterns

✅ Useful for Exploration

✅ Handles Large Datasets

---

# Disadvantages

❌ Harder to Evaluate

❌ Results May Be Subjective

❌ Cluster Meaning Not Always Clear

---

# Comparison

## Data Requirements

### Supervised

```text
Labeled Data Required
```

### Unsupervised

```text
No Labels Required
```

---

## Goal

### Supervised

```text
Predict Outcomes
```

### Unsupervised

```text
Find Hidden Patterns
```

---

## Output

### Supervised

```text
Predictions
```

### Unsupervised

```text
Groups or Structures
```

---

# Examples from Module 21

## Supervised Learning Example

Titanic Dataset

```text
Passenger Information
          ↓
Predict Survival
```

Known Label:

```text
Survived
```

---

## Unsupervised Learning Example

K-Means Clustering

```text
Data
 ↓
Clusters
 ↓
Patterns
```

No labels required.

---

# Evaluation Metrics

## Supervised Learning

Common Metrics:

```text
Accuracy
Precision
Recall
Specificity
F1 Score
```

---

## Unsupervised Learning

Common Metrics:

```text
SSE
Elbow Method
Cluster Quality
```

---

# K-Means and Unsupervised Learning

K-Means belongs to:

```text
Unsupervised Learning
```

Workflow:

```text
Choose K
      ↓
Assign Clusters
      ↓
Update Centroids
      ↓
Repeat
```

---

# Reinforcement Learning

Module 21 also introduced:

```text
Reinforcement Learning
```

A third machine learning approach.

---

# Reinforcement Learning Characteristics

```text
State
 ↓
Action
 ↓
Reward
 ↓
Learning
```

Examples:

- Q-Learning
- SARSA
- Deep Q-Networks

---

# Machine Learning Comparison

```text
Supervised Learning
      ↓
Known Answers

Unsupervised Learning
      ↓
No Answers

Reinforcement Learning
      ↓
Rewards + Penalties
```

---

# Module 21 Exam Facts

### Supervised Learning

```text
Uses Labeled Data
```

---

### Unsupervised Learning

```text
Uses Unlabeled Data
```

---

### K-Means

```text
Unsupervised Learning
```

---

### Titanic Dataset

```text
Classification Problem
```

---

### Reinforcement Learning

```text
Rewards and Penalties
```

---

# Quick Review

```text
Supervised
     ↓
Labels
     ↓
Prediction

Unsupervised
     ↓
No Labels
     ↓
Pattern Discovery

Reinforcement
     ↓
Rewards
     ↓
Learning
```