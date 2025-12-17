import streamlit as st
import plotly.express as px
from utils import load_css, load_dataset, navigation

st.set_page_config(page_title="Utilization", page_icon="🏥", layout="wide")
load_css()
navigation()
df = load_dataset()

st.title("🏥 UTILIZATION ANALYTICS")
st.markdown("### *Healthcare Consumption Patterns*")
st.markdown("---")

# Filters
region = st.selectbox("Filter by Region", ['All'] + list(df['region'].unique()))
dff = df if region == 'All' else df[df['region'] == region]

col1, col2 = st.columns(2)

with col1:
    st.subheader("📡 Procedure Frequency")
    # Check for procedure columns
    proc_cols = [c for c in df.columns if 'proc_' in c]
    if proc_cols:
        proc_data = dff[proc_cols].mean().reset_index()
        proc_data.columns = ['Procedure', 'Avg Count']
        fig = px.bar(proc_data, x='Avg Count', y='Procedure', orientation='h', color='Avg Count', color_continuous_scale='Bluered')
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': 'white'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No procedure data found in CSV.")

with col2:
    st.subheader("💊 Visits vs. Medication")
    fig2 = px.density_heatmap(
        dff, x="visits_last_year", y="medication_count",
        color_continuous_scale="Viridis",
        title="Heatmap: Doctor Visits vs Meds"
    )
    fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': 'white'})
    st.plotly_chart(fig2, use_container_width=True)