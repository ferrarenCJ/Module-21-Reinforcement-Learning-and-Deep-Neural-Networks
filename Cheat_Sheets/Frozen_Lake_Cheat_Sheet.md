# Frozen Lake Cheat Sheet

## What is Frozen Lake?

Frozen Lake is a reinforcement learning environment commonly used to teach:

- Reinforcement Learning
- Q-Learning
- Exploration vs Exploitation
- Policy Optimization

The goal is to navigate across a frozen lake without falling into holes.

---

# Environment Layout

Typical 4x4 Frozen Lake:

```text
S F F F
F H F H
F F F H
H F F G
```

---

# Legend

| Symbol | Meaning |
|----------|----------|
| S | Start |
| F | Frozen Surface |
| H | Hole |
| G | Goal |

---

# Objective

```text
Start
  ↓
Avoid Holes
  ↓
Reach Goal
```

---

# Reinforcement Learning Components

## Agent

The player navigating the lake.

---

## Environment

The Frozen Lake game board.

---

## State

The agent's current location.

---

## Actions

Possible moves:

```text
Left
Right
Up
Down
```

---

## Reward

Typical rewards:

### Reach Goal

```text
Reward = +1
```

### Fall into Hole

```text
Reward = 0
```

### Other Moves

```text
Reward = 0
```

---

# State Space

Each square represents a state.

Example:

```text
4 × 4 Grid

16 States
```

---

# Action Space

```text
0 = Left
1 = Down
2 = Right
3 = Up
```

---

# Frozen Lake Workflow

```text
Current State
       ↓
Choose Action
       ↓
Move
       ↓
Receive Reward
       ↓
Update Q-Value
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
Update Q-Matrix
```

---

# Q-Matrix Structure

```text
Rows    = States
Columns = Actions
```

Example:

```text
         Left Down Right Up

State 0
State 1
State 2
...
```

---

# Bellman Equation

Used to update Q-values:

```text
Q(s,a) =
Q(s,a) + α[R + γ max(Q') - Q(s,a)]
```

---

# Variables

| Symbol | Meaning |
|----------|----------|
| α | Learning Rate |
| γ | Discount Factor |
| R | Immediate Reward |
| Q | Q-Value |

---

# Learning Rate (α)

Controls how quickly learning occurs.

Typical value:

```text
0.1
```

---

# Discount Factor (γ)

Balances:

```text
Current Reward

vs

Future Reward
```

Typical value:

```text
0.95
```

---

# Exploration

Agent chooses random actions.

Purpose:

```text
Discover New States
```

Example:

```text
Unknown Environment
       ↓
Random Moves
       ↓
Learn Rewards
```

---

# Exploitation

Agent chooses actions with highest Q-values.

Purpose:

```text
Maximize Reward
```

Example:

```text
Known Environment
       ↓
Best Learned Move
```

---

# Training Episodes

The agent learns by repeatedly playing the game.

```text
Episode 1
Fail

Episode 10
Partial Success

Episode 1000
Optimal Policy
```

---

# Optimal Policy

After training:

```text
State
   ↓
Highest Q-Value
   ↓
Best Action
```

This produces the shortest and safest route.

---

# Python Example

Create Environment:

```python
import gymnasium as gym

env = gym.make("FrozenLake-v1")
```

---

# Create Q-Table

```python
import numpy as np

q_table = np.zeros(
    (env.observation_space.n,
     env.action_space.n)
)
```

---

# Select Best Action

```python
action = np.argmax(
    q_table[state]
)
```

---

# Update Q-Value

```python
q_table[state, action] += alpha * (
    reward +
    gamma * np.max(q_table[next_state])
    -
    q_table[state, action]
)
```

---

# Real-World Applications

Frozen Lake models many real-world navigation problems.

Examples:

## Autonomous Vehicles

```text
Current Location
       ↓
Avoid Hazards
       ↓
Reach Destination
```

---

## Robotics

```text
Navigate Environment
       ↓
Avoid Obstacles
```

---

## Logistics

```text
Route Optimization
```

---

# Key Concepts to Remember

## State

Current position.

---

## Action

Movement decision.

---

## Reward

Feedback for actions.

---

## Episode

One complete attempt.

---

## Exploration

Learn new possibilities.

---

## Exploitation

Use known information.

---

## Q-Matrix

Stores action values.

---

## Bellman Equation

Updates Q-values.

---

# Module 21 Exam Facts

### Frozen Lake Teaches

✅ Reinforcement Learning

✅ Q-Learning

✅ Exploration

✅ Exploitation

✅ Policy Optimization

---

### Goal

```text
Reach Goal
Avoid Holes
Maximize Rewards
```

---

### Core Process

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

### Outcome

```text
Optimal Policy
Optimal Path
Improved Decisions
```