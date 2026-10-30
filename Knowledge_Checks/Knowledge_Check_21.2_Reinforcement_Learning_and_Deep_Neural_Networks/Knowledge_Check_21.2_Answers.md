# Self-Study Knowledge Check 21.2: Reinforcement Learning and Deep Neural Networks

## Overview

**Learning Outcome Addressed**

- Identify key components of reinforcement learning and deep neural networks.

**Questions:** 9  
**Points:** 0 (Self-Study)  
**Attempts:** Unlimited

---

# Question 1

## Which of the following is correct about reinforcement learning?

### ✅ Correct Answer

```text
Reinforcement learning is an unsupervised machine learning approach
which gives rewards for correct decisions and penalties for
nonoptimal choices.
```

### Key Concept

Reinforcement learning improves decision-making by rewarding desirable actions and penalizing undesirable actions.

---

# Question 2

## What is an action in reinforcement learning?

### ✅ Correct Answer

```text
In reinforcement learning, moving from one state to another is called an action.
```

### Key Concept

An action is a decision made by the agent that causes a transition from one state to another.

---

# Question 3

## What are the three layers of neurons in deep neural networks?

### ✅ Correct Answer

```text
The three layers of neurons in deep neural networks
are the input layer, the hidden layer, and the output layer.
```

### Key Concept

```text
Input Layer
      ↓
Hidden Layer(s)
      ↓
Output Layer
```

---

# Question 4

## What does a Quality Matrix (Q-Matrix) consist of?

### ✅ Correct Answer

```text
A Q-matrix consists of a row for each possible state and
a corresponding column for each possible action at that state.
```

### Key Concept

```text
Rows = States

Columns = Actions
```

Each cell stores a Q-value representing the expected future reward.

---

# Question 5

## Which Python library can be used to implement deep neural network algorithms?

### ✅ Correct Answer

```text
TensorFlow
```

### Key Concept

TensorFlow is Google's deep learning framework used to build and train neural networks.

Example:

```python
import tensorflow as tf
from tensorflow import keras
```

---

# Question 6

## What is the significance of Gamma (γ) in the Q-Learning process?

### ✅ Correct Answer

```text
Gamma (γ) is a discount factor that is used to balance current and future rewards.
```

### Key Concept

- High Gamma → Values future rewards more.
- Low Gamma → Focuses more on immediate rewards.

Common values:

```text
0.80 - 0.99
```

---

# Question 7

## Which of the following is the first step in the Q-Learning process?

### ✅ Correct Answer

```text
The first step in the Q-learning process is to pick a state randomly.
```

### Key Concept

Q-Learning begins by exploring the environment.

Process:

```text
Pick State
    ↓
Choose Action
    ↓
Receive Reward
    ↓
Update Q-Matrix
```

---

# Question 8

## In deep neural networks, what is an activation?

### ✅ Correct Answer

```text
In deep neural networks, an activation is a connection
between neurons, represented by the arrows between the layers.
```

### Key Concept

```text
Neuron
   ↓ Activation
Neuron
```

Activations transfer information throughout the network.

---

# Question 9

## Which of the following is an application of deep neural networks?

### ✅ Correct Answer

```text
Image recognition
```

### Key Concept

The lesson specifically used the MNIST handwritten digit recognition example as an application of deep neural networks.

Examples:

- Image Recognition
- Handwritten Digit Recognition
- Computer Vision

---

# Answer Summary

| Question | Correct Answer |
|-----------|---------------|
| Q1 | Reinforcement learning is an unsupervised machine learning approach which gives rewards for correct decisions and penalties for nonoptimal choices. |
| Q2 | Moving from one state to another is called an action. |
| Q3 | Input layer, hidden layer, and output layer. |
| Q4 | A Q-matrix consists of a row for each state and a column for each action. |
| Q5 | TensorFlow |
| Q6 | Gamma is a discount factor that balances current and future rewards. |
| Q7 | Pick a state randomly. |
| Q8 | An activation is a connection between neurons. |
| Q9 | Image recognition |

---

# Key Module 21 Concepts

## Reinforcement Learning

```text
State
   ↓
Action
   ↓
Reward
   ↓
Q-Matrix Update
```

Topics:

- States
- Actions
- Rewards
- Q-Learning
- Bellman Equation
- Exploration vs Exploitation

---

## Deep Neural Networks

```text
Input Layer
      ↓
Hidden Layer(s)
      ↓
Output Layer
```

Topics:

- Neurons
- Activations
- Weights
- Biases
- Forward Propagation
- Backward Propagation
- TensorFlow
- Image Recognition

---

## Final Score

```text
9 / 9 Correct
```