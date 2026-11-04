# Deep Neural Networks Cheat Sheet

## What is a Deep Neural Network?

A Deep Neural Network (DNN) is a machine learning model inspired by the human brain that contains multiple layers of interconnected neurons.

Applications:

- Image Recognition
- Speech Recognition
- Computer Vision
- Natural Language Processing
- Autonomous Vehicles

---

# Neural Network Structure

```text
Input Layer
      ↓
Hidden Layer(s)
      ↓
Output Layer
```

---

# Input Layer

Purpose:

- Receives raw data
- Passes information to hidden layers

Example:

```text
28 x 28 MNIST Image
      ↓
784 Input Features
```

---

# Hidden Layers

Purpose:

- Feature extraction
- Pattern recognition
- Data transformation

Characteristics:

```text
More Hidden Layers
        ↓
More Complex Learning
```

---

# Output Layer

Purpose:

- Produces predictions

Example:

```text
Digit Recognition

0
1
2
3
4
5
6
7
8
9
```

10 output neurons represent probabilities for each digit.

---

# Neurons (Nodes)

A neuron performs:

```text
Inputs
   ↓
Weights
   ↓
Bias
   ↓
Activation Function
   ↓
Output
```

---

# Weights

Weights determine how strongly an input influences the output.

```text
Large Weight
      ↓
Strong Influence

Small Weight
      ↓
Weak Influence
```

---

# Bias

A bias is a constant added to the weighted sum.

Purpose:

```text
Shift Output Value
```

---

# Activation

An activation is a connection between neurons.

```text
Neuron
   ↓ Activation
Neuron
```

---

# Activation Functions

Used to introduce non-linearity.

---

## Sigmoid

Output Range:

```text
0 to 1
```

Formula:

```text
σ(x) = 1 / (1 + e^-x)
```

Common Use:

- Binary Classification
- Probabilities

---

## ReLU

Formula:

```text
f(x) = max(0,x)
```

Benefits:

- Fast Training
- Most Common Hidden Layer Function

---

## Tanh

Output Range:

```text
-1 to 1
```

Useful when centered outputs are desired.

---

# Forward Propagation

Process:

```text
Input
  ↓
Hidden Layers
  ↓
Output
```

Purpose:

```text
Generate Prediction
```

---

# Backward Propagation

Process:

```text
Prediction
      ↓
Calculate Error
      ↓
Update Weights
      ↓
Improve Model
```

Purpose:

```text
Reduce Error
```

---

# Training Cycle

```text
Forward Propagation
         ↓
Prediction
         ↓
Error
         ↓
Backward Propagation
         ↓
Weight Updates
         ↓
Repeat
```

---

# TensorFlow

Popular Deep Learning Framework.

Install:

```bash
pip install tensorflow
```

Import:

```python
import tensorflow as tf
from tensorflow import keras
```

---

# MNIST Example

Load Dataset:

```python
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
```

Training Data:

```text
60000 Images
```

Testing Data:

```text
10000 Images
```

---

# Normalization

Convert pixel values:

```text
0 - 255
```

to

```text
0 - 1
```

Code:

```python
X_train = X_train / 255
X_test = X_test / 255
```

---

# Flattening Images

Convert:

```text
28 x 28
```

into:

```text
784 Features
```

Code:

```python
X_train_flattened = X_train.reshape(
    len(X_train),
    28 * 28
)
```

---

# TensorFlow Neural Network Example

```python
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(
        100,
        activation='relu'
    ),
    keras.layers.Dense(
        10,
        activation='sigmoid'
    )
])
```

---

# Compile Model

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

---

# Train Model

```python
model.fit(
    X_train,
    y_train,
    epochs=5
)
```

---

# Common Deep Learning Terms

| Term | Meaning |
|--------|---------|
| Node | Artificial Neuron |
| Weight | Strength of Connection |
| Bias | Constant Adjustment |
| Activation | Connection Between Neurons |
| Epoch | One Full Training Pass |
| Hidden Layer | Feature Extraction Layer |
| Output Layer | Prediction Layer |

---

# Deep Learning Workflow

```text
Raw Data
    ↓
Input Layer
    ↓
Hidden Layers
    ↓
Prediction
    ↓
Error
    ↓
Learning
```

---

# Advantages

✅ High Accuracy

✅ Automatic Feature Learning

✅ Scales to Large Datasets

✅ Handles Complex Problems

✅ Image & Speech Recognition

---

# Module 21 Exam Facts

### Three Layers

```text
Input Layer
Hidden Layer
Output Layer
```

### Activation

```text
Connection Between Neurons
```

### TensorFlow

```text
Google's Deep Learning Framework
```

### Forward Propagation

```text
Generate Prediction
```

### Backward Propagation

```text
Update Weights and Biases
```

### Module Example

```text
MNIST Handwritten Digit Recognition
```

Accuracy:

```text
~98%
```