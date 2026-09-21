import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="centered"
)

model = joblib.load("loan_model.pkl")

st.title("🏦 Loan Approval Prediction")

st.write(
    "Enter applicant details to predict the loan approval status."
)

st.info(
    "This application provides a machine learning prediction "
    "for demonstration purposes. It is not an actual bank decision."
)

st.header("👤 Applicant Information")

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

married = st.selectbox(
    "Married",
    ["No", "Yes"]
)

dependents = st.selectbox(
    "Dependents",
    ["0", "1", "2", "3+"]
)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["No", "Yes"]
)

property_area = st.selectbox(
    "Property Area",
    ["Rural", "Semiurban", "Urban"]
)

credit_history = st.selectbox(
    "Credit History",
    ["Poor (0)", "Good (1)"]
)

st.header("💰 Financial Information")

applicant_income = st.number_input(
    "Applicant Income",
    min_value=0,
    value=10000,
    step=500
)

coapplicant_income = st.number_input(
    "Coapplicant Income",
    min_value=0,
    value=5000,
    step=500
)

loan_amount = st.number_input(
    "Loan Amount (in thousands)",
    min_value=0,
    value=100,
    step=10
)

loan_term = st.number_input(
    "Loan Amount Term (in days)",
    min_value=0,
    value=360,
    step=30
)

predict_button = st.button(
    "🔮 Predict Loan Approval",
    type="primary"
)

if predict_button:

    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=model.feature_names_in_
    )

    input_data.loc[0, "ApplicantIncome"] = applicant_income
    input_data.loc[0, "CoapplicantIncome"] = coapplicant_income
    input_data.loc[0, "LoanAmount"] = loan_amount
    input_data.loc[0, "Loan_Amount_Term"] = loan_term

    if credit_history == "Good (1)":
        input_data.loc[0, "Credit_History"] = 1
    else:
        input_data.loc[0, "Credit_History"] = 0

    if gender == "Male":
        input_data.loc[0, "Gender_Male"] = 1

    if married == "Yes":
        input_data.loc[0, "Married_Yes"] = 1

    if dependents == "1":
        input_data.loc[0, "Dependents_1"] = 1

    if dependents == "2":
        input_data.loc[0, "Dependents_2"] = 1

    if dependents == "3+":
        input_data.loc[0, "Dependents_3+"] = 1

    if education == "Not Graduate":
        input_data.loc[0, "Education_Not Graduate"] = 1

    if self_employed == "Yes":
        input_data.loc[0, "Self_Employed_Yes"] = 1

    if property_area == "Semiurban":
        input_data.loc[0, "Property_Area_Semiurban"] = 1

    if property_area == "Urban":
        input_data.loc[0, "Property_Area_Urban"] = 1

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    classes = list(model.classes_)

    if 1 in classes:
        approval_index = classes.index(1)
        approval_probability = probabilities[approval_index]
    else:
        approval_probability = 0

    st.divider()

    st.header("📊 Prediction Result")

    if prediction == 1:

        st.success("✅ Loan Prediction: APPROVED")

        st.metric(
            "Estimated Approval Probability",
            f"{approval_probability * 100:.2f}%"
        )

        st.progress(float(approval_probability))

    else:

        st.error("❌ Loan Prediction: REJECTED")

        st.metric(
            "Estimated Approval Probability",
            f"{approval_probability * 100:.2f}%"
        )

        st.progress(float(approval_probability))

    st.caption(
        "Prediction is based on the trained Logistic Regression model "
        "and the information entered above."
    )
