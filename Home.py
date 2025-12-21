import streamlit as st
from utils import load_css, navigation 

st.set_page_config(page_title="Health Nexus", page_icon="🧬", layout="wide")
load_css()
navigation() # <--- Now this will work because we imported it above

# --- MAIN CONTENT ---
st.markdown("<br><br>", unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    # 🧬 HEALTH <span style='color: #00F0FF'>NEXUS</span>
    ### *Advanced Medical Cost Intelligence System*
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **System Architecture:**
    This platform transforms raw medical data into actionable financial intelligence.
    
    * **Page 1:** AI-driven individual cost simulation.
    * **Page 2:** Population-level risk stratification.
    * **Page 3:** Utilization & procedural analytics.
    * **Page 4:** Economic burden & affordability modeling.
    * **Page 5:** Black-box model explainability.
    """)
    
    # We use st.container to group the button so it aligns well
    with st.container():
        if st.button("🚀 LAUNCH SYSTEM MAIN"):
            st.switch_page("pages/1_🔮_Individual_Prediction.py")

with col2:
    # A placeholder image for the cinematic feel
    st.markdown("""
    <div style="border: 2px solid #00F0FF; padding: 10px; border-radius: 10px; background-color: #000;">
        <h3 style="text-align: center; margin: 0;">SYSTEM ONLINE</h3>
        <p style="text-align: center; color: #00FFaa;">All Modules Active</p>
    </div>
    """, unsafe_allow_html=True)