import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Fake Job Posting Detection",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(to right,#f4f8ff,#eef5ff);
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:linear-gradient(to bottom,#0f172a,#1e3a8a);
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Title */
h1{
    color:#1e3a8a !important;
    text-align:center;
}

/* Form */
div[data-testid="stForm"]{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0 8px 20px rgba(0,0,0,.08);
}

/* Button */
div[data-testid="stForm"] button{
    width:100%;
    height:58px;
    background:linear-gradient(90deg,#2563EB,#4F46E5,#7C3AED) !important;
    color:white !important;
    border:none !important;
    border-radius:12px !important;
    font-size:18px !important;
    font-weight:700 !important;
    letter-spacing:.5px;
    cursor:pointer;
    transition:all .3s ease;
    box-shadow:0 8px 20px rgba(37,99,235,.35);
}

div[data-testid="stForm"] button:hover{
    background:linear-gradient(90deg,#1D4ED8,#4338CA,#6D28D9) !important;
    color:white !important;
    transform:translateY(-2px);
    box-shadow:0 10px 24px rgba(37,99,235,.45);
}


/* Footer */
footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("fake_job_detector.pkl")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.markdown(
    "<h2 style='text-align:center;'>🛡️ Fake Job Posting Detection</h2>",
    unsafe_allow_html=True
)

st.sidebar.success("🛡️ AI-Powered Job Fraud Detection")

st.sidebar.markdown("---")

st.sidebar.markdown("### 📌 Project Details")

st.sidebar.write(
    "This application predicts whether a job posting is genuine or fraudulent using Machine Learning."
)

st.sidebar.success("✅ Genuine Job Posting")

st.sidebar.error("🚨 Fraudulent Job Posting")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🧠 Models Compared")

st.sidebar.success("🏆 Logistic Regression (Optimized)")

st.sidebar.markdown("""
✔ K-Nearest Neighbors (KNN)

✔ Gaussian Naive Bayes

✔ Decision Tree
""")

st.sidebar.markdown("---")

st.sidebar.markdown("### 💻 Technologies")

st.sidebar.markdown("""
🐍 Python

📊 Pandas

🧠 Scikit-learn

📝 NLP (TF-IDF)

💾 Joblib

🎨 Streamlit
""")


# -----------------------------
# Title
# -----------------------------
st.markdown("""
<div style="
    background:linear-gradient(90deg,#EAF2FF,#F8FBFF);
    padding:20px;
    border-radius:15px;
    text-align:center;
    border:1px solid #D6E4FF;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
">

<h1 style="
    color:#1E3A8A;
    margin-bottom:0;
    font-size:42px;
">
🛡️ Fake Job Posting Detection
</h1>
            
</div>
""", unsafe_allow_html=True)
st.markdown("", unsafe_allow_html=True)

# -----------------------------
# Input Form
# -----------------------------
with st.form("prediction_form"):

    clean_text = st.text_area(
        "📝 Job Posting Details",
        height=300,
        placeholder="Paste the complete job posting here (description, requirements, benefits, etc.)..."
    )

    col1, col2 = st.columns(2)

    with col1:

        employment_type = st.selectbox(
            "💼 Employment Type",
            [
                "Full-time",
                "Part-time",
                "Contract",
                "Temporary",
                "Other"
            ]
        )

        required_experience = st.selectbox(
            "📈 Required Experience",
            [
                "Entry level",
                "Associate",
                "Mid-Senior level",
                "Director",
                "Executive",
                "Internship",
                "Not Applicable"
            ]
        )

        required_education = st.selectbox(
            "🎓 Required Education",
            [
                "High School or equivalent",
                "Associate Degree",
                "Bachelor's Degree",
                "Master's Degree",
                "Doctorate",
                "Certification",
                "Vocational",
                "Professional",
                "Some College Coursework Completed",
                "Some High School Coursework",
                "Unspecified",
                "Vocational - HS Diploma",
                "Vocational - Degree"
            ]
        )

    with col2:

        industry = st.selectbox(
            "🏭 Industry",
            [
                "Information Technology and Services",
                "Computer Software",
                "Internet",
                "Marketing and Advertising",
                "Financial Services",
                "Hospital & Health Care",
                "Education Management",
                "Staffing and Recruiting",
                "Accounting",
                "Retail",
                "Other"
            ]
        )

        function = st.selectbox(
            "⚙️ Function",
            [
                "Information Technology",
                "Engineering",
                "Sales",
                "Customer Service",
                "Marketing",
                "Administrative",
                "Finance",
                "Human Resources",
                "Management",
                "Other"
            ]
        )

        telecommuting = st.selectbox(
            "🌐 Remote Job",
            ["No", "Yes"]
        )
        telecommuting = 1 if telecommuting == "Yes" else 0

        has_company_logo = st.selectbox(
            "🏢 Company Logo Available",
            ["Yes", "No"]
        )
        has_company_logo = 1 if has_company_logo == "Yes" else 0

        has_questions = st.selectbox(
            "❓ Application Questions",
            ["Yes", "No"]
        )
        has_questions = 1 if has_questions == "Yes" else 0

    submitted = st.form_submit_button(
        "🔍 Predict Job Authenticity",
        use_container_width=True
    )

# -----------------------------
# Prediction
# -----------------------------
if submitted:

    if clean_text.strip() == "":
        st.warning("⚠️ Please enter the job posting details.")
        st.stop()

    input_data = pd.DataFrame({
        "telecommuting": [telecommuting],
        "has_company_logo": [has_company_logo],
        "has_questions": [has_questions],
        "employment_type": [employment_type],
        "required_experience": [required_experience],
        "required_education": [required_education],
        "industry": [industry],
        "function": [function],
        "clean_text": [clean_text]
    })

    # -----------------------------
    # Hybrid Fraud Detection
    # -----------------------------
    fraud_keywords = [
        "registration fee",
        "processing fee",
        "application fee",
        "bank account",
        "bank details",
        "upi",
        "whatsapp",
        "telegram",
        "guaranteed income",
        "guaranteed salary",
        "earn $5000",
        "earn money fast",
        "earn from home",
        "work from home",
        "no interview",
        "no experience required",
        "limited vacancies",
        "limited seats",
        "pay now",
        "urgent hiring",
        "click here",
        "investment required",
        "send money",
        "instant joining"
    ]

    text = clean_text.lower()

    # Machine Learning Prediction
    prediction = model.predict(input_data)[0]

    # Rule-based override for obvious scams
    if any(keyword in text for keyword in fraud_keywords):
        prediction = 1

    st.divider()

    st.markdown("""
<div style="
background:linear-gradient(90deg,#EEF4FF,#F8FBFF);
padding:18px;
border-radius:14px;
border-left:8px solid #2563EB;
box-shadow:0 4px 12px rgba(0,0,0,.08);
margin-bottom:20px;
">
<h2 style="
margin:0;
color:#1E3A8A;
font-size:28px;
font-weight:700;
">
🎯 Prediction Result
</h2>
</div>
""", unsafe_allow_html=True) 

    if prediction == 0:
        st.success("✅ Genuine Job Posting Detected\n\nThis job posting appears to be authentic based on the Machine Learning analysis.")
        # st.balloons()
    else:
        st.error("🚨 Fraudulent Job Posting Detected\n\nThis job posting contains suspicious patterns and should be verified before applying.")

    st.info(
        "ℹ️ This application provides predictions using a trained Machine Learning model. Results should be used as a decision-support tool and not as the sole basis for hiring decisions."
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.markdown("""
<div style="
text-align:center;
padding:12px;
background:#F8FAFC;
border-radius:12px;
border:1px solid #D1D5DB;
color:#4B5563;
font-size:14px;
">

<h3 style="color:#1E3A8A;margin-bottom:6px;">
👨‍💻 Developed by Khaja Mainuddin
</h4>

<p style="margin:6px 0;">
Artificial Intelligence and Data Science Graduate
</p>

<br>

Built with
🐍 Python &nbsp;|&nbsp;
🤖 Scikit-learn &nbsp;|&nbsp;
🎨 Streamlit

<br>

© 2026 All Rights Reserved

</div>
""", unsafe_allow_html=True)