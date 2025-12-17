import streamlit as st
import plotly.graph_objects as go
from utils import load_css, navigation, get_live_model, predict_live

st.set_page_config(page_title="Prediction", page_icon="🔮", layout="wide")
load_css()
navigation()

# --- HEADER ---
st.title("🔮 INDIVIDUAL FORECAST")
st.markdown("### *Multi-Algorithm Intelligence*")
st.markdown("Select from **11 different AI models**. The system will train your selection on the live dataset instantly.")
st.markdown("---")

# --- CONTROL DECK ---
st.markdown("#### 🛠️ CONFIGURATION PANEL")

with st.container():
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("**👤 SUBJECT PROFILE**")
        age = st.slider("Current Age", 18, 90, 45)
        sex = st.selectbox("Biological Sex", ["Male", "Female"])
        region = st.selectbox("Region", ["North", "South", "East", "West"])

    with c2:
        st.markdown("**⚖️ BIOMETRICS**")
        bmi = st.slider("BMI Score", 15.0, 50.0, 28.5)
        smoker = st.toggle("Active Smoker", value=False)
        dependents = st.number_input("Dependents / Children", 0, 5, 0)

    with c3:
        st.markdown("**🧠 INTELLIGENCE CORE**")
        # THE FULL 11-MODEL LIST
        model_choice = st.selectbox(
            "Select Algorithm", 
            [
                "Random Forest", 
                "Gradient Boosting", 
                "AdaBoost", 
                "Extra Trees", 
                "Decision Tree",
                "Linear Regression", 
                "Ridge Regression", 
                "Lasso Regression", 
                "ElasticNet",
                "K-Nearest Neighbors",
                "Support Vector Machine (SVR)"
            ]
        )
        
        # Train on demand
        model, features = get_live_model(model_choice)
        
        if model:
            st.success(f"✅ {model_choice} Online")
        else:
            st.error("❌ Engine Offline")

st.markdown("---")

if model:
    # 1. Run Prediction
    inputs = {
        'age': age, 'bmi': bmi, 'sex': sex, 
        'smoker': smoker, 'region': region, 'dependents': dependents
    }
    cost = predict_live(model, features, inputs)
    
    # 2. Optimization
    opt_inputs = inputs.copy()
    opt_inputs['bmi'] = 22.0
    opt_inputs['smoker'] = False
    opt_cost = predict_live(model, features, opt_inputs)
    
    gap = cost - opt_cost
    
    # --- VISUALS ---
    c_res1, c_res2 = st.columns([1, 1.5])
    
    with c_res1:
        st.markdown("#### 💸 ESTIMATED ANNUAL COST")
        st.markdown(f"""
        <div style="background-color: #111; padding: 20px; border-radius: 10px; border-left: 5px solid #00F0FF; box-shadow: 0 0 20px rgba(0, 240, 255, 0.2);">
            <h1 style='font-size: 56px; color: #00F0FF; margin: 0;'>${cost:,.0f}</h1>
            <p style='margin: 0; color: #888;'>Algorithm: {model_choice}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if gap > 1000:
            st.markdown("<br>", unsafe_allow_html=True)
            st.warning(f"⚠️ **RISK ANALYSIS:**\n\nYour profile suggests a **${gap:,.0f} premium** compared to optimal health.")
        else:
            st.markdown("<br>", unsafe_allow_html=True)
            st.success("✅ **LOW RISK PROFILE:**\n\nTracking with healthy baseline.")

    with c_res2:
        # Gauge Chart
        fig = go.Figure(go.Indicator(
            mode = "gauge+delta", value = cost,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Financial Risk Meter", 'font': {'size': 24, 'color': "white"}},
            delta = {'reference': opt_cost, 'increasing': {'color': "#FF0055"}, 'decreasing': {'color': "#00FFaa"}},
            gauge = {
                'axis': {'range': [0, 65000], 'tickcolor': "white"},
                'bar': {'color': "#00F0FF"},
                'bgcolor': "rgba(0,0,0,0)",
                'borderwidth': 2,
                'bordercolor': "#333",
                'steps': [
                    {'range': [0, 15000], 'color': '#222'},
                    {'range': [15000, 65000], 'color': '#111'}],
                'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 50000}}
        ))
        
        fig.update_layout(
            height=300, 
            margin=dict(t=50, b=20, l=40, r=40), 
            paper_bgcolor='rgba(0,0,0,0)', 
            font={'color': 'white'}
        )
        st.plotly_chart(fig, use_container_width=True)

else:
    st.error("⚠️ Model could not be trained. Check CSV.")