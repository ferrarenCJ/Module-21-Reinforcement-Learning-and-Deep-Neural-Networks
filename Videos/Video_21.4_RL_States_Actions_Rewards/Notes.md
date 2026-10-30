# Video 21.4: Reinforcement Learning - States, Actions, and Rewards

**Duration:** 08:48

---

# Overview

This video introduces the foundational concepts of Reinforcement Learning (RL):

- States
- Actions
- Rewards
- Reward Matrix

Reinforcement learning focuses on making decisions that maximize rewards over time. Each action influences future decisions, allowing the agent to learn increasingly effective strategies.

---

# What is Reinforcement Learning?

Reinforcement learning is a machine learning approach in which an agent learns by interacting with an environment.

The agent receives:

- Rewards for desirable actions
- Penalties for undesirable actions

The objective is to discover the sequence of actions that produces the highest cumulative reward.

---

# Reinforcement Learning Workflow

```text
Current State
       ↓
Choose Action
       ↓
Receive Reward
       ↓
Move to New State
       ↓
Learn from Outcome
       ↓
Improve Future Decisions
```

---

# Core Components

## Agent

The decision-maker within the environment.

Examples:

- Robot
- Autonomous vehicle
- Game player
- Machine learning model

---

## Environment

The world in which the agent operates.

Examples:

- Maze
- Game board
- Factory floor
- Road network

---

## State

A state represents the current condition or location of the agent.

Example:

```text
Room A
Room B
Room C
Room D
```

Each room represents a different state.

---

## Action

An action is a decision the agent can make.

Examples:

```text
Move Up
Move Down
Move Left
Move Right
```

---

## Reward

A reward measures the value of an action.

Examples:

```text
Goal Reached
Reward = +100
```

```text
Invalid Move
Reward = -100
```

```text
Normal Move
Reward = -1
```

Rewards guide the learning process.

---

# States and Actions Example

Consider a simple navigation problem:

```text
+-----+-----+
|  A  |  B  |
+-----+-----+
|  C  |  D  |
+-----+-----+
```

Possible states:

```text
A
B
C
D
```

Possible actions:

```text
Up
Down
Left
Right
```

Not every action is valid from every state.

---

# Reward Matrix

A Reward Matrix (R-Matrix) stores the reward values associated with actions and states.

The reward matrix helps the algorithm determine which actions are beneficial.

---

## Example Reward Matrix

```text
        A     B     C     D

A      -1     0    -1     0

B       0    -1     0   100

C      -1     0    -1     0

D       0   100     0   100
```

Values represent:

```text
Reward Received
for Moving
Between States
```

---

# Purpose of the Reward Matrix

The reward matrix serves as the foundation for learning.

It allows the agent to:

- Evaluate possible actions
- Discover profitable paths
- Avoid bad decisions
- Learn optimal routes

---

# Learning Through Trial and Error

Initially, the agent has no knowledge.

The process begins with random exploration.

```text
Unknown Environment
        ↓
Random Actions
        ↓
Rewards Observed
        ↓
Learning Occurs
```

Over time:

```text
More Experience
        ↓
Better Decisions
        ↓
Higher Rewards
```

---

# Example Pathfinding Problem

Suppose an agent must travel to a goal location.

Possible outcomes:

### Efficient Path

```text
Start
  ↓
Goal
```

Reward:

```text
High
```

---

### Inefficient Path

```text
Start
 ↓
Wrong Turn
 ↓
Wrong Turn
 ↓
Goal
```

Reward:

```text
Lower
```

The algorithm eventually learns to prefer the more efficient route.

---

# Reinforcement Learning Characteristics

## Sequential Decisions

Current decisions influence future outcomes.

```text
Decision 1
    ↓
Decision 2
    ↓
Decision 3
```

---

## Learning from Rewards

No explicit instructions are provided.

The agent learns solely through experience.

---

## Continuous Improvement

Performance improves as more interactions occur.

---

## Goal-Oriented Learning

Learning is focused on maximizing total reward.

---

# Reinforcement Learning vs Traditional Programming

## Traditional Programming

```text
Input
  ↓
Rules
  ↓
Output
```

Behavior is explicitly programmed.

---

## Reinforcement Learning

```text
Input
  ↓
Actions
  ↓
Rewards
  ↓
Learning
  ↓
Output
```

Behavior emerges through experience.

---

# Reward Design

Designing reward values is critical.

Poor reward design can create unintended behavior.

Example:

```text
Reward Goal = +100

Reward Move = +10
```

The agent might continue moving forever instead of reaching the goal.

Rewards should encourage desired outcomes.

---

# Real-World Applications

## Robotics

- Path planning
- Navigation
- Movement optimization

---

## Autonomous Vehicles

- Route optimization
- Obstacle avoidance
- Traffic navigation

---

## Gaming

- Chess
- Go
- Atari games

---

## Manufacturing

- Process optimization
- Resource allocation
- Automated decision-making

---

## Logistics

- Route planning
- Fleet optimization
- Warehouse automation

---

# Example: Fleet Operations

A delivery vehicle can make several routing decisions.

State:

```text
Current Location
```

Actions:

```text
Drive North
Drive South
Drive East
Drive West
```

Rewards:

```text
Fast Delivery = Positive Reward

Traffic Delay = Negative Reward

Fuel Waste = Negative Reward
```

The agent eventually learns the most efficient route.

---

# Key Takeaways

- Reinforcement learning learns through rewards and penalties.
- An agent interacts with an environment.
- States describe the current situation.
- Actions are decisions available to the agent.
- Rewards provide feedback.
- A Reward Matrix stores reward values between states and actions.
- Learning occurs through repeated interactions.
- The objective is to maximize cumulative rewards.
- Reinforcement learning is widely used for navigation and optimization problems.

---

# Study Notes

## Core RL Components

```text
Agent
   ↓
State
   ↓
Action
   ↓
Reward
   ↓
Learning
```

---

## Reward Matrix Purpose

```text
State + Action
        ↓
Reward
        ↓
Learning
```

---

## Goal of Reinforcement Learning

```text
Maximize Rewards
        ↓
Optimal Behavior
```

---

# Next Topic

## Required Discussion 21.2: Use Cases for Reinforcement Learning

and

## Videos 21.5 & 21.6: Quality Matrix (Q-Matrix) and the Bellman Equation

Key Concepts:

- Q-Matrix
- Q-Values
- Bellman Equation
- Future Rewards
- Optimal Policies