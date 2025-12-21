import streamlit as st
import plotly.express as px
from utils import load_css, load_dataset, navigation

st.set_page_config(page_title="Risk Stratification", page_icon="⚠️", layout="wide")
load_css()
navigation()
df = load_dataset()

st.title("⚠️ RISK STRATIFICATION")
st.markdown("### *Population Segmentation Analysis*")
st.markdown("---")

# Metrics
c1, c2, c3 = st.columns(3)
high_risk = df[df['risk_category'] == 'High']
med_risk = df[df['risk_category'] == 'Medium']

c1.metric("High Risk Patients", f"{len(high_risk):,}", f"{len(high_risk)/len(df):.1%} of Total")
c2.metric("Avg Cost (High Risk)", f"${high_risk['annual_medical_cost'].mean():,.0f}")
c3.metric("Avg Cost (Low Risk)", f"${df[df['risk_category']=='Low']['annual_medical_cost'].mean():,.0f}")

st.markdown("---")

c1, c2 = st.columns([1.5, 1])

with c1:
    st.subheader("🧬 Risk vs. Cost Distribution")
    # Interactive Scatter
    fig = px.scatter(
        df.sample(2000), x="age", y="annual_medical_cost", 
        color="risk_category", size="bmi",
        color_discrete_map={'High': '#FF0055', 'Medium': '#FFD700', 'Low': '#00FFaa'},
        title="Cost Drivers: Age, BMI (Size), and Risk Level"
    )
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': 'white'})
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("📊 Segmentation Volume")
    fig2 = px.pie(
        df, names='risk_category', values='annual_medical_cost',
        color='risk_category',
        color_discrete_map={'High': '#FF0055', 'Medium': '#FFD700', 'Low': '#00FFaa'},
        hole=0.4
    )
    fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': 'white'})
    st.plotly_chart(fig2, use_container_width=True)