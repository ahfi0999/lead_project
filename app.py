import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ==========================================
# 1. LOAD THE TRAINED MODEL
# ==========================================
# Load the files created by training_script.py
try:
    model = joblib.load('lead_scoring_model.pkl')
    scaler = joblib.load('scaler.pkl')
    model_columns = joblib.load('model_columns.pkl')
except FileNotFoundError:
    st.error("Error: Model files not found. Did you run 'training_script.py'?")
    st.stop()

# ==========================================
# 2. APP TITLE & LAYOUT
# ==========================================
st.set_page_config(page_title="Coaching Lead Scorer", layout="centered")

st.title("Coaching Lead Conversion Predictor")
st.markdown("### Identify high-potential leads and improve enrollments")
st.write("Enter lead details below to predict the probability of conversion.")

# ==========================================
# 3. SIDEBAR - USER INPUTS
# ==========================================
st.sidebar.header("Lead Information")

# --- NUMERICAL INPUTS ---
time_spent = st.sidebar.slider(
    "Total Time Spent on Website (Seconds)",
    0, 2000, 500,
    help="More time usually indicates higher interest"
)

total_visits = st.sidebar.number_input(
    "Total Visits",
    min_value=0,
    max_value=50,
    value=3
)

page_views = st.sidebar.number_input(
    "Page Views Per Visit",
    min_value=0.0,
    max_value=20.0,
    value=2.0
)

# --- CATEGORICAL INPUTS ---
occupation = st.sidebar.selectbox(
    "Occupation",
    ['Unemployed', 'Working Professional', 'Student', 'Other', 'Housewife', 'Businessman']
)

lead_source = st.sidebar.selectbox(
    "Lead Source",
    ['Google', 'Direct Traffic', 'Olark Chat', 'Organic Search', 'Reference', 'Welingak Website']
)

city = st.sidebar.selectbox(
    "City",
    ['Mumbai', 'Thane & Outskirts', 'Other Metro Cities', 'Other Cities', 'Tier II Cities']
)

last_activity = st.sidebar.selectbox(
    "Last Activity",
    [
        'Email Opened', 'SMS Sent', 'Olark Chat Conversation',
        'Page Visited on Website', 'Converted to Lead',
        'Email Bounced', 'Unreachable'
    ]
)

# Tags are strong predictors
tags = st.sidebar.selectbox(
    "Sales Tag (Current Status)",
    [
        'Will revert after reading the email', 'Ringing',
        'Interested in other courses', 'Closed by Horizzon',
        'switched off', 'Busy', 'Lost to EINS',
        'Not doing further education', 'invalid number',
        'number not provided', 'Interested in Next batch'
    ]
)

# ==========================================
# 4. PREDICTION LOGIC
# ==========================================
if st.button("Predict Conversion Score"):

    # A. Initialize a blank row with all model columns set to zero
    input_data = pd.DataFrame(columns=model_columns)
    input_data.loc[0] = 0

    # Force numeric data types
    input_data = input_data.astype(float)

    # B. Fill numerical values
    input_data.loc[0, 'Total Time Spent on Website'] = time_spent
    input_data.loc[0, 'TotalVisits'] = total_visits
    input_data.loc[0, 'Page Views Per Visit'] = page_views

    # C. Fill categorical values using manual one-hot encoding
    def set_col_value(prefix, value):
        col_name = f"{prefix}_{value}"
        if col_name in input_data.columns:
            input_data.loc[0, col_name] = 1

    set_col_value("What is your current occupation", occupation)
    set_col_value("Lead Source", lead_source)
    set_col_value("City", city)
    set_col_value("Last Activity", last_activity)
    set_col_value("Tags", tags)

    # D. Scale the input using the saved scaler
    input_scaled = scaler.transform(input_data)

    # E. Generate prediction probability
    prediction_prob = model.predict_proba(input_scaled)[0][1]
    score = round(prediction_prob * 100)

    # ==========================================
    # 5. DISPLAY RESULTS
    # ==========================================
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Conversion Probability", value=f"{score}%")

    with col2:
        if score >= 80:
            st.success(
                "HOT LEAD\n\n"
                "Recommended action: Call immediately."
            )
        elif score >= 50:
            st.warning(
                "WARM LEAD\n\n"
                "Recommended action: Send an email follow-up."
            )
        else:
            st.error(
                "COLD LEAD\n\n"
                "Recommended action: Keep in nurturing list."
            )

    # Optional debug view
    with st.expander("View processed input data"):
        st.write(input_data)
