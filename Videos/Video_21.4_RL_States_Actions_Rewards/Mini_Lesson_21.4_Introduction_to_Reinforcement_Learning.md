# Mini-Lesson 21.4: Introduction to Reinforcement Learning

**Estimated Time:** 30 Minutes

---

# Overview

This section introduces Reinforcement Learning (RL) and its most popular implementation, **Q-Learning**.

Unlike traditional machine learning approaches that rely on labeled datasets, reinforcement learning allows an agent to learn by interacting with an environment and receiving rewards or penalties based on its actions.

Topics covered include:

- Reinforcement Learning Fundamentals
- States, Actions, and Rewards
- Q-Learning
- Q-Matrix
- Exploration vs Exploitation
- Episodes
- Learning Rate
- Discount Factor (Gamma)
- Future Rewards

---

# What is Reinforcement Learning?

Reinforcement Learning (RL) is an unsupervised machine learning technique that learns through experience.

An agent performs actions within an environment and receives feedback in the form of rewards or penalties.

The objective is to maximize long-term rewards.

---

## Reinforcement Learning Framework

```text
Agent
   ↓
Action
   ↓
Environment
   ↓
Reward
   ↓
Learning
   ↓
Better Action
```

The process repeats continuously until the agent identifies the optimal strategy.

---

# What is Q-Learning?

Q-Learning is one of the most widely used reinforcement learning algorithms.

The "Q" stands for:

```text
Quality
```

Quality refers to how useful a specific action is for achieving a desired result.

Q-Learning helps determine:

```text
Best Action
        Given
Current State
```

---

# Model-Free Learning

Many algorithms operate using predefined rules known as policies.

Q-Learning differs because:

- No predefined model exists
- No predefined action outcomes are known
- Actions can be selected randomly

For this reason, Q-Learning is considered:

```text
Off-Policy
```

and

```text
Model-Free
```

---

# Q-Matrix

The foundation of Q-Learning is the:

```text
Q-Matrix
```

The Q-Matrix stores the expected value of taking a particular action from a specific state.

---

## Structure of a Q-Matrix

```text
            Actions

         A1   A2   A3

State 1   0    0    0

State 2   0    0    0

State 3   0    0    0
```

Rows represent:

```text
States
```

Columns represent:

```text
Actions
```

Values represent:

```text
Q-Values
```

---

# Creating a Q-Matrix in Python

Initially, the matrix contains only zeros.

```python
import numpy as np

Q_Matrix = np.zeros((state_size, action_size))
```

This provides a starting point for learning.

---

# Q-Values

Q-Values represent:

```text
Expected Future Reward
```

for performing a particular action from a given state.

As learning progresses:

```text
Low Quality Action
        ↓
Low Q-Value

High Quality Action
        ↓
High Q-Value
```

---

# Updating the Q-Matrix

Two primary methods are used to populate the Q-Matrix:

1. Exploration
2. Exploitation

---

# Exploration

Exploration occurs when the agent chooses random actions.

Goal:

```text
Discover New Information
```

Example:

```text
Unknown State
      ↓
Random Move
      ↓
Observe Reward
```

Benefits:

- Finds previously undiscovered paths
- Expands knowledge of the environment
- Prevents premature optimization

---

# Exploitation

Exploitation uses existing knowledge stored in the Q-Matrix.

The agent chooses:

```text
Highest Q-Value
```

available from its current state.

Example:

```text
State 3

Action A = 15

Action B = 40

Action C = 12

Choose Action B
```

Benefits:

- Maximizes rewards
- Uses learned experience
- Improves performance

---

# Exploration vs Exploitation

Both strategies are necessary.

Too much exploration:

```text
Learning Continues

Performance Decreases
```

Too much exploitation:

```text
Existing Knowledge Used

New Opportunities Missed
```

A balance must be maintained.

---

# Epsilon (ε)

The balance between exploration and exploitation is controlled using:

```text
ε (epsilon)
```

---

## High Epsilon

```text
More Exploration
```

Agent performs more random actions.

---

## Low Epsilon

```text
More Exploitation
```

Agent relies heavily on learned experience.

---

# Episodes

Learning occurs through repeated experiments called:

```text
Episodes
```

An episode is one complete attempt to solve a problem.

---

## Example

```text
Start State
      ↓
Move
      ↓
Move
      ↓
Move
      ↓
Goal State
```

