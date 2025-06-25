# policy_summarizer component code (placeholder)
import streamlit as st
from utils.ibm_granite import ask_granite


def summarize_text(text):
    prompt = f"Summarize the following city policy document in simple and clear language:\n\n{text}"
    return ask_granite(prompt)


def policy_summarizer_ui():
    st.subheader("📄 Policy Summarization")

    uploaded_file = st.file_uploader("Upload a policy document (.txt or .csv)", type=["txt", "csv"])

    if uploaded_file:
        if uploaded_file.name.endswith(".txt"):
            content = uploaded_file.read().decode("utf-8")
        elif uploaded_file.name.endswith(".csv"):
            import pandas as pd
            df = pd.read_csv(uploaded_file)
            content = df.to_string()
        else:
            st.error("Unsupported file type.")
            return

        st.text_area("📘 Document Content", value=content, height=200)

        if st.button("Summarize"):
            with st.spinner("Summarizing..."):
                summary = summarize_text(content)
                st.success("✅ Summary Generated")
                st.markdown(f"> {summary}")
