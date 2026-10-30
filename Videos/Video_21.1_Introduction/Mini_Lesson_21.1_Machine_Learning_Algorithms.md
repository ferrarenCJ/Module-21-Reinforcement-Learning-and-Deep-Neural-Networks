# Mini-Lesson 21.1: Machine Learning Algorithms

---

# Overview

Machine Learning (ML) is a problem-solving approach that allows computers to learn patterns from data rather than relying entirely on explicitly programmed instructions.

Instead of defining every rule required to solve a problem, machine learning algorithms analyze large quantities of data and discover patterns that can be used to generate predictions or decisions.

As computing power has continued to increase, machine learning has become more practical and widespread across a variety of industries.

Examples of data sources used in machine learning include:

- Data warehouses
- Sensors
- Images
- Audio recordings
- Transaction records
- Real-time streaming data

---

# Training Data

Machine learning algorithms require a dataset called **training data**.

Training data is used to teach the algorithm how to recognize patterns and relationships within the data.

The algorithm analyzes the characteristics of the training data and creates a model that can later be used to make predictions or decisions.

---

# Categories of Machine Learning

Machine learning can generally be divided into two primary categories:

## Supervised Learning

In supervised learning, the training dataset contains an **answer key**.

Because the correct answers are already known during training, the algorithm can compare its predictions against the correct outcomes and continuously improve its performance.

### Characteristics

- Uses labeled data
- Known outputs exist
- Suitable for prediction and classification problems
- Model learns from examples with correct answers

### Examples

- Email spam detection
- Credit risk classification
- House price prediction
- Image recognition

---

## Unsupervised Learning

In unsupervised learning, the training dataset does **not** contain answer labels.

The algorithm must independently discover patterns, relationships, or structures within the data.

### Characteristics

- Uses unlabeled data
- No answer key is provided
- Finds hidden patterns
- Discovers similarities and differences

### Examples

- Customer segmentation
- Market basket analysis
- Cluster analysis
- Anomaly detection

---

# Reinforcement Learning

Reinforcement Learning (RL) is a type of machine learning focused on learning the optimal sequence of actions needed to achieve a desired objective.

An agent interacts with an environment, receives feedback, and learns from experience.

The goal is to maximize rewards while minimizing penalties.

---

## Frozen Lake Example

A common reinforcement learning example is the **Frozen Lake** problem.

Objective:

```text
Agent
  ↓
Navigate across frozen lake
  ↓
Avoid holes
  ↓
Reach destination
```

The agent explores different possible paths.

Over time, the algorithm learns:

- Which decisions lead to success
- Which decisions result in failure
- Which path produces the highest reward

Eventually, the algorithm identifies the shortest and most optimal route.

---

# What Defines Reinforcement Learning?

Several characteristics distinguish reinforcement learning from other machine learning techniques.

## 1. Initial Input State

The model begins from a starting position or state.

## 2. Large Number of Possible Outputs

Many possible decisions or paths may exist.

## 3. Rewards and Penalties

The agent receives feedback based on its actions.

Examples:

```text
Correct Move  → Reward

Incorrect Move → Penalty
```

## 4. Highest Reward Wins

The optimal solution is determined by maximizing rewards.

## 5. Continuous Learning

The model can continue improving over time as additional experiences are collected.

## 6. Dependent Decisions

Future decisions often depend on previous actions.

This means reinforcement learning frequently focuses on sequences of actions rather than isolated decisions.

---

# Reinforcement Learning Applications

Reinforcement learning is widely used in situations where learning occurs through interactions with an environment.

Common applications include:

- Industrial automation
- Robotics
- Autonomous systems
- Machine learning optimization
- Educational recommendation systems
- Interactive decision-making systems

---

# Neural Networks

Neural networks are a type of supervised machine learning algorithm inspired by biological neural systems.

Neural networks are designed to imitate the structure and behavior of neurons found in the human brain.

They consist of many interconnected processing units called **nodes**.

Each node:

1. Receives input values
2. Processes information
3. Produces an output

---

# Biological vs Artificial Neural Networks

## Biological Neural Networks

Components:

- Dendrites
- Axons
- Synapses

Process:

```text
Input Signal
      ↓
Dendrites
      ↓
Neuron
      ↓
Synapse
      ↓
Next Neuron
```

Key characteristic:

- Approximately 10¹¹ neurons

---

## Artificial Neural Networks

Components:

- Nodes
- Inputs
- Outputs
- Weights
- Biases

Process:

```text
Input Layer
      ↓
Hidden Layer(s)
      ↓
Output Layer
```

Key characteristic:

- Typically around 10⁴ artificial neurons

---

# Neural Network Layers

## Input Layer

Receives external information.

Examples:

- Images
- Text
- Sensor readings
- Numerical data

---

## Hidden Layer

Extracts patterns and features from the data.

Tasks include:

- Pattern recognition
- Feature extraction
- Noise reduction

---

## Output Layer

Produces the final prediction or decision.

Examples:

```text
Dog
Cat
Car
```

or

```text
Fraud
Not Fraud
```

---

# Weights and Biases

Neural networks use:

## Weights

Control the importance of signals.

```text
Higher Weight → More Influence
Lower Weight → Less Influence
```

## Biases

Shift the output of a neuron and improve learning flexibility.

Together, weights and biases allow the model to learn complex relationships within data.

---

# Advantages of Neural Networks

## 1. Flexible Data Representation

Data can be represented as:

- Discrete values
- Continuous values
- Vectors
- Multi-dimensional arrays

### Example

Images can be converted into:

```text
X Coordinate
Y Coordinate
Pixel Color
Pixel Brightness
```

before being processed by a neural network.

---

## 2. Robustness to Noise

Neural networks can tolerate:

- Missing values
- Data errors
- Outliers

Because training normally occurs across very large datasets, small errors typically do not significantly impact performance.

---

# Real-World Applications of Neural Networks

Common use cases include:

- Visual interpretation
- Computer vision
- Speech recognition
- Robotics control
- Image enhancement
- Trend detection
- Predictive analytics

---

# Key Takeaways

- Machine learning learns patterns from data rather than following explicit programming instructions.
- Machine learning can be categorized into supervised and unsupervised learning.
- Supervised learning uses labeled training data.
- Unsupervised learning uses unlabeled training data.
- Reinforcement learning focuses on maximizing rewards through experience.
- Neural networks are inspired by biological neurons.
- Artificial neural networks contain input, hidden, and output layers.
- Weights and biases control learning inside neural networks.
- Neural networks are widely used for image recognition, speech processing, robotics, and predictive analytics.

---

# Study Notes

## Remember

```text
Supervised Learning
    ↓
Uses Labels

Unsupervised Learning
    ↓
No Labels

Reinforcement Learning
    ↓
Rewards & Penalties

Neural Networks
    ↓
Input → Hidden → Output
```

## Important Concepts for This Module

- Supervised Learning
- Unsupervised Learning
- K-Means Clustering
- Reinforcement Learning
- States
- Actions
- Rewards
- Q-Matrix
- Bellman Equation
- Neural Networks
- Deep Neural Networks