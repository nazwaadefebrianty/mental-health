import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Mental Health AI",
    page_icon="🧠",
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

/* container spacing */
.block-container {
    padding: 2rem 2.5rem;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================
st.markdown("""
# 🧠 Mental Health AI Dashboard
### Smart System untuk Mendeteksi Risiko Depresi Menggunakan Machine Learning

---
""")

# =========================
# METRICS DASHBOARD
# =========================
c1, c2, c3, c4 = st.columns(4)

c1.metric("AI Models", "1")
c2.metric("Algorithms", "SVM")
c3.metric("Features", "12 Inputs")
c4.metric("Status", "Active 🟢")

st.markdown("---")

# =========================
# FEATURES SECTION
# =========================
st.markdown("## ✨ System Features")

f1, f2, f3 = st.columns(3)

with f1:
    st.info("""
📊 Data Input
- Manual input user
- Upload CSV dataset
- Auto validation
""")

with f2:
    st.info("""
🧠 Machine Learning
- SVM Model
""")

with f3:
    st.info("""
📈 Output System
- Depression prediction
- AI explanation
- Export hasil CSV
""")

st.markdown("---")

# =========================
# HOW IT WORKS
# =========================
st.markdown("## ⚙️ How It Works")

st.markdown("""
1. Input data user (manual / CSV)  
2. Data diproses oleh ML model  
3. Model menghasilkan prediksi risiko  
4. AI memberikan alasan (explanation)  
5. Hasil bisa di-download  

""")

st.markdown("---")

# =========================
# FOOTER
# =========================
st.success("👉 Start using the system from Prediction page (sidebar)")
st.caption("Mental Health AI System • Machine Learning Based Classification")