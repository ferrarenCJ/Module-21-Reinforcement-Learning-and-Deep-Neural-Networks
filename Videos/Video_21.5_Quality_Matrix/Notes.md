# Video 21.5: Reinforcement Learning - The Quality Matrix and the Bellman Equation

**Duration:** 10:36

---

# Overview

In this video, Dr. Williams expands on the Reward Matrix introduced in Video 21.4 and introduces the **Quality Matrix (Q-Matrix)** and the **Bellman Equation**.

These concepts form the foundation of Q-Learning and allow reinforcement learning agents to determine which actions produce the greatest long-term reward.

---

# Review: Reward Matrix

The Reward Matrix (R-Matrix) stores the immediate rewards associated with moving between states.

Example:

```text
State A → State B = Reward 0

State B → Goal = Reward 100
```

The reward matrix answers:

```text
What reward do I receive
for taking this action?
```

However, it does not indicate whether an action is optimal when future rewards are considered.

---

# What is a Quality Matrix (Q-Matrix)?

The Quality Matrix stores the expected value of performing an action from a given state.

Unlike the Reward Matrix:

```text
Reward Matrix
    ↓
Immediate Rewards
```

The Q-Matrix stores:

```text
Long-Term Rewards
```

The Q-Matrix helps an agent determine which actions will lead to the highest cumulative reward.

---

# Q-Matrix Structure

Rows represent:

```text
States
```

Columns represent:

```text
Actions
```

Example:

```text
             Actions

          A1   A2   A3

State 1    0    0   80

State 2   10    0  100

State 3    0   40    0
```

Each value represents the quality of taking a specific action from a given state.

---

# Interpreting Q-Values

A higher Q-value indicates a more desirable action.

Example:

```text
Current State

Move Left  = 25

Move Right = 90
```

The agent chooses:

```text
Move Right
```

because:

```text
90 > 25
```

---

# Purpose of the Q-Matrix

The Q-Matrix allows the agent to:

- Learn from experience
- Compare available actions
- Estimate future rewards
- Discover optimal paths

---

# Bellman Equation

The Bellman Equation is used to update the values stored in the Q-Matrix.

It combines:

- Current reward
- Future reward potential

to improve decision making over time.

---

# Bellman Equation Components

## Current Q-Value

```text
Q(s,a)
```

Current estimate of the action's value.

---

## Learning Rate (α)

Controls how much newly discovered information influences learning.

### High Alpha

```text
Fast Learning
```

### Low Alpha

```text
Slow Learning
```

---

## Reward (R)

Immediate reward received after performing an action.

Example:

```text
Goal Reached = +100

Invalid Move = -10
```

---

## Discount Factor (γ)

Controls the importance of future rewards.

Typical values:

```text
0.80 - 0.99
```

### High Gamma

Future rewards become more important.

### Low Gamma

Immediate rewards become more important.

---

## Maximum Future Q-Value

```text
max(Q')
```

Represents the best possible future reward available from the next state.

---

# Bellman Equation Concept

The Bellman Equation updates the current action value using:

```text
Current Reward
      +
Expected Future Reward
```

This allows future opportunities to influence present decisions.

---

# Example

Suppose the agent receives:

```text
Immediate Reward = 50
```

and discovers:

```text
Future Reward = 100
```

The Bellman Equation increases the current Q-value because a promising future path exists.

---

# Building the Q-Matrix

The learning process follows:

```text
Initialize Q-Matrix
       ↓
Select Action
       ↓
Observe Reward
       ↓
Apply Bellman Equation
       ↓
Update Q-Matrix
       ↓
Repeat
```

Over many iterations the matrix becomes increasingly accurate.

---

# Learning Through Iteration

Initially:

```text
Q-Matrix

0 0 0

0 0 0

0 0 0
```

After repeated learning:

```text
Q-Matrix

20 40 80

10 60 100

15 45 75
```

The agent now understands which actions are most valuable.

---

# Finding the Optimal Path

After training:

```text
Current State
       ↓
Choose Highest Q-Value
       ↓
Best Action
```

The agent follows the largest Q-values toward the goal.

---

# Real-World Applications

## Robotics

- Navigation
- Path planning

## Autonomous Vehicles

- Route optimization
- Obstacle avoidance

## Logistics

- Delivery optimization
- Warehouse routing

## Gaming

- Chess
- Go
- Atari environments

---

# Key Takeaways

- The Reward Matrix stores immediate rewards.
- The Q-Matrix stores expected future rewards.
- Higher Q-values indicate better actions.
- The Bellman Equation updates Q-values over time.
- Alpha controls learning speed.
- Gamma controls the importance of future rewards.
- Repeated updates gradually produce an optimal policy.
- Q-Learning relies on the Q-Matrix to identify the best actions.

---

# Study Notes

## Q-Learning Flow

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
Learning
```

## Remember

```text
Reward Matrix
      ↓
Immediate Rewards

Q-Matrix
      ↓
Future Rewards + Current Rewards
```