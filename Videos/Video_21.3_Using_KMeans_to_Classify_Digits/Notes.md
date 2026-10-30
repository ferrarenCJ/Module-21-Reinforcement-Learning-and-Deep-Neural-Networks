# Video 21.3: Using K-Means to Classify Digits

**Duration:** 05:09

---

# Overview

This video demonstrates a practical application of K-Means clustering by using the algorithm to classify images of handwritten digits.

Although K-Means is an unsupervised learning algorithm, it can still identify patterns within image data and group similar digit images together.

This example illustrates how clustering techniques can be used in image processing and pattern recognition tasks.

---

# Objective

Use K-Means clustering to group handwritten digit images into clusters based on similarities in their pixel patterns.

The algorithm attempts to discover naturally occurring groups without being given the actual digit labels.

---

# Handwritten Digit Classification

The dataset consists of images representing digits such as:

```text
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

Each image is converted into numerical data that can be analyzed by a machine learning algorithm.

---

# Converting Images into Data

Machine learning algorithms cannot directly interpret images.

Images must first be converted into numerical features.

Example:

```text
Pixel Location (X,Y)
        ↓
Brightness Value
        ↓
Numerical Feature
```

Each pixel in the image becomes a feature that can be used by the clustering algorithm.

---

# Applying K-Means

The K-Means algorithm follows its standard workflow:

```text
Input Image Data
        ↓
Select Number of Clusters (K)
        ↓
Initialize Centroids
        ↓
Assign Images to Clusters
        ↓
Update Centroids
        ↓
Repeat Until Convergence
```

---

# Why K = 10?

Since the dataset contains:

```text
Digits 0-9
```

there are ten possible categories.

Therefore:

```python
K = 10
```

is a reasonable starting point for clustering.

---

# Cluster Formation

K-Means groups images with similar visual characteristics.

Example:

```text
Cluster 1
    ↓
Mostly Digit 0

Cluster 2
    ↓
Mostly Digit 1

Cluster 3
    ↓
Mostly Digit 7
```

The model does not know the actual digit labels.

Instead, it discovers similarities based entirely on the image data.

---

# Cluster Centroids

Each cluster is represented by a centroid.

The centroid can be viewed as the "average digit" for all observations assigned to that cluster.

Example:

```text
Many Digit 8 Images
         ↓
Average Shape
         ↓
Centroid
```

These centroids help determine which cluster a new image belongs to.

---

# Unsupervised Classification

Unlike supervised image classification:

```text
Image → Label
```

K-Means receives:

```text
Image Data Only
```

No labels are provided during training.

This makes K-Means an unsupervised learning technique.

---

# Evaluating Results

Although K-Means is unsupervised, results can still be compared against true labels.

Common evaluation methods include:

- Confusion Matrix
- Accuracy Score
- Cluster Visualization

These topics are explored further in the next lesson.

---

# Benefits of K-Means for Images

## Pattern Discovery

Identifies hidden structure in image datasets.

---

## No Labels Required

Useful when image labels are unavailable.

---

## Fast Training

Computationally efficient compared to many deep learning methods.

---

## Exploratory Analysis

Helps understand image distributions before building supervised models.

---

# Limitations

## Clusters May Not Match Labels Perfectly

Different digits may appear visually similar.

Example:

```text
1 and 7

3 and 8
```

may occasionally be grouped together.

---

## Sensitive to K

Choosing an incorrect number of clusters can reduce performance.

---

## Image Complexity

K-Means works best on simpler datasets and may struggle with highly complex image recognition tasks.

---

# Real-World Applications

Image clustering techniques can be used for:

- Handwriting recognition
- Document analysis
- Medical imaging
- Face grouping
- Object detection preprocessing
- Image organization

---

# Connection to Artificial Intelligence

Digit classification demonstrates how machine learning systems can:

```text
Observe Data
      ↓
Identify Patterns
      ↓
Group Similar Objects
      ↓
Make Predictions
```

These concepts are foundational to:

- Computer Vision
- Deep Learning
- Neural Networks
- Artificial Intelligence

---

# Key Takeaways

- K-Means can be applied to image classification tasks.
- Images are converted into numerical features before analysis.
- The algorithm groups similar digit images into clusters.
- No labels are required during training.
- Centroids represent the average characteristics of each cluster.
- K-Means is useful for pattern discovery and exploratory image analysis.
- Results can later be evaluated using confusion matrices and accuracy scores.
- Digit classification serves as an introductory computer vision example.

---

# Study Notes

## Remember

```text
Image
   ↓
Pixels
   ↓
Features
   ↓
K-Means
   ↓
Clusters
```

## Digit Classification Workflow

```text
Load Images
      ↓
Convert Pixels to Features
      ↓
Scale Data
      ↓
Apply K-Means
      ↓
Create Clusters
      ↓
Evaluate Results
```

---

# Next Topic

Mini-Lesson 21.3: The Confusion Matrix and Accuracy Score

Key Concepts:

- Confusion Matrix
- Classification Accuracy
- Model Evaluation
- Cluster Performance Measurement