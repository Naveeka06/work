import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("startup_data.csv")

st.title("📊 Startup Overview Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Startups", len(df))
col2.metric("Total Funding ($M)",
            f"{df['Funding Amount (M USD)'].sum():,.2f}")

col3.metric("Average Valuation ($M)",
            f"{df['Valuation (M USD)'].mean():,.2f}")

col4.metric("Average Revenue ($M)",
            f"{df['Revenue (M USD)'].mean():,.2f}")

st.divider()

col1, col2 = st.columns(2)

with col1:
    fig = px.histogram(
        df,
        x="Funding Amount (M USD)",
        title="Funding Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.histogram(
        df,
        x="Valuation (M USD)",
        title="Valuation Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Top 10 Startups by Valuation")

top10 = df.sort_values(
    by="Valuation (M USD)",
    ascending=False
).head(10)


