# eco_tips component code (placeholder)
import streamlit as st
from utils.ibm_granite import ask_granite

def eco_tips_ui():
    st.subheader("🌿 Eco Tips Generator")

    topic = st.text_input("Enter an environmental topic (e.g., plastic, solar energy):", key="eco_topic")

    if st.button("Generate Tip"):
        if topic.strip() == "":
            st.warning("Please enter a topic.")
        else:
            with st.spinner("Generating tip..."):
                prompt = f"Give me a practical eco-friendly tip related to: {topic}"
                response = ask_granite(prompt)
                st.success("Eco Tip:")
                st.markdown(f"> {response}")
