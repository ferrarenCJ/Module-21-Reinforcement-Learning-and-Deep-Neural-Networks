# Reinforcement Learning Cheat Sheet

## What is Reinforcement Learning?

Reinforcement Learning (RL) is a machine learning approach where an agent learns by interacting with an environment and receiving rewards or penalties for its actions.

Goal:

```text
Maximize Total Reward
```

---

# Core Components

## Agent

The learner or decision-maker.

Examples:

- Robot
- Self-driving car
- Game AI

---

## Environment

The world in which the agent operates.

Examples:

- Frozen Lake
- Taxi-v4
- Maze
- Chess Board

---

## State

The current situation of the agent.

Example:

```text
Location A
Location B
Location C
```

---

## Action

A movement or decision made by the agent.

Example:

```text
Up
Down
Left
Right
```

---

## Reward

Feedback received after taking an action.

Examples:

```text
Goal Reached = +100

Correct Action = +10

Wrong Action = -10

Dead End = -100
```

---

# Reinforcement Learning Workflow

```text
State
  ↓
Action
  ↓
Environment
  ↓
Reward
  ↓
New State
  ↓
Learn
```

---

# Trial and Error Learning

Unlike supervised learning:

```text
No Answer Key
```

The agent learns through experience.

```text
Explore
   ↓
Receive Reward
   ↓
Learn
   ↓
Improve
```

---

# States and Actions

Example:

```text
Current State = Room A

Available Actions:
    Move Left
    Move Right
    Move Forward
```

Action:

```text
Move Right
```

Next State:

```text
Room B
```

---

# Rewards

Rewards drive learning.

Example:

```text
Reach Goal
    ↓
Positive Reward
```

```text
Wrong Direction
    ↓
Penalty
```

---

# Policy

A policy is a strategy used by the agent.

Purpose:

```text
Determine Best Action
For Each State
```

---

# Optimal Policy

The best possible strategy.

```text
State
   ↓
Best Action
   ↓
Highest Reward
```

---

# Exploration

Agent tries new actions.

Purpose:

```text
Discover New Information
```

Example:

```text
Unknown Path
      ↓
Test Route
```

---

# Exploitation

Agent uses known information.

Purpose:

```text
Maximize Rewards
```

Example:

```text
Choose Best Known Action
```

---

# Exploration vs Exploitation

```text
Exploration
      ↓
Find New Opportunities

Exploitation
      ↓
Use Existing Knowledge
```

A balance is required.

---

# Episode

One complete learning cycle.

Example:

```text
Start
  ↓
Actions
  ↓
Goal
```

Each episode updates learning.

---

# Reward Matrix

Stores valid movements and rewards.

Structure:

```text
Rows    = States
Columns = Actions
```

Example:

```text
Current State
        ↓
Possible Actions
        ↓
Associated Rewards
```

---

# Quality Matrix (Q-Matrix)

Stores learned action values.

Structure:

```text
Rows    = States
Columns = Actions
```

Q-values represent:

```text
Expected Future Reward
```

---

# Q-Learning

Most common reinforcement learning algorithm.

Purpose:

```text
Learn Optimal Actions
```

Workflow:

```text
State
  ↓
Action
  ↓
Reward
  ↓
Update Q-Value
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

# Learning Rate (α)

Controls how quickly learning occurs.

Typical Values:

```text
0.1 - 0.9
```

Higher:

```text
Learn Faster
```

---

# Discount Factor (γ)

Balances:

```text
Immediate Rewards

vs

Future Rewards
```

Typical Values:

```text
0.80 - 0.99
```

---

# Reinforcement Learning Process

## Step 1

Observe state.

---

## Step 2

Choose action.

---

## Step 3

Receive reward.

---

## Step 4

Move to new state.

---

## Step 5

Update knowledge.

---

## Step 6

Repeat.

---

# Common Algorithms

## Q-Learning

```text
Off-Policy
```

Learns optimal policy independently of current actions.

---

## SARSA

```text
On-Policy
```

Learns based on the current policy.

---

## Deep Q-Network (DQN)

Combines:

```text
Q-Learning
      +
Deep Neural Networks
```

Used for large state spaces.

---

# Example Environments

## Frozen Lake

```text
Navigate Ice
Avoid Holes
Reach Goal
```

---

## Taxi-v4

```text
Pickup Passenger
Transport Passenger
Drop Passenger
```

---

## AWS DeepRacer

```text
Autonomous Driving
```

Agent learns how to complete laps.

---

# Advantages

✅ Learns Through Experience

✅ No Labeled Data Needed

✅ Adaptable

✅ Solves Sequential Decisions

✅ Used in Robotics and AI

---

# Disadvantages

❌ Requires Training Time

❌ Can Need Many Episodes

❌ Large State Spaces Increase Complexity

❌ Exploration Can Be Expensive

---

# Real-World Applications

## Self-Driving Cars

```text
Lane Following
Obstacle Avoidance
```

---

## Robotics

```text
Autonomous Navigation
```

---

## Video Games

```text
Game AI
```

---

## Logistics

```text
Route Optimization
```

---

## Finance

```text
Portfolio Optimization
```

---

# Reinforcement Learning vs Supervised Learning

## Reinforcement Learning

```text
Rewards
Penalties
Trial and Error
```

---

## Supervised Learning

```text
Labeled Data
Known Answers
```

---

# Module 21 Exam Facts

### Action

```text
Moving from One State to Another
```

---

### State

```text
Current Observation
```

---

### Agent

```text
Decision Maker
```

---

### Reward

```text
Feedback Signal
```

---

### Q-Matrix

```text
Stores Learned Rewards
```

---

### Gamma (γ)

```text
Balances Current and Future Rewards
```

---

### Bellman Equation

```text
Updates Q-Values
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
Q-Matrix Update
  ↓
Learning
  ↓
Optimal Policy
```