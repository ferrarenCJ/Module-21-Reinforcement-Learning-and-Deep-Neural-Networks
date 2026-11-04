# Confusion Matrix Cheat Sheet

## What is a Confusion Matrix?

A Confusion Matrix is a table used to evaluate the performance of a classification model by comparing predicted values against actual values.

It helps answer:

```text
How many predictions
were correct?
```

and

```text
What types of errors
did the model make?
```

---

# Confusion Matrix Structure

```text
                    Predicted

                Positive   Negative

Actual Positive     TP         FN

Actual Negative     FP         TN
```

---

# Components

## True Positive (TP)

The model correctly predicts a positive outcome.

Example:

```text
Actual = Survived
Predicted = Survived
```

Result:

```text
True Positive
```

---

## True Negative (TN)

The model correctly predicts a negative outcome.

Example:

```text
Actual = Did Not Survive
Predicted = Did Not Survive
```

Result:

```text
True Negative
```

---

## False Positive (FP)

The model predicts a positive outcome when the actual outcome is negative.

Example:

```text
Actual = Did Not Survive
Predicted = Survived
```

Result:

```text
False Positive
```

Also called:

```text
Type I Error
```

---

## False Negative (FN)

The model predicts a negative outcome when the actual outcome is positive.

Example:

```text
Actual = Survived
Predicted = Did Not Survive
```

Result:

```text
False Negative
```

Also called:

```text
Type II Error
```

---

# Accuracy

## Definition

Accuracy measures the percentage of correct predictions.

Formula:

```text
Accuracy =
(TP + TN)
──────────────
TP + TN + FP + FN
```

---

## Example

```text
TP = 40
TN = 50
FP = 5
FN = 5
```

```text
Accuracy =
(40 + 50) / 100

Accuracy = 90%
```

---

# Precision

## Definition

Precision measures how many predicted positives were actually correct.

Formula:

```text
Precision =
TP
──────
TP + FP
```

---

## Example

```text
TP = 40
FP = 10
```

```text
Precision =
40 / 50

Precision = 80%
```

---

# Recall

## Definition

Recall measures how many actual positives were correctly identified.

Formula:

```text
Recall =
TP
──────
TP + FN
```

---

## Example

```text
TP = 40
FN = 5
```

```text
Recall =
40 / 45

Recall = 88.9%
```

---

# Specificity

## Definition

Specificity measures how many actual negatives were correctly identified.

Formula:

```text
Specificity =
TN
──────
TN + FP
```

---

## Example

```text
TN = 50
FP = 5
```

```text
Specificity =
50 / 55

Specificity = 90.9%
```

---

# F1 Score

## Definition

The F1 Score combines:

```text
Precision
    +
Recall
```

into a single metric.

Formula:

```text
F1 =
2 × Precision × Recall
───────────────────────
 Precision + Recall
```

---

## Why Use F1?

Useful when:

```text
Class Distribution
Is Imbalanced
```

---

# Python Example

Import Metrics:

```python
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)
```

---

# Generate Confusion Matrix

```python
cm = confusion_matrix(
    y_test,
    y_pred
)
```

---

# Calculate Accuracy

```python
accuracy_score(
    y_test,
    y_pred
)
```

---

# Calculate Precision

```python
precision_score(
    y_test,
    y_pred
)
```

---

# Calculate Recall

```python
recall_score(
    y_test,
    y_pred
)
```

---

# Calculate F1

```python
f1_score(
    y_test,
    y_pred
)
```

---

# Titanic Example

Problem:

```text
Predict Passenger Survival
```

Possible Outcomes:

```text
0 = Did Not Survive

1 = Survived
```

---

# Example Confusion Matrix

```text
                    Predicted

                 Yes      No

Actual Yes        60       15

Actual No         20       85
```

Interpretation:

```text
TP = 60
FN = 15
FP = 20
TN = 85
```

---

# Performance Metrics Summary

| Metric | Measures |
|----------|----------|
| Accuracy | Overall Correct Predictions |
| Precision | Correct Positive Predictions |
| Recall | Captured Positive Cases |
| Specificity | Correct Negative Predictions |
| F1 Score | Balance of Precision and Recall |

---

# Advantages

✅ Easy to Interpret

✅ Shows Error Types

✅ Supports Multiple Metrics

✅ Common Model Evaluation Tool

---

# Limitations

❌ Accuracy Can Be Misleading

❌ Imbalanced Data May Distort Results

❌ Requires Additional Metrics for Full Evaluation

---

# Module 21 Exam Facts

### True Positive

```text
Correct Positive Prediction
```

---

### True Negative

```text
Correct Negative Prediction
```

---

### False Positive

```text
Incorrect Positive Prediction
```

---

### False Negative

```text
Incorrect Negative Prediction
```

---

### Accuracy

```text
Correct Predictions
÷
Total Predictions
```

---

### F1 Score

```text
Precision + Recall
Combined Metric
```

---

# Quick Review

```text
Actual vs Predicted
          ↓
Confusion Matrix
          ↓
Accuracy
Precision
Recall
Specificity
F1 Score
```