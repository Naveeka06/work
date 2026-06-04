import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("startup_data.csv")

st.title("🌍 Regional Analysis")

region_data = (
    df.groupby("Region")
    .agg({
        "Funding Amount (M USD)": "sum",
        "Valuation (M USD)": "mean",
        "Revenue (M USD)": "mean"
    })
    .reset_index()
)

st.dataframe(region_data)

fig = px.bar(
    region_data,
    x="Region",
    y="Funding Amount (M USD)",
    title="Funding by Region"
)

st.plotly_chart(fig, use_container_width=True)

fig2 = px.bar(
    region_data,
    x="Region",
    y="Valuation (M USD)",
    title="Average Valuation by Region"
)

st.plotly_chart(fig2, use_container_width=True)

fig3 = px.scatter(
    df,
    x="Revenue (M USD)",
    y="Valuation (M USD)",
    color="Region",
    size="Employees",
    hover_name="Startup Name",
    title="Revenue vs Valuation by Region"
)

st.plotly_chart(fig3, use_container_width=True)
