import streamlit as st
import pandas as pd
import joblib

# Page settings

st.set_page_config(
page_title="Loan Approval Prediction",
page_icon="🏦",
layout="centered"
)

# Load trained model

@st.cache_resource
def load_model():
return joblib.load("loan_model.pkl")

model = load_model()

# Title

st.title("🏦 Loan Approval Prediction")

st.write(
"Enter applicant details to predict the loan approval status "
"using a trained Machine Learning model."
)

st.info(
"This application provides a machine learning prediction "
"for demonstration purposes. It is not an actual bank decision."
)

# Applicant Information

st.header("👤 Applicant Information")

col1, col2 = st.columns(2)

with col1:
gender = st.selectbox(
"Gender",
["Female", "Male"]
)

```
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
```

with col2:
self_employed = st.selectbox(
"Self Employed",
["No", "Yes"]
)

```
property_area = st.selectbox(
    "Property Area",
    ["Rural", "Semiurban", "Urban"]
)

credit_history = st.selectbox(
    "Credit History",
    ["Good (1)", "Poor (0)"]
)
```

# Financial Information

st.header("💰 Financial Information")

applicant_income = st.number_input(
"Applicant Income",
min_value=0,
value=5000,
step=500
)

coapplicant_income = st.number_input(
"Coapplicant Income",
min_value=0,
value=0,
step=500
)

loan_amount = st.number_input(
"Loan Amount (in thousands)",
min_value=0,
value=150,
step=10
)

loan_term = st.number_input(
"Loan Amount Term (in days)",
min_value=0,
value=360,
step=30
)

# Prediction

if st.button("🔮 Predict Loan Approval", type="primary"):

```
try:
    # Create input DataFrame using the exact model columns
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=model.feature_names_in_
    )

    # Numerical features
    input_data.loc[0, "ApplicantIncome"] = applicant_income
    input_data.loc[0, "CoapplicantIncome"] = coapplicant_income
    input_data.loc[0, "LoanAmount"] = loan_amount
    input_data.loc[0, "Loan_Amount_Term"] = loan_term

    input_data.loc[0, "Credit_History"] = (
        1 if credit_history == "Good (1)" else 0
    )

    # Categorical features
    if gender == "Male":
        input_data.loc[0, "Gender_Male"] = 1

    if married == "Yes":
        input_data.loc[0, "Married_Yes"] = 1

    if dependents == "1":
        input_data.loc[0, "Dependents_1"] = 1
    elif dependents == "2":
        input_data.loc[0, "Dependents_2"] = 1
    elif dependents == "3+":
        input_data.loc[0, "Dependents_3+"] = 1

    if education == "Not Graduate":
        input_data.loc[0, "Education_Not Graduate"] = 1

    if self_employed == "Yes":
        input_data.loc[0, "Self_Employed_Yes"] = 1

    if property_area == "Semiurban":
        input_data.loc[0, "Property_Area_Semiurban"] = 1
    elif property_area == "Urban":
        input_data.loc[0, "Property_Area_Urban"] = 1

    # Make prediction
    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    classes = list(model.classes_)

    # Find approval probability
    approval_probability = None

    if "Y" in classes:
        approval_probability = probabilities[
            classes.index("Y")
        ]

    # Display result
    st.divider()

    st.header("📊 Prediction Result")

    if str(prediction).upper() == "Y":
        st.success("✅ Loan Prediction: APPROVED")
    else:
        st.error("❌ Loan Prediction: REJECTED")

    # Approval probability
    if approval_probability is not None:
        st.metric(
            "Estimated Approval Probability",
            f"{approval_probability * 100:.2f}%"
        )

        st.progress(
            float(approval_probability)
        )

    # Applicant Summary
    st.subheader("👤 Applicant Summary")

    summary_col1, summary_col2 = st.columns(2)

    with summary_col1:
        st.write(f"**Gender:** {gender}")
        st.write(f"**Married:** {married}")
        st.write(f"**Dependents:** {dependents}")
        st.write(f"**Education:** {education}")

    with summary_col2:
        st.write(f"**Self Employed:** {self_employed}")
        st.write(f"**Property Area:** {property_area}")
        st.write(f"**Credit History:** {credit_history}")

    st.caption(
        "Prediction is based on the trained Logistic Regression "
        "model and the information entered above."
    )

except Exception as e:
    st.error(
        "An error occurred while making the prediction."
    )

    st.code(str(e))
```
