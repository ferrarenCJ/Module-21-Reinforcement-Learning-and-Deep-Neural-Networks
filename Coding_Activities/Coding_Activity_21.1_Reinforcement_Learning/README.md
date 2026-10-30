# Required Coding Activity 21.1: Reinforcement Learning

## Overview

This activity explores how Reinforcement Learning can improve decision-making compared to a random-action approach.

Using the Taxi-v4 environment from Gymnasium, a self-driving taxi agent is trained to:

1. Pick up a passenger.
2. Navigate to the correct destination.
3. Minimize penalties.
4. Minimize the number of steps taken.

The activity compares the performance of:

- Random Action Selection
- Q-Learning Reinforcement Learning

---

# Learning Outcomes

By completing this activity, students will be able to:

- Implement a Quality Matrix (Q-Matrix).
- Apply the Bellman Equation.
- Understand states, actions, and rewards.
- Train a reinforcement learning agent.
- Evaluate agent performance.
- Compare random behavior versus learned behavior.

---

# Environment

The activity uses:

```python
gymnasium.make("Taxi-v4")
```

The environment simulates a taxi operating within a:

```text
5 × 5 Grid
```

---

# State Space

The environment consists of:

```text
25 Taxi Positions

4 Passenger Locations

1 Passenger-In-Taxi State

4 Possible Destinations
```

Total states:

```text
5 × 5 × 5 × 4

= 500 States
```

---

# Action Space

The taxi has six possible actions:

| Action | Description |
|----------|----------|
| 0 | Move South |
| 1 | Move North |
| 2 | Move East |
| 3 | Move West |
| 4 | Pickup Passenger |
| 5 | Dropoff Passenger |

Total actions:

```text
6 Actions
```

---

# Reward Structure

## Successful Dropoff

```text
+20 Reward
```

---

## Illegal Pickup or Dropoff

```text
-10 Penalty
```

---

## Movement

```text
-1 Per Step
```

The objective is to maximize rewards while minimizing unnecessary actions.

---

# Activity Structure

## Part 1: Environment Setup

Topics:

- Taxi Environment
- State Space
- Action Space
- State Encoding
- Reward Matrix

Questions:

- Question 1
- Question 2
- Question 3

---

## Part 2: Random Agent

Topics:

- Random Action Selection
- Monte Carlo Exploration
- Performance Measurement

Question:

- Question 4

The taxi selects actions randomly:

```python
env.action_space.sample()
```

No learning occurs.

---

## Part 3: Reinforcement Learning

Topics:

- Q-Learning
- Bellman Equation
- Q-Matrix
- Exploration vs Exploitation

Questions:

- Question 5
- Question 6
- Question 7

---

# Q-Matrix

A Quality Matrix is defined as:

```python
q_table = np.zeros((500, 6))
```

Rows:

```text
States
```

Columns:

```text
Actions
```

Each entry stores the expected reward for a state-action pair.

---

# Bellman Equation

The Bellman Equation is used to update the Q-Matrix.

Conceptually:

```text
Updated Q-Value
      =
Current Reward
      +
Expected Future Reward
```

This allows the agent to learn optimal actions over many episodes.

---

# Training Parameters

```python
alpha = 0.1
gamma = 0.6
epsilon = 0.1
```

### Alpha

Learning Rate

Controls how quickly learning occurs.

---

### Gamma

Discount Factor

Controls the importance of future rewards.

---

### Epsilon

Exploration Rate

Balances:

```text
Exploration

vs

Exploitation
```

---

# Reinforcement Learning Workflow

```text
Current State
      ↓
Choose Action
      ↓
Receive Reward
      ↓
Update Q-Value
      ↓
Move to Next State
      ↓
Repeat
```

After thousands of episodes, the agent learns an optimal policy.

---

# Results

## Without Reinforcement Learning

Characteristics:

- Random decisions
- Large number of steps
- High penalties
- Inconsistent performance

---

## With Reinforcement Learning

Characteristics:

- Learned decisions
- Fewer steps
- Fewer penalties
- Improved efficiency

---

# Key Concepts

## State

The current condition of the environment.

---

## Action

A decision available to the agent.

---

## Reward

Feedback received after an action.

---

## Episode

A complete taxi trip.

---

## Q-Value

Expected future reward of performing an action from a state.

---

## Policy

The strategy used to select actions.

---

# Files

```text
Required_Coding_Activity_21.1.ipynb
README.md
```

---

# Key Takeaways

- Reinforcement learning improves performance through experience.
- Q-Learning uses a Q-Matrix to store action values.
- The Bellman Equation updates Q-values.
- Exploration and exploitation must be balanced.
- Reinforcement learning significantly outperforms random action selection.
- Learned policies reduce steps and penalties while maximizing rewards.