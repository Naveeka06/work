import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("startup_data.csv")

st.title("💰 Funding Analytics")

industry = st.selectbox(
    "Filter Industry",
    ["All"] + list(df["Industry"].unique())
)

if industry != "All":
    df = df[df["Industry"] == industry]

fig = px.scatter(
    df,
    x="Funding Amount (M USD)",
    y="Valuation (M USD)",
    color="Industry",
    size="Revenue (M USD)",
    hover_name="Startup Name",
    title="Funding vs Valuation"
)

st.plotly_chart(fig, use_container_width=True)

funding_by_industry = (
    df.groupby("Industry")["Funding Amount (M USD)"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    funding_by_industry,
    x="Industry",
    y="Funding Amount (M USD)",
    title="Funding by Industry"
)

st.plotly_chart(fig2, use_container_width=True)

funding_by_region = (
    df.groupby("Region")["Funding Amount (M USD)"]
    .sum()
    .reset_index()
)

fig3 = px.pie(
    funding_by_region,
    names="Region",
    values="Funding Amount (M USD)",
    title="Funding Share by Region"
)

st.plotly_chart(fig3, use_container_width=True)
