# Mini-Lesson 21.5: Deep Neural Networks

---

# Overview

Deep Neural Networks (DNNs) are one of the most powerful machine learning techniques and are widely used for solving complex problems such as:

- Image Recognition
- Speech Recognition
- Natural Language Processing
- Computer Vision
- Autonomous Driving

Deep Neural Networks are inspired by the structure and operation of the human brain, where interconnected neurons process and transmit information.

---

# What is a Deep Neural Network?

A Deep Neural Network is a collection of artificial neurons (nodes) connected through multiple layers.

A neural network learns patterns by adjusting the strengths of connections between neurons during training.

---

# Structure of a Neural Network

A neural network consists of three major layer types:

```text
Input Layer
      ↓
Hidden Layer(s)
      ↓
Output Layer
```

---

# Input Layer

The input layer receives raw data and passes it to the hidden layers.

Example:

For handwritten digit recognition:

```text
28 × 28 Pixel Image
```

The image consists of:

```text
784 Pixel Values
```

Each pixel becomes an input feature.

---

# Hidden Layers

Hidden layers perform computations on the incoming data.

Responsibilities:

- Feature extraction
- Pattern recognition
- Data transformation
- Classification support

Deep Neural Networks contain:

```text
Two or More Hidden Layers
```

which allow the model to learn increasingly complex patterns.

---

# Output Layer

The output layer provides the final prediction.

For handwritten digit recognition:

```text
10 Output Nodes
```

represent:

```text
0,1,2,3,4,5,6,7,8,9
```

Each node contains the probability that the image belongs to that digit.

---

# Neural Network Connections

Every neuron in one layer is connected to neurons in the next layer.

These connections are called:

```text
Activations
```

Each connection has:

- Weight
- Bias

that determine how much influence information has on the next layer.

---

# TensorFlow

TensorFlow is Google's open-source machine learning framework.

It is widely used for:

- Deep Learning
- Neural Networks
- Computer Vision
- Artificial Intelligence

---

# Installing TensorFlow

```bash
pip install tensorflow
```

---

# Required Imports

```python
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
```

---

# Handwritten Digit Recognition

The lesson uses the MNIST dataset.

The dataset contains:

```text
Handwritten Digits
0 through 9
```

---

# Loading the Dataset

```python
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
```

---

# Training Data

```python
X_train.shape
```

Output:

```python
(60000, 28, 28)
```

Meaning:

```text
60,000 Images
28 × 28 Pixels Each
```

---

# Test Data

```python
X_test.shape
```

Output:

```python
(10000, 28, 28)
```

Meaning:

```text
10,000 Images
28 × 28 Pixels Each
```

---

# Data Normalization

Neural networks perform best when values are scaled.

Pixel values originally range from:

```text
0 - 255
```

Normalization:

```python
X_train = X_train / 255

X_test = X_test / 255
```

Results:

```text
0.0 - 1.0
```

---

# Why Normalize?

Benefits:

- Faster convergence
- Improved stability
- Better accuracy
- More efficient training

---

# Flattening Images

Neural networks require one-dimensional input vectors.

Original image:

```text
28 × 28
```

Flattened image:

```text
784 Features
```

---

# Flatten Training Data

```python
X_train_flattened = X_train.reshape(
    len(X_train),
    28 * 28
)
```

Output:

```python
(60000, 784)
```

---

# Flatten Test Data

```python
X_test_flattened = X_test.reshape(
    len(X_test),
    28 * 28
)
```

Output:

```python
(10000, 784)
```

---

# Neurons

Each neuron performs:

```text
Input
   ↓
Weighted Calculation
   ↓
Bias Adjustment
   ↓
Activation Function
   ↓
Output
```

---

# Weights

Weights determine the importance of each input.

Example:

```text
Large Weight
      ↓
Strong Influence
```

```text
Small Weight
      ↓
Weak Influence
```

Weights are learned automatically during training.

---

# Bias

