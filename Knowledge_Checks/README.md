# Module 21 Knowledge Checks

## Overview

This folder contains all knowledge checks, answer keys, notes, and study materials completed during Module 21.

The knowledge checks are designed to reinforce concepts learned throughout the module and provide an opportunity to assess understanding before completing the final assignment.

---

# Learning Objectives

The knowledge checks cover the following topics:

- Supervised Learning
- Unsupervised Learning
- K-Means Clustering
- Confusion Matrix
- Accuracy Metrics
- Reinforcement Learning
- Q-Learning
- Bellman Equation
- Deep Neural Networks
- TensorFlow
- Deep Dream

---

# Knowledge Checks Included

## Knowledge Check 21.1

### Introduction to Reinforcement Learning and Deep Neural Networks

Topics Covered:

- Reinforcement Learning Fundamentals
- States
- Actions
- Rewards
- Q-Matrix
- Bellman Equation
- Deep Neural Networks
- TensorFlow

---

## Knowledge Check 21.2

### Reinforcement Learning and Deep Neural Networks

Topics Covered:

- Reinforcement Learning Concepts
- Q-Learning Process
- Gamma (γ)
- Actions and States
- Neural Network Architecture
- Q-Matrix Structure
- TensorFlow
- Deep Neural Network Applications

Files:

```text
Knowledge_Check_21.2_Answers.md
```

---

# Core Concepts Reviewed

## Reinforcement Learning

```text
State
   ↓
Action
   ↓
Reward
   ↓
Learning
```

Key Concepts:

- Agent
- Environment
- States
- Actions
- Rewards
- Policies

---

## Q-Learning

```text
State
   ↓
Action
   ↓
Reward
   ↓
Bellman Update
   ↓
Q-Matrix Update
```

Key Concepts:

- Q-Matrix
- Bellman Equation
- Exploration
- Exploitation
- Optimal Policy

---

## Deep Neural Networks

Architecture:

```text
Input Layer
      ↓
Hidden Layer(s)
      ↓
Output Layer
```

Key Concepts:

- Neurons
- Activations
- Weights
- Biases
- Forward Propagation
- Backward Propagation

---

## TensorFlow

Primary Deep Learning Library:

```python
import tensorflow as tf
from tensorflow import keras
```

Applications:

- Image Recognition
- Computer Vision
- Deep Learning

---

# Important Formulas

## Accuracy

```text
Accuracy =
Correct Predictions
──────────────────
Total Predictions
```

---

## Precision

```text
Precision =
True Positives
──────────────
TP + FP
```

---

## Recall

```text
Recall =
True Positives
──────────────
TP + FN
```

---

## Bellman Equation

```text
Q(s,a) =
Q(s,a) + α[R + γ max(Q') - Q(s,a)]
```

Where:

```text
α = Learning Rate
γ = Discount Factor
R = Reward
```

---

# Study Tips

## Reinforcement Learning

Focus on:

- State
- Action
- Reward
- Q-Matrix
- Gamma (γ)
- Bellman Equation

---

## Deep Neural Networks

Memorize:

```text
Input Layer
Hidden Layer
Output Layer
```

and understand:

```text
Activation = Connection Between Neurons
```

---

## Q-Learning

Remember:

```text
The first step is to
pick a state randomly.
```

---

## TensorFlow

Remember:

```text
TensorFlow
```

is the Python library used for implementing deep neural networks.

---

# Folder Structure

```text
Knowledge_Checks/
│
├── README.md
│
├── Knowledge_Check_21.1/
│
└── Knowledge_Check_21.2_Reinforcement_Learning_and_Deep_Neural_Networks/
    └── Knowledge_Check_21.2_Answers.md
```

---

# Key Takeaways

✅ Reinforcement Learning learns through rewards and penalties.

✅ Actions move an agent from one state to another.

✅ A Q-Matrix contains states and actions.

✅ The Bellman Equation updates Q-values.

✅ Gamma (γ) balances current and future rewards.

✅ Deep Neural Networks contain input, hidden, and output layers.

✅ Activations are connections between neurons.

✅ TensorFlow is a popular deep learning framework.

✅ Image recognition is a common application of deep neural networks.

---

# Author

**Clifford J. Ferraren**

MIT Professional Education  
Applied Data Science Program

**Module 21 Knowledge Checks**