# anomaly_checker component code (placeholder)
import streamlit as st
import pandas as pd


def detect_anomalies(df: pd.DataFrame, column_name: str, threshold: float = 2.0):
    """Detects anomalies using z-score."""
    df["z_score"] = (df[column_name] - df[column_name].mean()) / df[column_name].std()
    df["anomaly"] = df["z_score"].abs() > threshold
    return df


def anomaly_checker_ui():
    st.subheader("🔍 Anomaly Detection")

    uploaded_file = st.file_uploader("Upload KPI CSV (e.g., energy or water usage)", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("📊 Uploaded Data Preview:", df.head())

        column_name = st.selectbox("Select column to check for anomalies:", df.columns)

        if st.button("Detect Anomalies"):
            result_df = detect_anomalies(df, column_name)

            st.write("✅ Anomaly Detection Completed")
            st.dataframe(result_df.style.applymap(
                lambda val: 'background-color: red' if isinstance(val, bool) and val else ''
            , subset=["anomaly"]))

            st.success(f"{result_df['anomaly'].sum()} anomalies found.")
