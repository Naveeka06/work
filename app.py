import streamlit as st

st.set_page_config(
    page_title="Startup Analytics Dashboard",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Startup Analytics Dashboard")

st.markdown("""
### Welcome

Use the sidebar to navigate:

- 📊 Overview
- 💰 Funding Analytics
- 🏭 Industry Insights
- 🌍 Regional Analysis
- 🤖 AI Insights

Built with Streamlit + Plotly.
""")
