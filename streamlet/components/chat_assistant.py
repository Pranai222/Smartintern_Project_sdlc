import streamlit as st
import requests
import os
import tempfile
from utils.ibm_granite import ask_granite_with_context

ALLOWED_EXTENSIONS = {"pdf", "docx", "txt"}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text(file_path):
    try:
        import textract
        return textract.process(file_path).decode("utf-8")
    except Exception as e:
        return f"[Error extracting text: {e}]"

def chat_assistant_ui():
    st.subheader("💬 AI Assistant + Document Chat")

    # Chat state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # File Upload
    uploaded_files = st.file_uploader("Upload supporting documents (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"], accept_multiple_files=True)

    # User Prompt
    user_input = st.text_input("Ask your question here...")

    if st.button("Ask") and user_input.strip() != "":
        # Gather context from files
        context = ""
        if uploaded_files:
            for file in uploaded_files:
                if file and allowed_file(file.name):
                    with tempfile.NamedTemporaryFile(delete=False) as tmp:
                        tmp.write(file.read())
                        tmp_path = tmp.name
                    file_text = extract_text(tmp_path)
                    context += f"\n--- File: {file.name} ---\n{file_text}\n"
                    os.unlink(tmp_path)

        # Send to WatsonX (using correct arguments)
        with st.spinner("Asking IBM Granite..."):
            try:
                response = ask_granite_with_context(user_input, context)
            except Exception as e:
                response = f"❌ Error: {e}"

        # Save chat history
        st.session_state.chat_history.append(("🧑 You", user_input))
        st.session_state.chat_history.append(("🤖 Assistant", response))

    # Display chat history
    for sender, message in st.session_state.chat_history:
        st.markdown(f"**{sender}:** {message}")
