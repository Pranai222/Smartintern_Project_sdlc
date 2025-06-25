# kpi_forecasting component code (placeholder)
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def forecast_kpi(df: pd.DataFrame, target_column: str, steps_ahead: int = 1):
    df = df.reset_index(drop=True)
    df["Time"] = range(len(df))
    
    X = df[["Time"]]
    y = df[target_column]

    model = LinearRegression()
    model.fit(X, y)

    future_time = [[len(df) + i] for i in range(steps_ahead)]
    predictions = model.predict(future_time)

    forecast_df = pd.DataFrame({
        "Time": [len(df) + i for i in range(steps_ahead)],
        "Forecast": predictions
    })

    return forecast_df, model


def kpi_forecasting_ui():
    st.subheader("📈 KPI Forecasting")

    uploaded_file = st.file_uploader("Upload KPI CSV (with time-series values)", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("📊 Data Preview:", df.head())

        column = st.selectbox("Select KPI Column to Forecast", df.columns)

        steps = st.slider("How many future steps to predict?", min_value=1, max_value=12, value=3)

        if st.button("Forecast"):
            forecast_df, model = forecast_kpi(df, column, steps)

            st.write("📈 Forecasted Values")
            st.dataframe(forecast_df)

            # Plot
            fig, ax = plt.subplots()
            ax.plot(df["Time"] if "Time" in df.columns else range(len(df)), df[column], label="Actual")
            ax.plot(forecast_df["Time"], forecast_df["Forecast"], label="Forecast", linestyle="--")
            ax.set_xlabel("Time")
            ax.set_ylabel(column)
            ax.set_title(f"{column} Forecast")
            ax.legend()
            st.pyplot(fig)
