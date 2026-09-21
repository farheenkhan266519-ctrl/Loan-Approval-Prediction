# Loan Approval Prediction

## 📌 Project Overview

This project uses Machine Learning to predict whether a loan application may be **approved or rejected** based on applicant information.

The project was developed as part of my **Machine Learning Internship at Big Brains**.

The main goal is to understand the complete Machine Learning workflow, from data exploration and preprocessing to model training, evaluation, prediction, documentation, and deployment.

---

## 🎯 Problem Statement

Loan approval decisions depend on several applicant details such as income, education, employment status, loan amount, and credit history.

The objective of this project is to build a Machine Learning classification model that can predict the loan approval status of an applicant.

---

## 📊 Dataset

The project uses a **Loan Approval Prediction Dataset** containing information about loan applicants.

Important features include:

* Gender
* Married
* Dependents
* Education
* Self Employment
* Applicant Income
* Coapplicant Income
* Loan Amount
* Loan Term
* Credit History
* Property Area

### Target Variable

**Loan Status**

* `Y` = Loan Approved
* `N` = Loan Rejected

---

## 🔧 Data Preprocessing

The dataset was prepared before training the Machine Learning model.

The preprocessing steps included:

1. Checking for missing values
2. Checking and removing duplicate records
3. Checking data types
4. Handling categorical variables
5. Encoding categorical data
6. Preparing input features and target variable
7. Splitting the data into training and testing sets

The final cleaned dataset was saved as:

`cleaned_loan_dataset.csv`

---

## 🔍 Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed to understand the dataset and identify relationships between applicant information and loan approval.

The analysis focused on:

* Loan approval distribution
* Credit history
* Applicant income
* Loan amount
* Education
* Employment status
* Relationships between important features

### Important Findings

* Credit history is an important factor associated with loan approval.
* Applicant and coapplicant income provide useful information for understanding loan applications.
* Loan amount and applicant characteristics can have a relationship with approval status.
* Categorical features such as education and employment status were also analyzed.

---

## 🤖 Machine Learning Model

### Logistic Regression

**Logistic Regression** was selected as the classification model because the target variable contains two possible outcomes:

* Approved
* Rejected

The dataset was divided into training and testing data.

The model was trained using the training dataset and then used to predict loan approval on unseen test data.

The trained model was saved as:

`loan_model.pkl`

---

## 📈 Model Evaluation

The Logistic Regression model was evaluated using Accuracy, Precision, Recall, F1-Score, and ROC-AUC.

| Metric    |     Result |
| --------- | ---------: |
| Accuracy  | **84.55%** |
| Precision | **82.35%** |
| Recall    | **98.82%** |
| F1-Score  | **89.84%** |
| ROC-AUC   | **84.18%** |

### Model Analysis

The model achieved an accuracy of **84.55%** on the test data.

The recall was **98.82%**, meaning the model correctly identified most of the positive loan approval cases in the test set.

The F1-Score of **89.84%** shows a balance between precision and recall.

The ROC-AUC score of **84.18%** indicates that the model has useful ability to distinguish between the two loan-status classes.

---

## 🔮 Prediction

The trained Logistic Regression model can be used to predict the loan status of an applicant.

The prediction process provides:

* Loan approval/rejection prediction
* Approval probability

### Example Prediction

```text
Loan Prediction: APPROVED
Estimated Approval Probability: 96.09%
```

The prediction application was successfully tested using applicant information and generated an approved prediction with an estimated approval probability of **96.09%**.

---

## 🌐 Deployment

The Machine Learning application was deployed using **Streamlit Community Cloud**.

The deployed application allows users to enter applicant information and receive a loan prediction and estimated approval probability through a web interface.

### Live Application

https://loan-approval-prediction-qc6kbltaix7xpvbgxunfy9.streamlit.app/

---

## 📁 Project Files

The GitHub repository contains the following project files:

```text
Loan-Approval-Prediction/
│
├── Loan_Approval_Prediction.ipynb
├── README.md
├── app.py
├── loan-project-screenshots.docx
├── loan_model.pkl
└── requirements.txt
```

### File Descriptions

| File                             | Description                                                                                                                    |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `Loan_Approval_Prediction.ipynb` | Complete Machine Learning notebook containing data exploration, preprocessing, EDA, model training, evaluation, and prediction |
| `README.md`                      | Complete documentation of the Loan Approval Prediction project                                                                 |
| `app.py`                         | Streamlit web application used to generate loan approval predictions                                                           |
| `loan-project-screenshots.docx`  | Document containing screenshots and proof of the completed project work                                                        |
| `loan_model.pkl`                 | Trained Logistic Regression Machine Learning model                                                                             |
| `requirements.txt`               | Required Python libraries for running the Streamlit application                                                                |

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit
* Google Colab
* GitHub
* Streamlit Community Cloud

---

## ⚠️ Limitations

This project is developed for educational and demonstration purposes.

The model's predictions depend on the quality and characteristics of the dataset used for training.

The dataset may not represent every real-world loan applicant.

A Machine Learning prediction should not be considered a guaranteed real-world loan approval decision.

The application should not be used as a replacement for professional banking or financial decisions.

---

## 🎓 Learning Outcomes

Through this project, I learned how to:

* Collect and explore a dataset
* Clean and preprocess data
* Handle categorical variables
* Perform Exploratory Data Analysis
* Prepare data for Machine Learning
* Train a Logistic Regression model
* Evaluate classification performance
* Generate predictions and probabilities
* Build a Streamlit Machine Learning application
* Deploy a Machine Learning application
* Use GitHub for project presentation
* Document a complete Machine Learning project
* Understand an end-to-end Machine Learning workflow

---

## 👩‍💻 Author

**Farheen Khan**

Computer Science Student
University of Management and Technology (UMT), Lahore

### GitHub

https://github.com/farheenkhan266519-ctrl

### Project Repository

https://github.com/farheenkhan266519-ctrl/Loan-Approval-Prediction

---

## ⭐ Project Status

**Completed ✅**

The project includes data preprocessing, exploratory analysis, Logistic Regression model training, model evaluation, prediction, Streamlit deployment, GitHub publication, and complete project documentation.
