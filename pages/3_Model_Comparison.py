import streamlit as st
import pandas as pd

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Model Comparison",
    page_icon="📈",
    layout="wide"
)

# =========================
# APPLE STYLE UI
# =========================
st.markdown("""
<style>

.main {
    background: linear-gradient(135deg, #0b0f1a, #111827);
    color: white;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI";
}

/* sidebar */
section[data-testid="stSidebar"] {
    background: rgba(20, 20, 30, 0.6);
    backdrop-filter: blur(20px);
}

/* metric cards */
[data-testid="stMetric"] {
    background: rgba(255,255,255,0.06);
    padding: 1rem;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.08);
}

/* block spacing */
.block-container {
    padding: 2rem 2.5rem;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown("# 📈 Model Performance Dashboard")
st.markdown("### Perbandingan performa model Machine Learning untuk deteksi depresi")

st.markdown("---")

# =========================
# DATA MODEL
# =========================
svm_acc = 85

best_model = "SVM"

# =========================
# METRIC CARDS
# =========================
c1, c2, c3 = st.columns(3)


with c2:
    st.metric(
        label="SVM 🏆 Best Model",
        value=f"{svm_acc}%",
        delta="+ highest accuracy"
    )


st.markdown("---")

# =========================
# INSIGHT SECTION
# =========================
st.markdown("## 🧠 Model Insight")

st.info("""
- **SVM** memiliki akurasi tertinggi → paling stabil untuk dataset ini  
""")

st.markdown("---")

# =========================
# CHART
# =========================
st.markdown("## 📊 Accuracy Comparison")

df = pd.DataFrame({
    "Model": ["SVM"],
    "Accuracy": [svm_acc]
})

st.bar_chart(df.set_index("Model"))

# =========================
# CONCLUSION
# =========================
st.markdown("---")

st.success("🏆 Best Performing Model: SVM (Recommended for deployment)")
st.caption("Model evaluation based on current training dataset")