A bias is a constant value added to the weighted input.

Purpose:

```text
Shift Output
```

to improve model flexibility and accuracy.

---

# Activation Functions

After weights and biases are applied, results pass through an activation function.

Purpose:

```text
Introduce Non-Linearity
```

and normalize outputs.

---

# Common Activation Functions

## Sigmoid

Output range:

```text
0 to 1
```

Often used for probability calculations.

---

## ReLU (Rectified Linear Unit)

```text
f(x) = max(0,x)
```

Most popular hidden-layer activation function.

Benefits:

- Fast training
- Reduces vanishing gradient problems

---

## Tanh

Output range:

```text
-1 to 1
```

Centered around zero.

---

# Forward Propagation

Initially:

```text
Random Weights
Random Biases
```

Data moves through the network.

Process:

```text
Input Layer
      ↓
Hidden Layer
      ↓
Output Layer
```

This is called:

```text
Forward Propagation
```

---

# Backward Propagation

After a prediction is made:

```text
Actual Value
         vs
Predicted Value
```

The error is calculated.

Weights and biases are then adjusted.

This process is called:

```text
Backward Propagation
```

---

# Learning Process

```text
Forward Propagation
         ↓
Calculate Error
         ↓
Backward Propagation
         ↓
Update Weights
         ↓
Improve Model
```

The cycle repeats many times.

---

# Building a Deep Neural Network

Example:

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

# Model Compilation

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

---

# Training the Model

```python
model.fit(
    X_train,
    y_train,
    epochs=5
)
```

---

# Results

The model achieved approximately:

```text
98% Accuracy
```

Meaning:

```text
98% Correct Digit Recognition
```

---

# Advantages of Deep Neural Networks

## High Accuracy

Excellent performance on complex tasks.

---

## Automatic Feature Detection

No manual feature engineering required.

---

## Scalability

Handles large datasets effectively.

---

## Flexibility

Applicable across many domains.

---

# Real-World Applications

## Image Recognition

- Face recognition
- OCR
- Medical imaging

---

## Speech Recognition

- Siri
- Alexa
- Voice assistants

---

## Autonomous Vehicles

- Object detection
- Lane tracking

---

## Healthcare

- Disease diagnosis
- Medical image analysis

---

## Finance

- Fraud detection
- Risk analysis

---

# Deep Learning vs Traditional Machine Learning

## Traditional ML

```text
Manual Feature Engineering
```

Often required.

---

## Deep Learning

```text
Automatic Feature Learning
```

Performed by hidden layers.

---

# Key Components

## Nodes

Artificial neurons.

---

## Activations

Connections between neurons.

---

## Weights

Strength of influence.

---

## Biases

Adjust output values.

---

## Activation Functions

Transform outputs.

---

## Hidden Layers

Extract useful features.

---

# Key Takeaways

- Deep Neural Networks mimic certain aspects of the human brain.
- Networks are composed of input, hidden, and output layers.
- MNIST is a popular handwritten digit recognition dataset.
- Data should be normalized before training.
- Images are flattened into feature vectors.
- Weights and biases are learned automatically.
- Activation functions introduce non-linearity.
- Forward propagation generates predictions.
- Backward propagation improves the model.
- TensorFlow provides tools for building and training neural networks.
- Deep neural networks can achieve very high accuracy on image recognition tasks.

---

# Study Notes

## Neural Network Workflow

```text
Image
  ↓
Input Layer
  ↓
Hidden Layers
  ↓
Activation Functions
  ↓
Output Layer
  ↓
Prediction
```

---

## Learning Process

```text
Forward Propagation
         ↓
Prediction
         ↓
Error Calculation
         ↓
Backward Propagation
         ↓
Weight Updates
         ↓
Improved Accuracy
```

---

# Next Topic

## Video 21.10: Deep Dream Exercise

Key Concepts:

- Deep Learning Visualization
- Neural Network Feature Detection
- Image Manipulation
- Deep Dream
- Computer Vision