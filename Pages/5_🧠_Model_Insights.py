import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_css, navigation, get_live_model

st.set_page_config(page_title="AI Insights", page_icon="🧠", layout="wide")
load_css()
navigation()

st.title("🧠 INTELLIGENCE CORE")
st.markdown("### *Algorithm Transparency & Forensics*")
st.markdown("Select any of the **11 Models** below to deconstruct its decision-making process.")
st.markdown("---")

# 1. GET THE LIVE MODEL (Updated with ALL 11 Options)
model_type = st.selectbox(
    "Select Model to Inspect", 
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

# Train the model on the fly to get insights
model, feature_names = get_live_model(model_type)

if model:
    c1, c2 = st.columns([2, 1])
    
    with c1:
        st.subheader(f"⚡ {model_type} Drivers")
        
        # A. TREE-BASED MODELS (Feature Importance)
        if hasattr(model, 'feature_importances_'):
            imp = model.feature_importances_
            df_imp = pd.DataFrame({'Feature': feature_names, 'Importance': imp}).sort_values('Importance', ascending=True)
            
            fig = px.bar(
                df_imp, x='Importance', y='Feature', orientation='h',
                color='Importance', color_continuous_scale='Tealgrn',
                title=f"What matters most to {model_type}?"
            )
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': 'white'})
            st.plotly_chart(fig, use_container_width=True)
            
        # B. LINEAR MODELS (Coefficients)
        elif hasattr(model, 'coef_'):
            imp = model.coef_
            df_imp = pd.DataFrame({'Feature': feature_names, 'Coefficient': imp}).sort_values('Coefficient', ascending=True)
            
            fig = px.bar(
                df_imp, x='Coefficient', y='Feature', orientation='h',
                color='Coefficient', color_continuous_scale='Balance',
                title=f"Weight Impact (Positive vs Negative)"
            )
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': 'white'})
            st.plotly_chart(fig, use_container_width=True)
            
        # C. BLACK BOX MODELS (KNN, SVR)
        else:
            st.warning(f"⚠️ **Black Box Algorithm Detected**")
            st.markdown(f"""
            The **{model_type}** algorithm calculates predictions using distance metrics in high-dimensional space (e.g., Euclidean distance or RBF Kernels) rather than explicit weights or splits.
            
            It does not offer a simple "Feature Importance" chart because every data point influences every other data point dynamically.
            """)
            
            st.info("💡 **Tip:** To see clear drivers, switch to 'Random Forest' or 'Linear Regression'.")

    with c2:
        st.subheader("📝 Technical Specs")
        st.markdown(f"""
        <div style="background-color: #111; padding: 20px; border-radius: 10px; border: 1px solid #333;">
            <p><b>Algorithm:</b> <span style="color: #00F0FF">{model_type}</span></p>
            <p><b>Input Features:</b> {len(feature_names)}</p>
            <p><b>Training Data:</b> Live Sample (10k rows)</p>
            <p><b>Library:</b> Scikit-Learn</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 💡 Analyst Note")
        if "Linear" in model_type or "Ridge" in model_type:
            st.caption("Linear models show **Direction**: Positive bars increase cost, Negative bars decrease cost.")
        elif "Tree" in model_type or "Forest" in model_type or "Boost" in model_type:
            st.caption("Tree models show **Importance**: Which variable was split the most often? (Direction is not shown).")

else:
    st.error("Engine Offline. Check medical_insurance.csv.")