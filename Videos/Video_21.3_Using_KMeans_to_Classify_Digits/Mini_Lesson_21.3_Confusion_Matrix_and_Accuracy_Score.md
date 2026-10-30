# Mini-Lesson 21.3: The Confusion Matrix and Accuracy Score

---

# Overview

The confusion matrix is one of the most important tools used to evaluate machine learning classification models.

It helps determine:

- How well a model performs
- Where errors occur
- Whether the model is making correct predictions
- Which model performs best for a specific business problem

The confusion matrix compares:

```text
Actual Values
        vs
Predicted Values
```

allowing us to identify correct and incorrect predictions.

---

# What is a Confusion Matrix?

A confusion matrix is a table that summarizes the performance of a classification model.

For binary classification:

```text
                    Predicted

                 Positive   Negative

Actual Positive      TP         FN

Actual Negative      FP         TN
```

Where:

- TP = True Positive
- TN = True Negative
- FP = False Positive
- FN = False Negative

---

# Fraud Detection Example

Suppose we are building a machine learning model to determine whether a credit card transaction is fraudulent.

## Positive

```text
Fraudulent Transaction
```

## Negative

```text
Legitimate Transaction
```

---

# True Positive (TP)

The model correctly predicts fraud.

```text
Actual Fraud
Predicted Fraud
```

✅ Correct Prediction

---

# True Negative (TN)

The model correctly predicts a legitimate transaction.

```text
Actual Legitimate
Predicted Legitimate
```

✅ Correct Prediction

---

# False Positive (FP)

The model predicts fraud when the transaction is actually legitimate.

```text
Actual Legitimate
Predicted Fraud
```

❌ Incorrect Prediction

Also called a:

```text
False Alarm
```

---

# False Negative (FN)

The model predicts a transaction is legitimate when it is actually fraudulent.

```text
Actual Fraud
Predicted Legitimate
```

❌ Incorrect Prediction

Potentially the most dangerous error in fraud detection.

---

# Confusion Matrix Metrics

Several performance metrics can be calculated from a confusion matrix.

---

# 1. Accuracy

Accuracy measures:

```text
How many predictions
were correct?
```

Formula:

```text
Accuracy =
(TP + TN)
----------------
(TP + FP + TN + FN)
```

---

## Example

```text
90 Correct Predictions
100 Total Predictions
```

```text
Accuracy = 90%
```

---

# 2. Precision

Precision measures:

```text
How many positive predictions
were correct?
```

Formula:

```text
Precision =
TP
-----------
TP + FP
```

---

## Example

If a model predicts:

```text
100 Fraud Cases
```

and:

```text
90 are truly fraudulent
```

then:

```text
Precision = 90%
```

---

# 3. Recall

Recall measures the model's ability to identify positive cases.

Question:

```text
How many actual positive
cases were found?
```

Formula:

```text
Recall =
TP
-----------
TP + FN
```

---

## Importance of Recall

High recall means:

```text
Few False Negatives
```

This is important in:

- Disease detection
- Fraud detection
- Security monitoring

where missing a positive case can be costly.

---

# Precision vs Recall

These metrics often involve tradeoffs.

---

## Spam Detection Example

If an email is falsely classified as normal:

```text
Spam → Inbox
```

the impact is relatively low.

High precision may be preferred.

---

## Medical Testing Example

If a COVID-positive patient is classified as negative:

```text
Positive Patient
       ↓
Negative Prediction
```

the consequences can be severe.

In these situations:

```text
High Recall
```

is critical.

---

# 4. Specificity

Specificity measures:

```text
How well the model
identifies negatives.
```

Formula:

```text
Specificity =
TN
-----------
TN + FP
```

---

## High Specificity

Means:

```text
Few False Positives
```

The model is effective at recognizing negative observations.

---

# 5. F1 Score

The F1 Score combines:

- Precision
- Recall

into a single metric.

Formula:

```text
F1 =
2 × Precision × Recall
------------------------
Precision + Recall
```

---

# Why Use F1 Score?

The F1 score provides a balanced measure of performance.

Benefits:

- Combines precision and recall
- Useful with imbalanced datasets
- Produces a score between 0 and 1

---

## Interpretation

### F1 = 1

```text
Perfect Model
```

### F1 = 0

```text
Poor Model
```

---

# Python Implementation

## Confusion Matrix

```python
from sklearn.metrics import confusion_matrix

y_true = [0, 0, 0, 1, 1, 1, 1, 1]
y_pred = [0, 1, 0, 1, 0, 1, 0, 1]

cm = confusion_matrix(y_true, y_pred)

print(cm)
```

---

## Accuracy

```python
from sklearn.metrics import accuracy_score

accuracy_score(y_true, y_pred)
```

---

## Recall

```python
from sklearn.metrics import recall_score

recall_score(y_true, y_pred, average=None)
```

---

## Precision

```python
from sklearn.metrics import precision_score

precision_score(y_true, y_pred, average=None)
```

---

## Specificity

```python
from sklearn.metrics import confusion_matrix

tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

specificity = tn / (tn + fp)
```

---

## F1 Score

```python
from sklearn.metrics import f1_score

f1_score(y_true, y_pred, average=None)
```

---

# When Accuracy Can Be Misleading

Consider:

```text
1,000 Transactions

990 Legitimate
10 Fraudulent
```

If a model predicts:

```text
Everything Legitimate
```

Accuracy:

```text
990 / 1000 = 99%
```

Despite high accuracy:

```text
Fraud Detection = 0%
```

This demonstrates why precision, recall, specificity, and F1 score are equally important.

---

# Real-World Applications

## Fraud Detection

- Credit card fraud
- Insurance fraud
- Transaction monitoring

---

## Healthcare

- Disease diagnosis
- Medical screening
- Risk prediction

---

## Cybersecurity

- Intrusion detection
- Malware classification
- Threat monitoring

---

## Utility Operations

- Leak detection
- Asset failure prediction
- Service interruption forecasting

---

# Key Takeaways

- A confusion matrix compares actual outcomes to predicted outcomes.
- True positives and true negatives represent correct predictions.
- False positives and false negatives represent prediction errors.
- Accuracy measures overall correctness.
- Precision measures correctness of positive predictions.
- Recall measures the ability to find positive cases.
- Specificity measures the ability to identify negatives.
- F1 Score balances precision and recall.
- Accuracy alone is not always sufficient for evaluating model performance.
- Confusion matrices are essential for assessing machine learning models.

---

# Study Notes

## Remember

```text
TP = Correct Positive

TN = Correct Negative

FP = False Alarm

FN = Missed Positive
```

---

## Evaluation Metrics

```text
Accuracy
    ↓
Overall Performance

Precision
    ↓
Positive Prediction Quality

Recall
    ↓
Positive Detection Rate

Specificity
    ↓
Negative Detection Rate

F1 Score
    ↓
Precision + Recall Balance
```

---

# Next Topic

Mini-Lesson 21.4: Introduction to Reinforcement Learning

Key Concepts:

- Agents
- States
- Actions
- Rewards
- Environments
- Learning Through Experience