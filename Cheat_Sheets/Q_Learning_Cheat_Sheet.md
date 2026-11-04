# Q-Learning Cheat Sheet

## What is Q-Learning?

Q-Learning is a reinforcement learning algorithm that learns the best action to take in a particular state by maximizing future rewards.

Characteristics:

- Model-Free
- Off-Policy
- Reinforcement Learning Algorithm
- Uses a Q-Matrix
- Uses the Bellman Equation

---

# Goal of Q-Learning

```text
Current State
      ↓
Best Action
      ↓
Maximum Reward
```

The agent learns the optimal policy through trial and error.

---

# Key Components

## Agent

The decision-maker.

Examples:

- Robot
- Game Player
- Autonomous Vehicle

---

## Environment

The world in which the agent operates.

Examples:

- Frozen Lake
- Taxi-v4
- Maze
- Road Network

---

## State

The current situation of the agent.

Example:

```text
State 0
State 1
State 2
...
```

---

## Action

A move that transitions the agent from one state to another.

Examples:

```text
Left
Right
Up
Down
```

---

## Reward

Feedback received after taking an action.

Examples:

```text
Goal Reached = +100

Hole = 0

Invalid Move = -1
```

---

# Q-Matrix

The Q-Matrix stores learned action values.

Structure:

```text
Rows    = States
Columns = Actions
```

Example:

```text
         Left Right Up Down

State 0
State 1
State 2
```

Each cell contains:

```text
Expected Future Reward
```

---

# Q-Values

Q-values represent the quality of taking an action in a specific state.

Higher Q-value:

```text
Better Action
```

Lower Q-value:

```text
Worse Action
```

---

# Bellman Equation

Used to update Q-values.

Formula:

```text
Q(s,a) =
Q(s,a) + α[R + γ max(Q') - Q(s,a)]
```

---

# Variables

| Variable | Meaning |
|----------|----------|
| Q(s,a) | Current Q-Value |
| α | Learning Rate |
| R | Reward |
| γ | Discount Factor |
| max(Q') | Best Future Reward |

---

# Learning Rate (α)

Controls how quickly learning occurs.

Typical Range:

```text
0.1 - 0.9
```

Higher Value:

```text
Learn Faster
```

---

# Discount Factor (γ)

Balances:

```text
Immediate Reward

vs

Future Reward
```

Typical Range:

```text
0.80 - 0.99
```

---

# Exploration

Agent chooses random actions.

Purpose:

```text
Discover New Paths
```

Example:

```text
Unknown State
      ↓
Random Action
```

---

# Exploitation

Agent chooses the action with the highest Q-value.

Purpose:

```text
Maximize Reward
```

Example:

```text
Known State
      ↓
Best Action
```

---

# Exploration vs Exploitation

```text
Exploration
      ↓
Learn New Information

Exploitation
      ↓
Use Existing Knowledge
```

A balance between both is required.

---

# Episode

One complete attempt.

Example:

```text
Start
  ↓
Actions
  ↓
Goal
```

Each episode updates the Q-Matrix.

---

# Q-Learning Process

## Step 1

Select a state randomly.

```python
current_state = np.random.randint(0,n)
```

---

## Step 2

Find valid actions.

```python
playable_actions = []
```

---

## Step 3

Choose an action.

```python
next_state =
np.random.choice(playable_actions)
```

---

## Step 4

Receive reward.

```text
Reward Matrix
```

provides reward values.

---

## Step 5

Compute Temporal Difference (TD)

```text
Reward
   +
Future Reward
   -
Current Q
```

---

## Step 6

Update Q-Value

Using:

```text
Bellman Equation
```

---

## Step 7

Repeat

```text
Many Episodes
```

until learning stabilizes.

---

# Reward Matrix

Defines valid moves and rewards.

Example:

```text
State
   ↓
Action
   ↓
Reward
```

---

# Example

```python
rewards = np.array([
 [0,1,0],
 [1,0,1],
 [0,1,100]
])
```

Goal state:

```text
Reward = 100
```

---

# Python Q-Learning Example

Create Q-Matrix:

```python
Q = np.zeros((15,15))
```

---

# Update Q-Values

```python
Q[current_state,next_state] += (
    alpha * TD
)
```

---

# Find Best Action

```python
np.argmax(Q[state])
```

Returns:

```text
Highest Q-Value Action
```

---

# Policy

A policy is the strategy used by the agent.

Goal:

```text
Optimal Policy
```

Meaning:

```text
Best Action
For Every State
```

---

# Route Optimization Example

```text
L1
 ↓
L2
 ↓
L3
 ↓
Goal
```

Q-Learning discovers this route automatically.

---

# Advantages

✅ Learns Through Experience

✅ Does Not Need Labeled Data

✅ Finds Optimal Policies

✅ Adaptable

✅ Widely Used

---

# Disadvantages

❌ Requires Many Iterations

❌ Large State Spaces Can Be Slow

❌ Exploration Can Be Expensive

---

# Real-World Applications

## Autonomous Vehicles

```text
Current Location
       ↓
Best Route
```

---

## Robotics

```text
Obstacle Avoidance
```

---

## Gaming AI

```text
Strategic Decision Making
```

---

## Logistics

```text
Route Optimization
```

---

# Module 21 Exam Facts

### Q-Learning Type

```text
Reinforcement Learning
```

---

### Stores Information In

```text
Q-Matrix
```

---

### Uses

```text
Bellman Equation
```

---

### Starts By

```text
Picking a Random State
```

---

### Learns Through

```text
Rewards
and
Penalties
```

---

### Goal

```text
Find Optimal Policy
```

---

# Quick Review

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
  ↓
Learning
```