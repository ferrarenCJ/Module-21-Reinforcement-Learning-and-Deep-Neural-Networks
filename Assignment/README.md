# Required Final Assignment 21.1: Introduction to Reinforcement Learning and Deep Neural Networks

## Overview

This assignment applies concepts from Module 21 by implementing both a Machine Learning clustering algorithm and a Reinforcement Learning algorithm.

The assignment is divided into two parts:

1. **K-Means Clustering on the Titanic Dataset**
2. **Reinforcement Learning using the Bellman Equation and Q-Learning**

---

# Learning Outcomes

By completing this assignment, students will be able to:

- Implement K-Means using Scikit-Learn.
- Prepare and preprocess data for machine learning.
- Evaluate clustering model performance.
- Implement a Quality Matrix (Q-Matrix).
- Apply the Bellman Equation.
- Implement the fundamental steps of Reinforcement Learning.
- Use Q-Learning to identify optimal routes.

---

# Part 1: K-Means Algorithm

## Objective

Apply the K-Means clustering algorithm to the Titanic dataset to determine whether passengers survived the disaster.

Although K-Means is an unsupervised learning algorithm, it can be used to explore patterns within the data and compare model predictions with actual survival outcomes.

---

# Titanic Dataset

The dataset contains passenger information including:

| Column | Description |
|----------|----------|
| PassengerId | Unique Passenger Identifier |
| Survived | Survival Indicator (0 = No, 1 = Yes) |
| Pclass | Passenger Class |
| Name | Passenger Name |
| Sex | Gender |
| Age | Age |
| SibSp | Number of Siblings/Spouses |
| Parch | Number of Parents/Children |
| Ticket | Ticket Number |
| Fare | Ticket Fare |
| Cabin | Cabin Number |
| Embarked | Port of Embarkation |

---

# Data Preparation Steps

## Load Data

```python
pd.read_csv()
```

Files:

```text
train.csv
test.csv
```

---

## Explore Data

Tasks:

- View sample records
- Calculate descriptive statistics
- Identify missing values

Functions used:

```python
head()
describe()
isna().sum()
```

---

## Data Cleaning

Tasks:

- Fill missing numeric values
- Remove unnecessary columns
- Encode categorical values

Columns removed:

```text
Name
Ticket
Cabin
Embarked
```

---

## Label Encoding

The `Sex` column is encoded as:

```text
Female = 0
Male = 1
```

using:

```python
LabelEncoder()
```

---

## Feature Creation

Training Features:

```python
X_train
```

Test Features:

```python
X_test
```

Training Labels:

```python
y_train
```

Test Labels:

```python
y_test
```

---

# K-Means Model

## Configuration

```python
from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters=2,
    random_state=42
)
```

Two clusters were used because the target variable contains:

```text
0 = Did Not Survive
1 = Survived
```

---

# Model Evaluation

Predictions generated:

```python
y_pred = kmeans.predict(X_test)
```

Model accuracy evaluated by comparing:

```text
y_pred

vs

y_test
```

---

# Performance Improvements

Additional improvements explored:

## Feature Scaling

```python
StandardScaler
```

Benefits:

- Prevents large numeric values from dominating clustering
- Improves cluster formation

---

## Multiple Initializations

```python
n_init = 50
```

Benefits:

- More stable clustering results
- Better convergence

---

# Part 2: Reinforcement Learning

## Objective

Train a robot to navigate through a building consisting of 15 rooms and determine optimal routes between locations.

---

# Room Layout

Locations:

```text
L1  - L15
```

Each room is represented as a state within the environment.

---

# Reward Matrix

A rewards matrix captures valid room transitions.

Example:

```text
State
   ↓
Action
   ↓
Reward
```

Connected rooms receive a positive reward while invalid moves receive zero reward.

---

# Actions

The system defines:

```python
actions = list(range(1,16))
```

representing all 15 rooms.

---

# State Mapping

Two dictionaries are used:

```python
location_to_state
```

and

```python
state_to_location
```

These provide conversions between room labels and numeric states.

---

# Bellman Equation

The Bellman Equation updates Q-values through:

```text
Current Reward
      +
Future Reward
      ↓
New Q-Value
```

Formula:

```text
Q(s,a)
=
Q(s,a)
+
α[R + γ max(Q') - Q(s,a)]
```

---

# Hyperparameters

## Alpha

```python
alpha = 0.9
```

Learning Rate

---

## Gamma

```python
gamma = 0.75
```

Discount Factor

---

# Q-Learning Process

```text
Random State
      ↓
Valid Action
      ↓
Reward
      ↓
Bellman Update
      ↓
Update Q-Matrix
```

The process repeats over many training iterations.

---

# Optimal Route Calculations

Routes generated:

## Question 15a

```text
L1 → L15
```

---

## Question 15b

```text
L9 → L1
```

---

## Question 15c

```text
L6 → L1
```

The trained Q-Matrix identifies the most efficient path between locations.

---

# Key Concepts

## Machine Learning

- K-Means
- Clustering
- Feature Engineering
- Data Cleaning
- Model Evaluation

---

## Reinforcement Learning

- State
- Action
- Reward
- Q-Matrix
- Bellman Equation
- Optimal Policy

---

# Files Included

```text
Module21_FinalAssignment_Student.ipynb
README.md

data/
├── train.csv
└── test.csv

finalAssignmentImg.png
```

---

# Key Takeaways

- K-Means can be used to explore patterns within survival data.
- Data preprocessing is critical to model performance.
- Feature scaling can improve clustering quality.
- Reinforcement learning learns through rewards and penalties.
- The Q-Matrix stores learned action values.
- The Bellman Equation updates Q-values using immediate and future rewards.
- Q-Learning can identify optimal paths without explicitly programming routes.
- Reinforcement learning provides an effective framework for sequential decision-making problems.

---

# Author

**Clifford J. Ferraren**

MIT Professional Education  
Applied Data Science Program

**Module 21 Final Assignment**