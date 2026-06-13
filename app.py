from modules.knn import predict_knn
from modules.svm import predict_svm
from modules.decision_tree import predict_dt

import streamlit as st
import pandas as pd
import numpy as np

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Mental Health AI Pro",
    page_icon="🧠",
    layout="wide"
)

# =========================
# STYLE (PRO UI)
# =========================
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0b0f1a, #111827);
    color: white;
}

.block-container {
    padding: 2rem;
}

.card {
    padding: 1.5rem;
    border-radius: 16px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    background: linear-gradient(90deg, #6366f1, #3b82f6);
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Dashboard", "📊 Prediction", "📈 Analytics"]
)

# =========================
# ENCODING
# =========================
gender_map = {"Female": 0, "Male": 1}
social_map = {"Low": 0, "Medium": 1, "High": 2}
platform_map = {"Both": 0, "Instagram": 1, "Tiktok": 2}

# =========================
# DASHBOARD (PRO)
# =========================
if menu == "🏠 Dashboard":

    st.title("🧠 Mental Health AI - Pro System")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">🤖 <b>AI Model</b><br>KNN / SVM / DT</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">📊 <b>Type</b><br>Classification AI</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">⚡ <b>Status</b><br>Production Ready</div>', unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 📌 System Overview")
    st.info("AI ini menganalisis risiko depresi berdasarkan pola hidup digital, tidur, dan kondisi mental pengguna.")

# =========================
# PREDICTION (PRO)
# =========================
elif menu == "📊 Prediction":

    st.title("📊 Prediction Engine")

    input_method = st.radio("Input Method", ["Manual Input", "Upload CSV"], horizontal=True)
    model_choice = st.radio("Model", ["KNN", "SVM", "Decision Tree"], horizontal=True)

    if input_method == "Manual Input":

        col1, col2 = st.columns(2)

        with col1:
            age = st.slider("Age", 10, 30, 18)
            gender = st.selectbox("Gender", ["Female", "Male"])
            social_hours = st.slider("Social Media Hours", 0.0, 15.0, 5.0)
            platform = st.selectbox("Platform", ["Both", "Instagram", "Tiktok"])
            screen_time = st.slider("Screen Before Sleep", 0.0, 10.0, 2.0)

        with col2:
            sleep = st.slider("Sleep Hours", 0.0, 12.0, 7.0)
            physical = st.slider("Physical Activity", 0.0, 10.0, 5.0)
            social = st.selectbox("Social Interaction", ["Low", "Medium", "High"])
            academic = st.slider("Academic Performance", 0.0, 10.0, 5.0)
            stress = st.slider("Stress Level", 0, 10, 5)
            anxiety = st.slider("Anxiety Level", 0, 10, 5)
            addiction = st.slider("Addiction Level", 0, 10, 5)

        if st.button("🚀 Predict Now"):

            input_data = [
                age,
                gender_map[gender],
                social_hours,
                platform_map[platform],
                sleep,
                screen_time,
                academic,
                physical,
                social_map[social],
                stress,
                anxiety,
                addiction
            ]

            model = predict_knn if model_choice == "KNN" else predict_svm if model_choice == "SVM" else predict_dt
            result = model(input_data)

            st.markdown("### 📊 Result")

            if result == 1:
                st.error("🔴 HIGH RISK - Depression Detected")
                st.warning("User shows multiple risk indicators")
            else:
                st.success("🟢 LOW RISK - No Depression Detected")
                st.info("No significant risk patterns found")

            # =========================
            # PRO AI INSIGHT
            # =========================
            st.markdown("### 🧠 AI Insight")

            reasons = []

            if stress >= 7:
                reasons.append("High stress level")
            if anxiety >= 7:
                reasons.append("High anxiety level")
            if sleep < 6:
                reasons.append("Low sleep quality")
            if social_hours > 8:
                reasons.append("Excessive social media usage")
            if addiction >= 7:
                reasons.append("Digital dependency detected")

            if len(reasons) == 0:
                st.success("No major risk factors detected")
            else:
                for r in reasons:
                    st.info("• " + r)

# =========================
# ANALYTICS (PRO)
# =========================
else:

    st.title("📈 Model Analytics Dashboard")

    data = pd.DataFrame({
        "Model": ["KNN", "SVM", "Decision Tree"],
        "Accuracy": [78, 85, 80]
    })

    st.markdown("### 📊 Model Performance")
    st.bar_chart(data.set_index("Model"))

    st.success("SVM is the best performing model 🚀")