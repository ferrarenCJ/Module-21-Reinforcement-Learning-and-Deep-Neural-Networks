# Required Coding Activity 21.1: Reinforcement Learning

## Activity Overview

**Learning Outcomes Addressed**

- Implement the Quality Matrix (Q-Matrix) and the Bellman Equation.
- Implement the fundamental steps of Reinforcement Learning.

**Points:** 20  
**Submission Type:** Jupyter Notebook Upload  
**Estimated Time:** 75 Minutes

---

# Objective

In this activity, a reinforcement learning agent is trained to operate a self-driving taxi.

The goal is to:

1. Pick up a passenger.
2. Transport the passenger.
3. Drop off the passenger at the correct destination.
4. Minimize steps and penalties.

The activity compares:

- Random decision-making (no reinforcement learning)
- Q-Learning (reinforcement learning)

---

# Problem Setup

## Environment

The Taxi-v4 environment contains:

```text
5 x 5 Grid
```

Resulting in:

```text
25 Taxi Locations
```

Possible passenger locations:

```text
R (Red)
G (Green)
Y (Yellow)
B (Blue)
```

Plus:

```text
Passenger in Taxi
```

Total states:

```text
5 × 5 × 4 × 5 = 500 States
```

---

# Actions

The taxi can perform:

```text
0 = South
1 = North
2 = East
3 = West
4 = Pickup
5 = Dropoff
```

Total actions:

```text
6 Actions
```

---

# Rewards

## Successful Dropoff

```text
+20
```

---

## Illegal Pickup/Dropoff

```text
-10
```

---

## Normal Movement

```text
-1
```

The reward system encourages efficient behavior.

---

# Part 1: Environment Setup

## Install Package

```bash
pip install gymnasium
```

---

## Create Environment

```python
import gymnasium

env = gymnasium.make("Taxi-v4").env

obs, info = env.reset(seed=0)
```

---

# Question 1

## Display State Space

### Solution

```python
print("State Space {}".format(env.observation_space))
```

Output:

```text
Discrete(500)
```

---

# Question 2

## Encode Taxi Environment

### Solution

```python
taxi_row, taxi_column, passenger_index, destination_index = 0, 0, 3, 0

state = env.unwrapped.encode(
    taxi_row,
    taxi_column,
    passenger_index,
    destination_index
)
```

---

# Question 3

## Display Transition Probabilities

### Solution

```python
env.unwrapped.P[state]
```

The dictionary contains:

```text
Action
↓
Probability
↓
Next State
↓
Reward
↓
Done Flag
```

---

# Part 2: Without Reinforcement Learning

The taxi selects actions randomly.

Example:

```python
action = env.action_space.sample()
```

No learning occurs.

---

# Question 4

## Written Response

```text
The infinite while loop ends when the variable done becomes True. This occurs when the passenger has been successfully dropped off at the correct destination, causing either the terminated or truncated condition returned by env.step() to become True. Once done is True, the loop exits and the program displays the results.
```

---

# Observations

Random actions cause:

- Many unnecessary movements
- Large numbers of penalties
- Inconsistent performance

---

# Part 3: Reinforcement Learning

Q-Learning introduces a Quality Matrix.

The Q-Matrix stores:

```text
State + Action
       ↓
Expected Reward
```

---

# Question 5

## Create Q-Matrix

### Solution

```python
import numpy as np

q_table = np.zeros((500, 6))
```

Dimensions:

```text
500 States
6 Actions
```

---

# Training Parameters

## Alpha (Learning Rate)

```python
alpha = 0.1
```

Controls how quickly learning occurs.

---

## Gamma (Discount Factor)

```python
gamma = 0.6
```

Controls the importance of future rewards.

---

## Epsilon (Exploration Rate)

```python
epsilon = 0.1
```

Balances exploration and exploitation.

---

# Bellman Equation

The Q-Matrix is updated using:

```text
Q(s,a) =
(1 - α)Q(s,a)
+
α[R + γ max(Q')]
```

This allows future rewards to influence current decisions.

---

# Question 6

## Written Response

```text
The main difference between Part 3 and Part 2 is that Part 3 uses reinforcement learning through a Quality Matrix, while Part 2 selects actions randomly and does not learn from previous experiences. The reinforcement learning agent stores information about rewards and continuously improves its decision-making over time.

The Bellman Equation is used to train the model and update the entries of the Quality Matrix. The equation combines the immediate reward from an action with the expected future rewards, allowing the agent to learn optimal actions through repeated episodes.
```

---

# Q-Learning Process

```text
State
   ↓
Action
   ↓
Reward
   ↓
Bellman Update
   ↓
Q-Matrix
   ↓
Learning
```

---

# Evaluation

After training:

```python
action = np.argmax(q_table[state])
```

The taxi selects the action with the highest expected reward.

---

# Question 7

## Written Response

```text
The reinforcement learning approach performed significantly better than the random-action approach. In Part 2, actions were selected randomly, resulting in many unnecessary steps and penalties before successfully completing the task. Since no learning occurred, the performance remained inconsistent.

In Part 3, the Q-Learning algorithm used the Quality Matrix to choose actions with the highest expected rewards. After training, the taxi completed tasks in fewer steps and incurred fewer penalties. The reinforcement learning model was more efficient because it learned from previous experiences and continuously improved its performance.
```

---

# Results Comparison

## Random Strategy

```text
Random Actions
      ↓
Many Steps
      ↓
Many Penalties
```

---

## Q-Learning Strategy

```text
Learned Actions
      ↓
Fewer Steps
      ↓
Fewer Penalties
```

---

# Key Takeaways

- Reinforcement learning improves performance through experience.
- The Taxi-v4 environment contains 500 states and 6 actions.
- The Q-Matrix stores learned action values.
- The Bellman Equation updates Q-values.
- Alpha controls learning speed.
- Gamma controls future reward importance.
- Epsilon balances exploration and exploitation.
- Q-Learning significantly outperforms random action selection.
- Reinforcement learning minimizes penalties and improves efficiency.

---

# Study Notes

## Reinforcement Learning Cycle

```text
State
   ↓
Action
   ↓
Reward
   ↓
Bellman Equation
   ↓
Q-Matrix Update
   ↓
Improved Policy
```

## Remember

```text
Without RL
     ↓
Random Decisions

With RL
     ↓
Learned Decisions
```