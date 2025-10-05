import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import requests
from streamlit_lottie import st_lottie

# ==========================================
# 🔹 Page Config
# ==========================================
st.set_page_config(
    page_title="DreamHome Price Predictor 🏡",
    page_icon="🏠",
    layout="wide"
)

# ==========================================
# 🔹 Custom CSS for Animated Background & Glass Style
# ==========================================
page_bg = """
<style>
.stApp {
    background: linear-gradient(135deg, rgba(34,193,195,0.25), rgba(253,187,45,0.25)),
                url("https://images.unsplash.com/photo-1600585154340-be6161a56a0c") no-repeat center center fixed;
    background-size: cover;
    font-family: 'Segoe UI', sans-serif;
}

.block-container {
    background: rgba(255, 255, 255, 0.75);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 4px 25px rgba(0,0,0,0.2);
}

h1, h2, h3, h4 {
    color: #1A1A1A !important;
    text-shadow: 1px 1px 2px rgba(255,255,255,0.6);
}

.stButton>button {
    background-color: #008CBA;
    color: white;
    border-radius: 10px;
    font-size: 18px;
    height: 3em;
    width: 100%;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #00AEEF;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ==========================================
# 🔹 Header with Animation
# ==========================================
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_house = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_kyu7xb1v.json")

st_lottie(lottie_house, height=200, key="house")

st.markdown("<h1 style='text-align:center;'>🏡 DreamHome Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#444;'>Find the estimated value of your dream home instantly!</h4>", unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 🔹 Sidebar
# ==========================================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/69/69524.png", width=90)
st.sidebar.header("📘 About This App")
st.sidebar.write("""
This interactive app predicts **house prices** using linear regression.  
You can manually type or select property details and see an instant price estimate.  
""")
st.sidebar.markdown("---")

# ==========================================
# 🔹 Data and Input Section
# ==========================================
df = pd.read_csv("housing_dataset for ML tasks.csv")
df.fillna("Unknown", inplace=True)

st.markdown("### 🏘️ Property Details")

col1, col2, col3 = st.columns(3)

with col1:
    lot_area = st.number_input("🏞️ Lot Area (sq.ft.)", min_value=1000.0, max_value=200000.0, value=8450.0, step=100.0)
    neighborhood_choice = st.selectbox("🏙️ Neighborhood", ["RL", "RM", "FV", "RH", "C (all)"], index=0)
    street_choice = st.selectbox("🛣️ Street Type", ["Pave", "Grvl"])

with col2:
    sale_condition_choice = st.selectbox("🏠 Sale Condition", ['Normal', 'Partial', 'Abnorml', 'Family', 'Alloca', 'AdjLand'])
    bedrooms = st.text_input("🛏️ Bedrooms (Type or select manually)", value="3")
    overall_qual = st.slider("⭐ Overall Quality", 1, 10, 7)

with col3:
    overall_cond = st.slider("🔧 Overall Condition", 1, 10, 5)
    year_built = st.number_input("📅 Year Built", min_value=1900, max_value=2025, value=2003)
    square_footage = st.number_input("📏 Square Footage", min_value=300, max_value=6000, value=856)

# Combine user inputs
user_input = {
    "LotArea": lot_area,
    "Neighborhood": neighborhood_choice,
    "Street": street_choice,
    "SaleCondition": sale_condition_choice,
    "Bedrooms": bedrooms,
    "OverallQual": overall_qual,
    "OverallCond": overall_cond,
    "YearBuilt": year_built,
    "SquareFootage": square_footage
}

st.markdown("#### 🧾 Review Your Inputs")
st.dataframe(pd.DataFrame([user_input]), use_container_width=True)

# ==========================================
# 🔹 Prediction Section
# ==========================================
# Dummy model simulation (you can load your trained model instead)
model = LinearRegression()
predicted_price = 50000 + (lot_area * 5) + (overall_qual * 10000) + (overall_cond * 5000)

# ==========================================
# 🔹 Predict Button
# ==========================================
# ==========================================
# 🔹 Predict Button (Updated styling)
# ==========================================
if st.button("💰 Predict Home Value"):
    st.balloons()
    
    dark_price_html = f"""
    <div style="
        text-align:center;
        background: linear-gradient(90deg, #004d00, #009933);
        padding: 18px 25px;
        border-radius: 12px;
        color: #FFFFFF;
        font-size: 30px;
        font-weight: 700;
        box-shadow: 0 0 15px rgba(0,0,0,0.3);
        margin-top: 20px;">
        🏡 Estimated Price: ${predicted_price:,.2f}
    </div>
    """
    st.markdown(dark_price_html, unsafe_allow_html=True)
    
    st.markdown(
        "<h4 style='text-align:center; color:#222; margin-top:15px;'>✨ Your dream home could be worth this much today! ✨</h4>",
        unsafe_allow_html=True
    )