One complete run equals:

```text
1 Episode
```

---

# Why Multiple Episodes?

One episode is rarely enough.

The agent must repeat the process many times to learn:

- Good decisions
- Poor decisions
- Optimal paths

Example:

```text
1000 Episodes
      ↓
Improved Q-Matrix
      ↓
Optimal Strategy
```

---

# Q-Learning Process

The basic workflow is:

## Step 1

Start in state:

```text
S1
```

---

## Step 2

Choose an action:

```text
A1
```

using either:

- Exploration
- Exploitation

---

## Step 3

Receive a reward:

```text
R1
```

---

## Step 4

Move to the next state.

---

## Step 5

Update the Q-Matrix.

---

## Step 6

Repeat until the episode ends.

---

# Q-Learning Formula

```text
Q(s,a) =
Q(s,a) +
α × [ R + γ × Max(Q') − Q(s,a) ]
```

This formula updates the value of every action taken.

---

# Q-Learning Variables

## Learning Rate (α)

Alpha controls how much new information affects learning.

---

### High Alpha

```text
New Information
More Important
```

---

### Low Alpha

```text
Historical Knowledge
More Important
```

---

# Gamma (γ)

Gamma controls the importance of future rewards.

Typical values:

```text
0.80 - 0.99
```

---

## High Gamma

```text
Future Rewards
Highly Valued
```

Agent plans ahead.

---

## Low Gamma

```text
Immediate Rewards
Highly Valued
```

Agent becomes more short-sighted.

---

# Reward

A reward is feedback received after performing an action.

Examples:

```text
Correct Action
      ↓
+100
```

```text
Incorrect Action
      ↓
-100
```

The reward structure depends entirely on the problem being solved.

---

# Future Reward Function

The Q-Learning formula includes:

```text
Max(Q')
```

This evaluates:

```text
Best Future Action
```

from the next state.

This allows future rewards to influence current decisions.

---

# Why Future Rewards Matter

Consider two possible paths:

```text
Path A
Reward = 5

Path B
Reward = 2
Future Reward = 100
```

A greedy algorithm may choose:

```text
Path A
```

Q-Learning recognizes:

```text
Path B
```

provides a greater long-term return.

---

# Example: Robot Navigation

A robot must navigate a maze.

Goal:

```text
Reach Exit
```

Rewards:

```text
Wall = -10

Move = -1

Goal = +100
```

The agent learns:

- Which paths lead to failure
- Which paths reach the goal fastest

Eventually, the optimal route emerges.

---

# Advantages of Q-Learning

## Model-Free

Does not require knowledge of environment dynamics.

---

## Adaptable

Works in many different situations.

---

## Scalable

Can solve problems with many states and actions.

---

## Learns Through Experience

No predefined rules are necessary.

---

# Real-World Applications

## Robotics

- Navigation
- Path optimization
- Motion planning

---

## Autonomous Vehicles

- Route selection
- Obstacle avoidance

---

## Gaming

- Chess
- Go
- Atari environments

---

## Operations Research

- Scheduling
- Resource allocation
- Optimization problems

---

## Industrial Automation

- Process optimization
- Equipment control

---

# Key Takeaways

- Reinforcement learning learns through rewards and penalties.
- Q-Learning is one of the most common reinforcement learning algorithms.
- The Q-Matrix stores expected rewards for actions.
- Exploration discovers new information.
- Exploitation uses existing knowledge.
- Epsilon controls the balance between exploration and exploitation.
- Episodes represent complete learning attempts.
- Alpha controls learning speed.
- Gamma controls the importance of future rewards.
- Q-Learning can efficiently discover optimal paths and strategies.

---

# Study Notes

## Reinforcement Learning Components

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
```

---

## Remember

```text
Exploration
    ↓
Try New Actions

Exploitation
    ↓
Use Best Known Actions
```

---

## Key Parameters

```text
Alpha (α)
    ↓
Learning Rate

Gamma (γ)
    ↓
Future Reward Weight

Epsilon (ε)
    ↓
Exploration vs Exploitation
```

---

# Next Topic

Video 21.4: Reinforcement Learning - States, Actions, and Rewards

Key Concepts:

- Environment
- Agent
- States
- Actions
- Reward Matrix
- Reinforcement Learning Workflow