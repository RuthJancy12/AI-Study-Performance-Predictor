# 🎓 AI Study Performance Predictor

An AI-based machine learning project that predicts student performance using academic and study-related factors.

## 📌 Project Overview

The AI Study Performance Predictor analyzes student-related information and uses a Machine Learning model to predict the student's Final Grade.

The project uses a **Decision Tree Classifier** and provides an interactive web interface using **Streamlit**.

## ✨ Features

- 📊 Student performance prediction
- 📚 Study and academic factor analysis
- 🤖 Decision Tree Machine Learning model
- 🌐 Interactive Streamlit web application
- 🔢 Numerical encoding for categorical features
- 📈 Approximately **91.25% test accuracy**

## 📥 Input Features

The model uses several student-related features, including:

- Study Hours
- Attendance
- Resources
- Extracurricular Activities
- Motivation
- Internet Access
- Gender
- Age
- Learning Style
- Online Courses
- Discussions
- Assignment Completion
- EduTech
- Stress Level

Some categorical features are represented using **numerical encoding such as 0 and 1** so that they can be processed by the Machine Learning model.

## 🤖 Machine Learning Model

**Algorithm:** Decision Tree Classifier

The dataset is divided into training and testing sets.

- Training data: 80%
- Testing data: 20%
- Test Accuracy: **91.25%**

> Accuracy represents the performance of the model on the test dataset and does not guarantee the same accuracy on new real-world data.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- VS Code

## 📂 Project Structure

```text
AI-Study-Performance-Predictor/
│
├── dataset/
│   └── student_performance.csv
│
├── app.py
├── train_model.py
├── student_performance_model.pkl
├── README.md
└── .gitattributes
