# Streamlit main app controller (placeholder)
# 📁 File: app.py

import streamlit as st
from streamlit_option_menu import option_menu

# Import UI components
from components.smart_dashboard import smart_dashboard_ui
from components.feedback_form import feedback_form_ui
from components.chat_assistant import chat_assistant_ui
from components.eco_tips import eco_tips_ui
from components.kpi_forecasting import kpi_forecasting_ui
from components.anomaly_checker import anomaly_checker_ui
from components.policy_summarizer import policy_summarizer_ui
from components.report_generator import report_generator_ui

# App configuration
st.set_page_config(page_title="Sustainable Smart City Assistant", layout="wide")

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        "🌍 Smart City Assistant",
        ["Dashboard", "Feedback", "Chat", "Eco Tips", "Forecasting", "Anomaly Detection", "Policy Summarizer", "Report Generator"],
        icons=["bar-chart", "envelope", "chat-dots", "leaf", "graph-up", "search", "file-earmark-text", "journal-text"],
        menu_icon="building", default_index=0
    )

# Page routing
if selected == "Dashboard":
    smart_dashboard_ui()
elif selected == "Feedback":
    feedback_form_ui()
elif selected == "Chat":
    chat_assistant_ui()
elif selected == "Eco Tips":
    eco_tips_ui()
elif selected == "Forecasting":
    kpi_forecasting_ui()
elif selected == "Anomaly Detection":
    anomaly_checker_ui()
elif selected == "Policy Summarizer":
    policy_summarizer_ui()
elif selected == "Report Generator":
    report_generator_ui()
