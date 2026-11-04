# Module 21 Cheat Sheets

## Overview

This folder contains quick-reference guides, summaries, formulas, and study aids for Module 21 topics:

- K-Means Clustering
- Reinforcement Learning
- Q-Learning
- Bellman Equation
- Deep Neural Networks
- TensorFlow
- Deep Q-Networks (DQN)

These cheat sheets are intended to provide a concise review of key concepts, algorithms, formulas, and Python implementations covered throughout the module.

---

# Contents

```text
Cheat_Sheets
│
├── KMeans_Cheat_Sheet.md
├── Reinforcement_Learning_Cheat_Sheet.md
├── QLearning_Cheat_Sheet.md
├── Deep_Neural_Networks_Cheat_Sheet.md
├── TensorFlow_Cheat_Sheet.md
└── Module_21_Formula_Sheet.md
```

---

# Topics Covered

## K-Means Clustering

Key concepts:

- Unsupervised Learning
- Clusters
- Centroids
- Feature Scaling
- SSE
- Elbow Method

Common code:

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
```

---

## Reinforcement Learning

Key concepts:

- Agent
- Environment
- States
- Actions
- Rewards
- Episodes
- Policies

Workflow:

```text
State
  ↓
Action
  ↓
Reward
  ↓
Learning
```

---

## Q-Learning

Key concepts:

- Q-Matrix
- Exploration
- Exploitation
- Bellman Equation
- Discount Factor (γ)
- Learning Rate (α)

Q-Matrix Structure:

```text
Rows    = States
Columns = Actions
```

---

## Bellman Equation

Core equation used to update Q-values:

```text
Q(s,a) =
Q(s,a) + α[R + γ max(Q') - Q(s,a)]
```

Where:

- α = Learning Rate
- γ = Discount Factor
- R = Reward

---

## Deep Neural Networks

Neural Network Architecture:

```text
Input Layer
      ↓
Hidden Layer(s)
      ↓
Output Layer
```

Key concepts:

- Neurons
- Activations
- Weights
- Biases
- Activation Functions

---

## TensorFlow

Common imports:

```python
import tensorflow as tf
from tensorflow import keras
```

Applications:

- Image Recognition
- Deep Learning
- Neural Networks
- Computer Vision

---

# Quick Reference

## K-Means Workflow

```text
Select K
    ↓
Initialize Centroids
    ↓
Assign Points
    ↓
Update Centroids
    ↓
Repeat
```

---

## Reinforcement Learning Workflow

```text
State
   ↓
Action
   ↓
Reward
   ↓
Q-Matrix Update
```

---

## Deep Learning Workflow

```text
Forward Propagation
         ↓
Prediction
         ↓
Error
         ↓
Backward Propagation
         ↓
Weight Updates
```

---

# Purpose

These cheat sheets are designed to:

- Support exam preparation
- Provide quick formula reference
- Summarize module content
- Accelerate assignment completion
- Reinforce machine learning concepts

---

# Module 21 Focus Areas

✅ K-Means Clustering

✅ Elbow Method

✅ Reinforcement Learning

✅ Q-Learning

✅ Bellman Equation

✅ Q-Matrix

✅ Deep Neural Networks

✅ TensorFlow

✅ Deep Q-Networks (DQN)

✅ Image Recognition

---

# Author

**Clifford J. Ferraren**

MIT Professional Education  
Applied Data Science Program