"""Streamlit UI."""

import streamlit as st
import tempfile
from src.agent import SecurityAgent

st.set_page_config(page_title="Security Log Analyzer", page_icon="shield", layout="wide")

st.title("LLM-Powered Security Log Analyzer")
st.caption("LangGraph agent + OpenAI GPT-4 · Self-reflection loop")

uploaded = st.file_uploader("Upload log file", type=["log", "txt"])

if uploaded and st.button("Analyze"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".log") as f:
        f.write(uploaded.read())
        path = f.name

    with st.spinner("Analyzing with LangGraph agent..."):
        agent = SecurityAgent()
        result = agent.analyze(path)

    st.subheader("Summary")
    st.write(result["summary"])

    st.subheader("Findings")
    st.json(result["findings"])

    st.subheader("Reflection")
    st.json(result["reflection"])
