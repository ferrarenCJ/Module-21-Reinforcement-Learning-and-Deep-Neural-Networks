# Module 21 Sandbox

## Overview

This folder contains experimental notebooks, practice exercises, testing scripts, and exploratory work completed during Module 21.

The Sandbox serves as a safe environment for experimenting with concepts before incorporating them into coding activities, assignments, and projects.

---

# Purpose

The Sandbox is used to:

- Test code snippets.
- Explore machine learning concepts.
- Validate formulas and algorithms.
- Practice reinforcement learning techniques.
- Experiment with TensorFlow models.
- Investigate dataset behavior.
- Troubleshoot errors and solutions.

---

# Topics Explored

## K-Means Clustering

Experiments:

- Testing different cluster counts
- Elbow Method analysis
- SSE evaluation
- Feature scaling comparisons

Example:

```python
from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters=3,
    random_state=42
)
```

---

## Data Preprocessing

Experiments:

- Missing value imputation
- Label encoding
- Data normalization
- Standardization

Example:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
```

---

## Confusion Matrix Metrics

Experiments:

- Accuracy
- Precision
- Recall
- Specificity
- F1 Score

Example:

```python
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score
)
```

---

## Reinforcement Learning

Experiments:

- State transitions
- Reward matrices
- Bellman Equation calculations
- Exploration vs exploitation

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

Experiments:

- Q-Matrix creation
- Q-value updates
- Route optimization
- Hyperparameter tuning

Example:

```python
Q = np.zeros((15,15))
```

---

## Frozen Lake

Experiments:

- Environment exploration
- Episode tracking
- Policy optimization
- Agent navigation

Example:

```python
import gymnasium as gym

env = gym.make("FrozenLake-v1")
```

---

## Deep Neural Networks

Experiments:

- Network architecture design
- Hidden layer tuning
- Activation function comparisons
- Training performance evaluation

Architecture:

```text
Input Layer
      ↓
Hidden Layer(s)
      ↓
Output Layer
```

---

## TensorFlow

Experiments:

- MNIST digit recognition
- Model compilation
- Model training
- Prediction testing

Example:

```python
import tensorflow as tf
from tensorflow import keras
```

---

# Suggested Sandbox Structure

```text
Sandbox/
│
├── README.md
│
├── KMeans_Experiments.ipynb
├── Elbow_Method_Testing.ipynb
├── Reinforcement_Learning_Practice.ipynb
├── Frozen_Lake_Exploration.ipynb
├── Bellman_Equation_Testing.ipynb
├── TensorFlow_Practice.ipynb
├── MNIST_Experiments.ipynb
└── Scratch_Work.ipynb
```

---

# Best Practices

✅ Test ideas before adding them to assignments

✅ Save useful experiments for future reference

✅ Document observations and results

✅ Keep notebooks focused on a single concept

✅ Compare multiple approaches and parameters

✅ Record lessons learned from failures

---

# Common Experiments

## K-Means

```python
for k in range(1,11):
    model = KMeans(n_clusters=k)
```

Purpose:

```text
Find Optimal Number of Clusters
```

---

## Q-Learning

```python
np.argmax(Q[state])
```

Purpose:

```text
Find Best Action
```

---

## TensorFlow

```python
model.fit(
    X_train,
    y_train,
    epochs=5
)
```

Purpose:

```text
Evaluate Model Performance
```

---

# Key Takeaways

- Experimentation accelerates learning.
- Small tests help validate concepts.
- Reinforcement learning is best understood through trial and error.
- TensorFlow models benefit from iterative tuning.
- Sandbox notebooks provide a valuable record of discoveries and troubleshooting efforts.

---

# Module 21 Connection

```text
K-Means
    ↓
Model Evaluation
    ↓
Reinforcement Learning
    ↓
Q-Learning
    ↓
Deep Neural Networks
    ↓
TensorFlow
```

The Sandbox supports every stage of the Module 21 learning process.

---

# Author

**Clifford J. Ferraren**

MIT Professional Education  
Applied Data Science Program

**Module 21 Sandbox**