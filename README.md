# 🛡️ Fake Job Posting Detection using Machine Learning

A Machine Learning and Natural Language Processing (NLP) based web application that detects whether a job posting is **Genuine** or **Fraudulent**. The project uses text preprocessing, feature engineering, and machine learning algorithms to help identify fake job advertisements.

---

## 📌 Project Overview

Fake job postings have become increasingly common across online job portals. These fraudulent advertisements often deceive job seekers into sharing sensitive information or paying money.

This project applies **Natural Language Processing (NLP)** and **Machine Learning** techniques to automatically classify job postings as **Genuine** or **Fraudulent**.

The application provides an easy-to-use **Streamlit web interface** where users can enter job posting details and receive instant predictions.

---

## 🚀 Features

- 🔍 Detects Genuine and Fraudulent Job Postings
- 🤖 Machine Learning-based Prediction
- 📝 NLP Text Processing using TF-IDF
- 🎨 Interactive Streamlit Web Application
- ⚡ Real-time Prediction
- ✅ User-friendly Interface
- 📊 Model Comparison and Evaluation

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Text Preprocessing
5. Feature Engineering
   - TF-IDF Vectorization
   - One-Hot Encoding
6. Model Training
7. Hyperparameter Tuning
8. Model Evaluation
9. Best Model Selection
10. Web Application Deployment

---

## 🤖 Machine Learning Models Evaluated

- K-Nearest Neighbors (KNN)
- Naive Bayes
- Decision Tree
- Logistic Regression (Optimized)

---

## 🏆 Final Selected Model

**Logistic Regression (Optimized)**

Selected based on the highest **F1-Score** after hyperparameter tuning and model comparison.

### Performance

| Metric | Score |
|---------|-------|
| Accuracy | **98.41%** |
| Precision | **89.73%** |
| Recall | **75.72%** |
| F1 Score | **82.13%** |
| Cross Validation Score | **0.8003** |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorizer
- Joblib
- Streamlit
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```
Fake-Job-Posting-Detection/
│
├── app.py
├── fake_job_detector.pkl
├── requirements.txt
├── Job_Posting_Detection.ipynb
├── fake_job_postings.csv
├── README.md
└── .gitignore
```

---

## ▶️ Installation

### Clone the Repository

```bash
git clone https://github.com/Mainuddin123/Fake-Job-Posting-Detection.git
```

### Navigate to the Project

```bash
cd Fake-Job-Posting-Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📷 Application Preview

### Home Page
<img width="945" height="921" alt="image" src="https://github.com/user-attachments/assets/3afd4a51-5299-4c89-a821-3e56fe013f13" />


### Genuine Job Prediction
<img width="958" height="925" alt="WhatsApp Image 2026-06-28 at 8 23 40 PM" src="https://github.com/user-attachments/assets/ba0087bb-eb08-4fdf-8376-36976ba111fd" />

### Fraudulent Job Prediction
<img width="953" height="915" alt="WhatsApp Image 2026-06-28 at 8 22 09 PM" src="https://github.com/user-attachments/assets/2834d67d-8bd6-4248-8dd2-cd73973e69e0" />


---

## 📊 Dataset

The project uses a Fake Job Posting dataset containing:

- Job Description
- Employment Type
- Required Experience
- Required Education
- Industry
- Function
- Remote Job
- Company Logo
- Application Questions
- Fraudulent Label

---
🌐 Live Demo

Fake Job Posting Detection:
https://fake-job-posting-detection-kjyzqwhnbh2fyigss7ftr3.streamlit.app/



## 🎯 Future Enhancements

- Deep Learning Models (LSTM/BERT)
- Explainable AI (SHAP/LIME)
- Confidence Score Visualization
- Batch Prediction
- REST API Deployment
- Cloud Deployment

---

## 👨‍💻 Developed By

**Khaja Mainuddin**

Artificial Intelligence and Data Science Graduate

---

## 📬 Connect With Me

**GitHub**

https://github.com/Mainuddin123

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is intended for educational and research purposes.
