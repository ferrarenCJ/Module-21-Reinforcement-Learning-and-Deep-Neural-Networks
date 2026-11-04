# Module 21 Coding Activities

## Overview

This folder contains all coding activities completed during Module 21.

The activities focus on applying machine learning, reinforcement learning, deep learning, and Python programming concepts through hands-on exercises.

---

# Learning Objectives

By completing these coding activities, students practiced:

- Implementing K-Means clustering
- Evaluating machine learning models
- Building confusion matrices
- Applying reinforcement learning concepts
- Implementing Q-Learning algorithms
- Using the Bellman Equation
- Working with Gymnasium environments
- Building Deep Neural Networks
- Using TensorFlow and Keras
- Applying Deep Dream image processing

---

# Coding Activities Included

## Activity 21.1: K-Means Clustering

### Topics

- Unsupervised Learning
- Clustering
- Centroids
- Feature Scaling
- Elbow Method

### Skills Practiced

```python
from sklearn.cluster import KMeans
```

```python
kmeans.fit(X)
```

```python
kmeans.predict(X)
```

---

## Activity 21.2: Confusion Matrix and Model Evaluation

### Topics

- Accuracy
- Precision
- Recall
- Specificity
- F1 Score

### Skills Practiced

```python
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score
)
```

---

## Activity 21.3: Introduction to Reinforcement Learning

### Topics

- States
- Actions
- Rewards
- Policies

### Skills Practiced

```text
State
  ↓
Action
  ↓
Reward
```

---

## Activity 21.4: Q-Learning

### Topics

- Q-Matrix
- Bellman Equation
- Exploration
- Exploitation

### Skills Practiced

```python
Q = np.zeros((states, actions))
```

```python
np.argmax(Q[state])
```

---

## Activity 21.5: Frozen Lake Environment

### Topics

- OpenAI Gymnasium
- Frozen Lake
- Navigation Problems
- Reinforcement Learning

### Skills Practiced

```python
import gymnasium as gym
```

```python
env = gym.make("FrozenLake-v1")
```

---

## Activity 21.6: Deep Neural Networks

### Topics

- Neural Network Architecture
- Forward Propagation
- Backward Propagation
- Activation Functions

### Skills Practiced

```python
import tensorflow as tf
```

```python
from tensorflow import keras
```

---

## Activity 21.7: MNIST Digit Recognition

### Topics

- Image Recognition
- Handwritten Digits
- TensorFlow
- Deep Learning

### Skills Practiced

```python
model.fit()
```

```python
model.evaluate()
```

---

## Activity 21.8: Deep Dream

### Topics

- Deep Learning Visualization
- Feature Amplification
- Neural Network Interpretation

### Skills Practiced

```text
Image
  ↓
Feature Detection
  ↓
Feature Amplification
  ↓
Dream-Like Output
```

---

# Key Technologies

## Python

Primary programming language used throughout the module.

---

## NumPy

Used for:

- Arrays
- Mathematical Operations
- Matrix Manipulation

---

## Pandas

Used for:

- DataFrames
- Data Cleaning
- Data Analysis

---

## Scikit-Learn

Used for:

- K-Means
- Model Evaluation
- Data Preprocessing

---

## Gymnasium

Used for:

- Reinforcement Learning Environments
- Frozen Lake
- Agent Training

---

## TensorFlow

Used for:

- Neural Networks
- Deep Learning
- Image Recognition

---

# Key Takeaways

✅ K-Means is an unsupervised clustering algorithm.

✅ Confusion matrices help evaluate model performance.

✅ Reinforcement learning learns from rewards and penalties.

✅ Q-Learning uses the Bellman Equation to update Q-values.

✅ Frozen Lake is a useful environment for learning reinforcement learning.

✅ Deep Neural Networks contain input, hidden, and output layers.

✅ TensorFlow provides powerful tools for deep learning applications.

✅ Deep Dream helps visualize what neural networks learn from images.

---

# Module 21 Activity Summary

```text
K-Means
    ↓
Model Evaluation
    ↓
Reinforcement Learning
    ↓
Q-Learning
    ↓
Frozen Lake
    ↓
Deep Neural Networks
    ↓
TensorFlow
    ↓
Deep Dream
```

---

# Author

**Clifford J. Ferraren**

MIT Professional Education  
Applied Data Science Program

**Module 21 Coding Activities**