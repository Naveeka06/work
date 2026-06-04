import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("startup_data.csv")

st.title("🏭 Industry Insights")

industry_stats = (
    df.groupby("Industry")
    .agg({
        "Revenue (M USD)": "mean",
        "Valuation (M USD)": "mean",
        "Funding Amount (M USD)": "mean",
        "Employees": "mean"
    })
    .reset_index()
)

st.dataframe(industry_stats)

fig = px.bar(
    industry_stats,
    x="Industry",
    y="Revenue (M USD)",
    title="Average Revenue by Industry"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.bar(
    industry_stats,
    x="Industry",
    y="Valuation (M USD)",
    title="Average Valuation by Industry"
)

st.plotly_chart(fig2, use_container_width=True)

market_share = (
    df.groupby("Industry")
    ["Market Share (%)"]
    .mean()
    .reset_index()
)

fig3 = px.treemap(
    market_share,
    path=["Industry"],
    values="Market Share (%)",
    title="Industry Market Share"
)

st.plotly_chart(fig3, use_container_width=True)
