# Bellman Equation Cheat Sheet

## Purpose

The Bellman Equation is the core mathematical formula used in Reinforcement Learning to update Q-values and estimate future rewards.

---

# Bellman Equation

```text
Q(s,a) =
Q(s,a) + α[R + γ max(Q') - Q(s,a)]
```

---

# Variables

| Variable | Meaning |
|----------|----------|
| Q(s,a) | Current Q-value |
| α | Learning Rate |
| R | Immediate Reward |
| γ | Discount Factor |
| max(Q') | Best Future Reward |

---

# Learning Rate (α)

Controls how quickly new information replaces old information.

Typical values:

```text
0.1 - 0.9
```

---

# Discount Factor (γ)

Balances:

```text
Current Rewards

vs

Future Rewards
```

Typical values:

```text
0.8 - 0.99
```

---

# Workflow

```text
Current State
      ↓
Select Action
      ↓
Receive Reward
      ↓
Compute Bellman Update
      ↓
Update Q-Value
```

---

# Example

```python
Q[current_state, next_state] += alpha * TD
```

where:

```python
TD = reward + gamma * max_future_reward - current_q
```

---

# Key Takeaways

✅ Updates Q-values

✅ Supports reinforcement learning

✅ Uses future rewards

✅ Foundation of Q-Learning

✅ Helps discover optimal policies