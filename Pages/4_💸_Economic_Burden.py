import streamlit as st
import plotly.express as px
from utils import load_css, load_dataset, navigation

st.set_page_config(page_title="Economics", page_icon="💸", layout="wide")
load_css()
navigation()
df = load_dataset()

st.title("💸 ECONOMIC BURDEN")
st.markdown("### *Affordability & Premium Stress*")

# Logic
df['burden_percent'] = (df['annual_medical_cost'] / df['income']) * 100
avg_burden = df['burden_percent'].mean()

c1, c2 = st.columns(2)
c1.metric("Avg Burden", f"{avg_burden:.1f}%", "of Annual Income")
c2.metric("Median Income", f"${df['income'].median():,.0f}")

st.markdown("---")
st.subheader("📉 The Affordability Gap")
st.caption("Patients above the dashed line spend >10% of income on health.")

fig = px.scatter(
    df.sample(2000), x="income", y="burden_percent", 
    color="risk_category",
    color_discrete_map={'High': '#FF0055', 'Medium': '#FFD700', 'Low': '#00FFaa'},
    log_x=True
)
fig.add_hline(y=10, line_dash="dash", line_color="white")
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)', font={'color': 'white'},
    xaxis_title="Income (Log Scale)", yaxis_title="% Income Spent on Health"
)
st.plotly_chart(fig, use_container_width=True)