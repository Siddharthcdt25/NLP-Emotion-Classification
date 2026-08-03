# 🧠 NLP Emotion Classification

<p align="center">

  <img src="assets/snapshot.png" alt="NLP Emotion Classification - Project Snapshot" width="100%">

</p>

<p align="center">
  <strong>A Classical Machine Learning NLP application for detecting emotions from natural language.</strong>
</p>

<p align="center">

  <a href="YOUR_STREAMLIT_URL">
    <img src="https://img.shields.io/badge/Live%20Demo-Streamlit-red?logo=streamlit&logoColor=white" alt="Live Demo">
  </a>

  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn&logoColor=white" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/NLP-Classical%20NLP-purple" alt="NLP">
  <img src="https://img.shields.io/badge/TF--IDF-Feature%20Extraction-yellow" alt="TF-IDF">
  <img src="https://img.shields.io/badge/Linear%20SVM-Classifier-green" alt="Linear SVM">
  <img src="https://img.shields.io/badge/Streamlit-Deployed-red?logo=streamlit&logoColor=white" alt="Streamlit">

</p>

---

## 📌 Overview

**NLP Emotion Classification** is a classical Natural Language Processing project that
classifies human-written text into one of six emotion categories.

The project follows a complete machine learning workflow:

> **Raw Text → Text Preprocessing → TF-IDF → Machine Learning Classification → Emotion Prediction → Streamlit Deployment**

The application allows users to enter a sentence or short paragraph and receive an
instant emotion prediction through an interactive web interface.

### Supported Emotions

- 😠 Anger
- 😨 Fear
- 😄 Joy
- ❤️ Love
- 😢 Sadness
- 😲 Surprise

---

## 🎯 Project Objective

The primary objective of this project is to build an end-to-end **classical NLP
classification system** capable of identifying the emotional intent expressed in
natural language.

Rather than using deep learning or transformer-based architectures, this project
focuses on understanding and implementing the fundamentals of classical NLP:

- Text preprocessing
- Label encoding
- Bag-of-Words representation
- TF-IDF feature extraction
- Multinomial Naive Bayes
- Logistic Regression
- Linear SVM
- Model evaluation
- Model serialization
- Streamlit deployment

This makes the project particularly useful for understanding the foundations of
NLP before moving toward deep learning and transformer-based approaches.

---

## 🧠 Machine Learning Pipeline

```text
                 INPUT TEXT
                     │
                     ▼
             Text Preprocessing
                     │
                     ▼
              TF-IDF Vectorizer
                     │
                     ▼
               Linear SVM
                     │
                     ▼
             Numeric Prediction
                     │
                     ▼
              Label Encoder
                     │
                     ▼
             Emotion Prediction

## 📊 Dataset

The project uses a labeled text dataset for emotion classification.

Each record contains two main fields:

| Column | Description |
|---|---|
| `text` | Input sentence/text |
| `emotion` | Target emotion label |

The dataset contains six emotion categories:

```text
anger
fear
joy
love
sadness
surprise


### 🧹 Text Processing

```markdown
# 🧹 Text Processing

Natural language cannot be directly provided to a traditional machine
learning algorithm. Therefore, the text must first be transformed into a
suitable numerical representation.

The general text-processing workflow used in this project is:

```text
Raw Text
   ↓
Text Cleaning
   ↓
Text Normalization
   ↓
Feature Extraction
   ↓
Numerical Feature Matrix
   ↓
Machine Learning Model


### 📝 TF-IDF Feature Extraction

```markdown
# 📝 TF-IDF Feature Extraction

The final model uses **TF-IDF (Term Frequency-Inverse Document Frequency)**
for converting text into numerical features.

TF-IDF measures the importance of a word within a document relative to the
entire collection of documents.

The basic idea is:

```text
TF-IDF
   =
Term Frequency × Inverse Document Frequency


### ▶️ Run Locally

```markdown
# ▶️ Run Locally

You can run the application locally using Python and Streamlit.

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/NLP-Emotion-Classification.git


### 🔍 Why Classical NLP?

```markdown
# 🔍 Why Classical NLP?

This project intentionally uses **classical Natural Language Processing**
rather than deep learning or transformer-based architectures.

The primary objective was to understand the fundamental NLP workflow and how
traditional machine learning algorithms can be applied to text classification.

The project demonstrates the complete classical NLP pipeline:

```text
Raw Text
   ↓
Text Processing
   ↓
Feature Engineering
   ↓
Bag-of-Words / TF-IDF
   ↓
Machine Learning
   ↓
Model Evaluation
   ↓
Model Serialization
   ↓
Deployment


### ⚠️ Limitations

```markdown
# ⚠️ Limitations

Although the model achieves strong classification performance on the
evaluation data, emotion classification is inherently challenging.

A sentence can have different emotional meanings depending on context,
conversation history, tone, sarcasm, and the way it is expressed.

For example:

```text
"I'm fine."

