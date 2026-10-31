# Module 21: Glossary

## Accuracy
The ratio of correct predictions to the total number of predictions.

```text
Accuracy =
Correct Predictions / Total Predictions
```

---

## Actions
In reinforcement learning, an action is a decision taken by an agent that causes a transition from one state to another.

---

## Activation
A connection between neurons in a neural network.

---

## Activation Function
A mathematical function applied to neuron outputs to introduce non-linearity and normalize values.

Common examples:

- Sigmoid
- ReLU
- Tanh
- Sine

---

## Agent
The entity in reinforcement learning that interacts with the environment and learns through rewards and penalties.

---

## Artificial Neural Network (ANN)
A machine learning model inspired by the biological brain consisting of:

- Input Layer
- Hidden Layer(s)
- Output Layer

---

## Backward Propagation
The process of adjusting weights and biases after evaluating prediction errors to improve model performance.

---

## Bellman Equation
An equation used in reinforcement learning to update Q-values and estimate future rewards.

Used in:

- Q-Learning
- Reinforcement Learning

---

## Bias
A constant value added to a neuron's weighted sum to shift the output positively or negatively.

---

## Biological Neural Network
The network of neurons in the human brain consisting of:

- Dendrites
- Axons
- Synapses

which inspired artificial neural networks.

---

## Centroid
The center point of a cluster in the K-Means algorithm.

---

## Clustering
A process of grouping similar observations together.

Commonly used in:

- Unsupervised Learning
- Data Segmentation
- Pattern Discovery

---

## Clusters
Groups of data points that are more similar to each other than to points in other groups.

---

## Deep Neural Networks (DNNs)
Neural networks containing multiple hidden layers between the input and output layers.

Applications include:

- Image Recognition
- Speech Recognition
- Autonomous Vehicles
- Computer Vision

---

## Deep Q-Network (DQN)
A reinforcement learning algorithm that combines:

```text
Q-Learning
      +
Deep Neural Networks
```

to predict Q-values.

---

## Elbow Method
A technique used to determine the optimal number of clusters in K-Means.

---

## Elbow Point
The point where the SSE curve begins to level off, indicating the optimal number of clusters.

---

## Episode
A complete sequence of actions in reinforcement learning from a starting state to a terminal state.

---

## Expectation-Maximization Process
The iterative process used in K-Means:

### Expectation

Assign data points to the nearest centroid.

### Maximization

Recalculate centroid positions.

---

## Exploitation
Choosing the action with the highest known Q-value.

Goal:

```text
Maximize Reward
```

---

## Exploration
Choosing actions randomly to discover new states and rewards.

Goal:

```text
Learn New Information
```

---

## F1 Score
A performance metric that combines precision and recall.

Range:

```text
0 to 1
```

Higher values indicate better performance.

---

## Feature Scaling
The process of transforming variables to a common scale.

Examples:

- Standardization
- Normalization

---

## Forward Propagation
The process of sending inputs through a neural network to generate predictions.

---

## Gamma (γ)
The discount factor used in reinforcement learning.

Purpose:

```text
Balance
Current Rewards
and
Future Rewards
```

Typical values:

```text
0.80 - 0.99
```

---

## Hidden Layer
Intermediate layer(s) within a neural network responsible for feature extraction and transformation.

---

## Input Layer
The first layer of a neural network that receives raw data.

---

## K-Means Algorithm
An unsupervised clustering algorithm that partitions data into K clusters.

Basic Steps:

1. Select K clusters.
2. Initialize centroids.
3. Assign data points.
4. Recalculate centroids.
5. Repeat until convergence.

---

## Learning Rate (α)
A parameter in Q-Learning that controls how quickly Q-values are updated.

Higher values:

```text
Faster Learning
```

Lower values:

```text
Slower Learning
```

---

## Max Function
A function used in the Bellman Equation to identify the maximum future reward from available actions.

---

## Neurons
Individual processing units within a neural network.

Also called:

```text
Nodes
```

---

## Output Layer
The final layer of a neural network that produces predictions.

---

## Policy
The strategy an agent follows when selecting actions.

---

## Precision
Measures how many positive predictions were actually correct.

```text
Precision =
True Positives
─────────────
Predicted Positives
```

---

## Q-Learning Algorithm
A reinforcement learning algorithm that learns optimal actions by updating Q-values using the Bellman Equation.

Process:

```text
State
  ↓
Action
  ↓
Reward
  ↓
Q-Value Update
```

---

## Q-Values
Values stored within the Q-Matrix that estimate the quality of a specific state-action pair.

---

## Quality Matrix (Q-Matrix)
A table storing learned action values.

```text
Rows    = States
Columns = Actions
```

---

## Recall
Measures a model's ability to identify actual positive observations.

```text
Recall =
True Positives
────────────
Actual Positives
```

---

## Reinforcement Learning
A machine learning approach where agents learn through rewards and penalties while interacting with an environment.

---

## Reward Matrix
A table defining valid transitions and rewards between states.

---

## Reward
A numerical value used to encourage desirable behavior in reinforcement learning.

Examples:

```text
Positive Reward
      +
Penalty (Negative Reward)
```

---

## Sigmoid Function
A commonly used activation function that maps values between:

```text
0 and 1
```

making it useful for probabilities.

---

## SARSA
(State-Action-Reward-State-Action)

A reinforcement learning algorithm that learns based on the current policy.

Characteristics:

- On-policy
- More conservative than Q-Learning

---

## Specificity
Measures the proportion of true negatives correctly identified.

```text
Specificity =
True Negatives
─────────────
Actual Negatives
```

---

## States
The observations or positions an agent can occupy within an environment.

---

## Sum of Squared Errors (SSE)
A measure used by K-Means to evaluate cluster quality.

Lower SSE indicates:

```text
Better Clustering
```

---

## Supervised Learning
A machine learning approach using labeled training data with known outcomes.

Examples:

- Classification
- Regression

---

## TensorFlow
An open-source Python machine learning framework developed by Google.

Used for:

- Deep Learning
- Neural Networks
- Computer Vision
- Artificial Intelligence

---

## Unsupervised Learning
A machine learning approach using unlabeled data to discover hidden patterns.

Examples:

- Clustering
- Dimensionality Reduction

---

## Weight
A parameter within a neural network that determines the strength of a connection between neurons.

Characteristics:

- Positive weights increase influence.
- Negative weights decrease influence.

---

# Key Module 21 Concepts

## K-Means

```text
Data
 ↓
Clusters
 ↓
Centroids
 ↓
Elbow Method
```

---

## Reinforcement Learning

```text
State
 ↓
Action
 ↓
Reward
 ↓
Q-Matrix
 ↓
Learning
```

---

## Deep Neural Networks

```text
Input Layer
      ↓
Hidden Layer(s)
      ↓
Output Layer
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
Backward Propation
         ↓
Weight Updates
```