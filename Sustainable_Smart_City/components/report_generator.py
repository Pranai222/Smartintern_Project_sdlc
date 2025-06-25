# 📁 File: components/report_generator.py

import streamlit as st
from utils.ibm_granite import ask_granite

# ✅ Helper: Generate prompt and get AI-written report
def generate_city_report(city_name: str, kpi_dict: dict) -> str:
    kpi_lines = '\n'.join([f'- {k}: {v}' for k, v in kpi_dict.items()])
    prompt = f"""
Generate a sustainability report for the city of {city_name}.
Include analysis and recommendations based on the following KPIs:

{kpi_lines}

The report should be concise, informative, and easy for both citizens and city officials to understand.
"""
    return ask_granite(prompt)

# ✅ UI Component for Report Generator
def report_generator_ui():
    st.subheader("📝 Sustainability Report Generator")

    city_name = st.text_input("City Name", value="Smartville")

    st.markdown("### 📊 Enter KPI Values:")
    kpis = {
        "Water Usage (litres/day)": st.number_input("Water Usage", min_value=0.0, value=10000.0),
        "Electricity Consumption (kWh/day)": st.number_input("Electricity Consumption", min_value=0.0, value=5000.0),
        "Air Quality Index (AQI)": st.number_input("Air Quality Index", min_value=0.0, value=80.0),
        "Carbon Emissions (tons/year)": st.number_input("Carbon Emissions", min_value=0.0, value=1500.0)
    }

    if st.button("Generate Report"):
        with st.spinner("Generating AI-powered report..."):
            report = generate_city_report(city_name, kpis)
            st.success("✅ Report Ready")
            st.markdown("### 📄 AI-Generated Sustainability Report")
            st.markdown(report)
