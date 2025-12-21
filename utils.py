import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib

# Try to import sklearn components
try:
    from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor, ExtraTreesRegressor
    from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.neighbors import KNeighborsRegressor
    from sklearn.svm import SVR
    from sklearn.preprocessing import StandardScaler
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

# ==========================================
# 1. CSS
# ==========================================
def load_css():
    st.markdown("""
        <style>
        [data-testid="stSidebar"] { display: none; }
        .stApp { background-color: #000000; color: #E0E0E0; }
        div[data-testid="column"] { overflow: visible !important; }
        h1, h2, h3 { color: #00F0FF; font-family: 'Helvetica Neue', sans-serif; }
        
        /* NEON BUTTONS */
        div.stButton > button {
            width: 100%; height: 45px; background-color: #000; color: #FFF;
            border: 2px solid #333; border-radius: 10px; font-weight: 800;
            overflow: visible !important; position: relative; z-index: 1;
        }
        div.stButton > button:before {
            content: ''; background: var(--btn-glow); position: absolute;
            top: -2px; left: -2px; right: -2px; bottom: -2px;
            z-index: -1; filter: blur(20px); opacity: 0; transition: opacity 0.3s;
            border-radius: 15px;
        }
        div.stButton > button:hover { border-color: var(--btn-glow); box-shadow: 0 0 15px var(--btn-glow); color: #fff; }
        div.stButton > button:hover:before { opacity: 0.8; }
        </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. NAVIGATION (FIXED: No Callbacks)
# ==========================================
def navigation():
    st.markdown("""
    <style>
    div[data-testid="column"]:nth-of-type(1) div.stButton > button { --btn-glow: #BD00FF; }
    div[data-testid="column"]:nth-of-type(2) div.stButton > button { --btn-glow: #00F0FF; }
    div[data-testid="column"]:nth-of-type(3) div.stButton > button { --btn-glow: #FFD700; }
    div[data-testid="column"]:nth-of-type(4) div.stButton > button { --btn-glow: #FF0000; }
    div[data-testid="column"]:nth-of-type(5) div.stButton > button { --btn-glow: #00FF00; }
    div[data-testid="column"]:nth-of-type(6) div.stButton > button { --btn-glow: #FF00C8; }
    </style>
    """, unsafe_allow_html=True)
    c1,c2,c3,c4,c5,c6 = st.columns(6)
    
    # STANDARD IF STATEMENTS (Fixes the no-op error)
    with c1: 
        if st.button("🏠 HOME"): st.switch_page("Home.py")
    with c2: 
        if st.button("🔮 PREDICT"): st.switch_page("pages/1_🔮_Individual_Prediction.py")
    with c3: 
        if st.button("⚠️ RISK"): st.switch_page("pages/2_⚠️_Risk_Stratification.py")
    with c4: 
        if st.button("🏥 USAGE"): st.switch_page("pages/3_🏥_Utilization_Analytics.py")
    with c5: 
        if st.button("💸 ECON"): st.switch_page("pages/4_💸_Economic_Burden.py")
    with c6: 
        if st.button("🧠 AI"): st.switch_page("pages/5_🧠_Model_Insights.py")
    st.markdown("---")

# ==========================================
# 3. LIVE ENGINE (Shared Logic)
# ==========================================
@st.cache_resource
def get_live_model(model_type="Random Forest"):
    if not os.path.exists('medical_insurance.csv'): return None, "CSV Missing"
    df = pd.read_csv('medical_insurance.csv')
    
    # Sampling for speed
    if len(df) > 5000: df = df.sample(5000, random_state=42)
    
    # Clean
    df['income'] = df['income'].fillna(df['income'].median())
    
    dep_col = 'children' if 'children' in df.columns else 'dependents'
    if dep_col not in df.columns: df['dependents'] = 0; dep_col = 'dependents'
    
    features_raw = ['age', 'bmi', 'sex', 'smoker', 'region', dep_col]
    target = 'annual_medical_cost'
    
    df = df[features_raw + [target]].dropna()
    
    # Encoding
    df['sex_code'] = df['sex'].map({'Male': 1, 'Female': 0}).fillna(0)
    df['smoker_code'] = df['smoker'].map({'Current': 2, 'Former': 1, 'Never': 0}).fillna(0)
    regions = ['North', 'South', 'East', 'West']
    for r in regions: df[f'region_{r}'] = (df['region'] == r).astype(int)
        
    feature_cols = ['age', 'bmi', 'sex_code', 'smoker_code', dep_col] + [f'region_{r}' for r in regions]
    X = df[feature_cols]
    y = df[target]
    
    if HAS_SKLEARN:
        if model_type == "Random Forest": model = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42)
        elif model_type == "Gradient Boosting": model = GradientBoostingRegressor(n_estimators=100, max_depth=3, random_state=42)
        elif model_type == "Linear Regression": model = LinearRegression()
        elif model_type == "Decision Tree": model = DecisionTreeRegressor(max_depth=10)
        elif model_type == "Ridge Regression": model = Ridge()
        elif model_type == "Lasso Regression": model = Lasso()
        elif model_type == "K-Nearest Neighbors":
            scaler = StandardScaler(); X = scaler.fit_transform(X)
            model = KNeighborsRegressor(n_neighbors=5); model.custom_scaler = scaler
        elif model_type == "Support Vector Machine (SVR)":
            scaler = StandardScaler(); X = scaler.fit_transform(X)
            model = SVR(); model.custom_scaler = scaler
        else: model = RandomForestRegressor(n_estimators=50)
            
        model.fit(X, y)
        return model, feature_cols
    return None, "No Sklearn"

def predict_live(model, features, inputs):
    input_data = pd.DataFrame(0, index=[0], columns=features)
    input_data['age'] = inputs['age']
    input_data['bmi'] = inputs['bmi']
    input_data[features[4]] = inputs.get('dependents', 0)
    input_data['sex_code'] = 1 if inputs['sex'] == 'Male' else 0
    input_data['smoker_code'] = 2 if inputs['smoker'] else 0
    reg = inputs.get('region', 'North')
    if f'region_{reg}' in input_data.columns: input_data[f'region_{reg}'] = 1
        
    if hasattr(model, 'custom_scaler'): return model.predict(model.custom_scaler.transform(input_data))[0]
    return model.predict(input_data)[0]

@st.cache_data
def load_dataset():
    if os.path.exists('medical_insurance.csv'):
        df = pd.read_csv('medical_insurance.csv')
        if 'income' not in df.columns: df['income'] = 50000
    else:
        # Dummy
        df = pd.DataFrame({'age': [30], 'annual_medical_cost': [5000]})
    
    # Feature Engineering for Dashboard Analysis
    if 'risk_score' not in df.columns:
        df['risk_score'] = (df['age'] * 0.4) + (df['bmi'] * 0.6)
    if 'risk_category' not in df.columns:
        try: df['risk_category'] = pd.qcut(df['risk_score'], q=[0, .33, .66, 1], labels=['Low', 'Medium', 'High'])
        except: df['risk_category'] = 'Medium'
    return df