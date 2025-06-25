import streamlit as st
import pandas as pd

def summary_card(title, value, unit, color):
    st.markdown(f"""
        <div style="
            background-color:{color};
            padding:20px;
            border-radius:10px;
            text-align:center;
            color:white;
            margin-bottom:15px;">
            <h4>{title}</h4>
            <h2>{value} {unit}</h2>
        </div>
    """, unsafe_allow_html=True)

def smart_dashboard_ui():
    st.subheader("📊 City Health Dashboard")

    uploaded_file = st.file_uploader("Upload KPI Data (.csv)", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Data Loaded")
        st.dataframe(df.head())

        # Try to grab the latest entry (last row)
        latest_data = df.iloc[-1]

        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

        if not numeric_cols.any():
            st.warning("⚠️ No numeric columns found in uploaded file.")
            return

        st.markdown("### 🧾 KPI Summary Cards")
        col1, col2 = st.columns(2)

        with col1:
            for col in numeric_cols[::2]:  # Every other KPI
                summary_card(col, latest_data[col], "", "#4CAF50")

        with col2:
            for col in numeric_cols[1::2]:
                summary_card(col, latest_data[col], "", "#2196F3")
