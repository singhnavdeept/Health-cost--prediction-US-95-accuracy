

# 🏥 Health Insurance Cost Prediction using Predictive Analytics

An end-to-end predictive analytics project that estimates healthcare insurance costs using machine learning models, developed through **Jupyter Notebook–based experimentation** and presented via an **interactive Streamlit application**.

---

## 📌 Project Overview

Healthcare insurance cost estimation is a complex problem influenced by demographic attributes, lifestyle factors, and healthcare utilization patterns. This project applies **predictive analytics and supervised machine learning techniques** to model and predict insurance charges, while emphasizing **data preprocessing, exploratory analysis, model comparison, and interpretability**.

The project follows an **industry-aligned workflow**, beginning with exploratory experimentation in Jupyter Notebook and culminating in an interactive Streamlit-based interface for demonstration and decision support.

---

## 🎯 Objectives

* To analyze healthcare-related data and identify key cost drivers
* To preprocess and transform raw data into a machine-learning-ready format
* To develop and compare multiple regression-based predictive models
* To evaluate models using standard performance metrics
* To demonstrate the complete analytics pipeline through an interactive UI

---

## 🧠 Learning Outcomes

Through this project, the following key learnings were achieved:

* Practical understanding of **predictive analytics lifecycle**
* Hands-on experience with **Jupyter Notebook for iterative analysis**
* Comparative evaluation of **linear vs ensemble-based models**
* Importance of **data preprocessing and feature interactions**
* Transition from **analytical notebooks to deployable applications**
* Interpretation of regression metrics such as **R², RMSE, and MAE**

---

## 📊 Dataset & Data Collection

* **Data Source:** Healthcare.gov Developer API
* **Format:** JSON (transformed to tabular format)
* **Collection Method:** RESTful API calls using Python
* **Attributes:** Demographic and healthcare-related variables
* **Target Variable:** Insurance charges (continuous)

API-based data acquisition was used to simulate real-world data pipelines and ensure reproducibility.

---

## 🔍 Exploratory Data Analysis (EDA)

EDA was conducted in Jupyter Notebook to understand:

* Distribution of insurance charges
* Impact of age, BMI, and smoking status
* Feature interactions and non-linear patterns
* Relative influence of demographic vs utilization factors

Insights from EDA directly informed model selection and evaluation strategy.

---

## 🤖 Models Implemented

The following supervised regression models were developed and evaluated using a unified preprocessing pipeline:

* **Linear Regression**

  * Baseline model for interpretability and comparison

* **Random Forest Regressor**

  * Ensemble model capturing non-linear relationships and feature interactions

* **Gradient Boosting Regressor**

  * Sequential ensemble model optimized for reducing prediction error

---

## 📈 Model Evaluation Metrics

Models were evaluated using standard regression metrics:

* **R² Score** – Variance explained by the model
* **RMSE** – Root Mean Squared Error
* **MAE** – Mean Absolute Error

Ensemble-based models consistently outperformed the linear baseline, particularly for high-cost and high-risk cases.

---

## 🧪 Development Environment

* **Jupyter Notebook** – Core environment for:

  * Data preprocessing
  * EDA
  * Model training
  * Comparative analysis

* **Streamlit** – Used to:

  * Showcase the entire project
  * Enable real-time model selection
  * Demonstrate predictions interactively

---

## 🖥️ Streamlit Application

The Streamlit UI represents the deployment-oriented extension of the notebook workflow. It allows:

* Dynamic selection of trained models
* Real-time user input
* Immediate prediction of insurance costs
* Visualization of model behavior

🔗 **Live Demonstration & Project Artifacts:**
[https://drive.google.com/drive/folders/1F7TbcC1OfNRrmFO4qVkZ5C_Qd9-oaiPs?usp=sharing](https://drive.google.com/drive/folders/1F7TbcC1OfNRrmFO4qVkZ5C_Qd9-oaiPs?usp=sharing)

---

## 📁 Repository Structure (Indicative)

```
├── notebooks/
│   └── health_cost_prediction.ipynb
├── app/
│   └── streamlit_app.py
├── models/
│   └── trained_models.pkl
├── data/
│   └── processed_data.csv
├── report/
│   └── INT234_Project_Report.docx
└── README.md
```

---

## 🚀 How to Run (Local)

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

---

## 🔮 Future Enhancements

* Integration of real-time and longitudinal healthcare data
* Explainable AI using SHAP/LIME
* Deployment as a REST API
* Fairness and bias evaluation
* Advanced hyperparameter optimization

---

## 👤 Author

**Navdeep Singh**
B.Tech Computer Science & Engineering
Lovely Professional University

* 🔗 GitHub: [https://github.com/singhnavdeept](https://github.com/singhnavdeept)
* 🔗 LinkedIn: [https://www.linkedin.com/in/navdeepsinghjour](https://www.linkedin.com/in/navdeepsinghjour)

---

## 📜 License

This project is developed for **academic and educational purposes** as part of the **INT234 – Predictive Analytics** course.

---

### 🧠 Final Note

This README is intentionally written to reflect **ownership, understanding, and learning**, not just implementation. It complements your report, notebook, and Streamlit UI as a complete academic portfolio.

If you want, I can:

* Shorten this for recruiters
* Rewrite it in a more **research-paper tone**
* Add badges / visuals for GitHub
* Align it with **viva explanations**


