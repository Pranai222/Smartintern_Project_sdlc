# feedback_form component code (placeholder)
import streamlit as st
import datetime

def feedback_form_ui():
    st.subheader("📢 Citizen Feedback Form")

    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        category = st.selectbox("Category", ["Water", "Electricity", "Pollution", "Roads", "Waste", "Other"])
        description = st.text_area("Describe the issue or suggestion")
        date = st.date_input("Date of Observation", value=datetime.date.today())
        submitted = st.form_submit_button("Submit")

        if submitted:
            if not name or not description:
                st.warning("Please complete all required fields.")
            else:
                st.success("✅ Feedback submitted successfully!")
                st.markdown("---")
                st.markdown("### 📄 Submitted Details")
                st.markdown(f"**Name:** {name}")
                st.markdown(f"**Category:** {category}")
                st.markdown(f"**Date:** {date}")
                st.markdown(f"**Description:** {description}")
