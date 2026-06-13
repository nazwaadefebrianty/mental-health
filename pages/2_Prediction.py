from modules.knn import predict_knn
from modules.svm import predict_svm
from modules.decision_tree import predict_dt

import streamlit as st
import pandas as pd
import numpy as np

# =========================
# CONFIG UI
# =========================

st.set_page_config(
    page_title="Mental Health AI Pro Max",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0b0f1a, #111827);
    color: #ffffff;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto;
}

section[data-testid="stSidebar"] {
    background: rgba(20, 20, 30, 0.6);
    backdrop-filter: blur(20px);
}

.stButton>button {
    width: 100%;
    border-radius: 14px;
    background: linear-gradient(135deg, #007AFF, #5856D6);
    color: white;
    font-weight: 600;
}

[data-testid="stMetric"] {
    background: rgba(255,255,255,0.06);
    border-radius: 16px;
    padding: 1rem;
}
</style>
""", unsafe_allow_html=True)

# =========================
# MENU
# =========================

menu = st.sidebar.radio(
    "📌 Navigation",
    ["🏠 Dashboard", "📊 Prediction", "📈 Analytics"]
)

# =========================
# ENCODING
# =========================

gender_map = {"Female": 0, "Male": 1}
social_map = {"Low": 0, "Medium": 1, "High": 2}
platform_map = {"Both": 0, "Instagram": 1, "Tiktok": 2}

# =========================
# DASHBOARD (UPGRADED UI)
# =========================

if menu == "🏠 Dashboard":

    st.markdown("""
    <div style="
        padding: 2rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #0f172a, #1e293b);
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        margin-bottom: 20px;
    ">
        <h1 style="color:white; margin-bottom:0;">
            🧠 Mental Health AI System
        </h1>
        <p style="color:#cbd5e1; font-size:16px;">
            AI-powered Depression Risk Detection using Machine Learning (KNN, SVM, Decision Tree)
        </p>
    </div>
    """, unsafe_allow_html=True)

    # HERO STATS
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="
            padding: 20px;
            border-radius: 16px;
            background: rgba(59,130,246,0.15);
            border: 1px solid rgba(59,130,246,0.3);
        ">
            <h3>🤖 AI Models</h3>
            <h2>KNN / SVM / DT</h2>
            <p style="color:#94a3b8;">3 Machine Learning algorithms</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
            padding: 20px;
            border-radius: 16px;
            background: rgba(34,197,94,0.15);
            border: 1px solid rgba(34,197,94,0.3);
        ">
            <h3>📊 System Type</h3>
            <h2>Classification AI</h2>
            <p style="color:#94a3b8;">Binary Risk Prediction</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="
            padding: 20px;
            border-radius: 16px;
            background: rgba(168,85,247,0.15);
            border: 1px solid rgba(168,85,247,0.3);
        ">
            <h3>⚡ Status</h3>
            <h2>Active</h2>
            <p style="color:#94a3b8;">System running normally</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # FEATURE SECTION
    st.markdown("""
    <div style="
        padding: 20px;
        border-radius: 16px;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
    ">
        <h3>📌 What This System Does</h3>
        <ul>
            <li>🔍 Analyzes social media behavior</li>
            <li>😴 Evaluates sleep patterns</li>
            <li>📱 Detects digital addiction level</li>
            <li>🧠 Predicts depression risk using AI</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # CALL TO ACTION
    st.markdown("""
    <div style="
        text-align:center;
        padding: 20px;
        border-radius: 16px;
        background: linear-gradient(90deg, #2563eb, #7c3aed);
    ">
        <h3 style="color:white;">🚀 Ready to start prediction?</h3>
        <p style="color:#e2e8f0;">Go to Prediction menu in sidebar</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# PREDICTION
# =========================

elif menu == "📊 Prediction":

    st.title("📊 Prediction System")

    input_method = st.radio("Input Method", ["Manual Input", "Upload CSV"], horizontal=True)
    model_choice = st.radio("Model", ["KNN", "SVM", "Decision Tree"], horizontal=True)

    # =========================
    # MANUAL
    # =========================

    if input_method == "Manual Input":

        c1, c2 = st.columns(2)

        with c1:
            age = st.slider("Age", 10, 30, 18)
            gender = st.selectbox("Gender", ["Female", "Male"])
            social_hours = st.slider("Social Media Hours", 0.0, 15.0, 5.0)
            platform = st.selectbox("Platform", ["Both", "Instagram", "Tiktok"])
            screen_time = st.slider("Screen Before Sleep", 0.0, 10.0, 2.0)

        with c2:
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

            # =========================
            # REASON ENGINE
            # =========================

            reasons = []

            if stress >= 7:
                reasons.append("High stress level")
            if anxiety >= 7:
                reasons.append("High anxiety level")
            if sleep < 6:
                reasons.append("Low sleep duration")
            if social_hours > 8:
                reasons.append("Excessive social media usage")
            if screen_time > 3:
                reasons.append("High screen time before sleep")
            if addiction >= 7:
                reasons.append("High addiction level")

            st.subheader("📊 Result")

            if result == 1:
                st.error("🔴 Depresi Terdeteksi")

                st.subheader("🧠 AI Explanation")

                if len(reasons) == 0:
                    st.warning("Risk detected but no strong factor found")
                else:
                    for r in reasons:
                        st.warning("⚠️ " + r)
            else:
                st.success("🟢 Tidak Depresi")
                st.info("No major risk detected")

    # =========================
    # CSV
    # =========================

    else:

        st.subheader("📂 Upload Dataset")
        uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

        if uploaded_file is not None:

            df = pd.read_csv(uploaded_file)
            st.dataframe(df.head())

            if st.button("📊 Predict Dataset"):

                results = []
                all_reasons = []

                for _, row in df.iterrows():

                    data = [
                        int(row["age"]),
                        gender_map.get(row["gender"], 0),
                        float(row["daily_social_media_hours"]),
                        platform_map.get(row["platform_usage"], 0),
                        float(row["sleep_hours"]),
                        float(row["screen_time_before_sleep"]),
                        float(row["academic_performance"]),
                        float(row["physical_activity"]),
                        social_map.get(row["social_interaction_level"], 0),
                        int(row["stress_level"]),
                        int(row["anxiety_level"]),
                        int(row["addiction_level"])
                    ]

                    model = predict_knn if model_choice == "KNN" else predict_svm if model_choice == "SVM" else predict_dt
                    pred = model(data)
                    results.append(pred)

                    reasons = []

                    if data[9] >= 7:
                        reasons.append("High stress")
                    if data[10] >= 7:
                        reasons.append("High anxiety")
                    if data[4] < 6:
                        reasons.append("Low sleep")
                    if data[2] > 8:
                        reasons.append("High social media usage")
                    if data[11] >= 7:
                        reasons.append("High addiction")

                    all_reasons.append(", ".join(reasons))

                df["prediction"] = results
                df["prediction"] = df["prediction"].apply(lambda x: "Depresi" if x == 1 else "Tidak Depresi")
                df["reason"] = all_reasons

                st.success("Prediction completed 🚀")
                st.dataframe(df)

                st.download_button(
                    "⬇️ Download Result",
                    df.to_csv(index=False).encode("utf-8"),
                    "result.csv",
                    "text/csv"
                )

# =========================
# ANALYTICS
# =========================

else:

    st.title("📈 Model Analytics")

    chart = pd.DataFrame({
        "Model": ["KNN", "SVM", "Decision Tree"],
        "Accuracy": [78, 85, 80]
    })

    st.bar_chart(chart.set_index("Model"))
    st.success("SVM is best performing 🚀")