import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("startup_data.csv")

st.title("🤖 AI Generated Business Insights")

highest_funded = (
    df.groupby("Industry")
    ["Funding Amount (M USD)"]
    .sum()
    .idxmax()
)

highest_valuation = (
    df.groupby("Industry")
    ["Valuation (M USD)"]
    .mean()
    .idxmax()
)

highest_revenue = (
    df.groupby("Industry")
    ["Revenue (M USD)"]
    .mean()
    .idxmax()
)

best_region = (
    df.groupby("Region")
    ["Funding Amount (M USD)"]
    .sum()
    .idxmax()
)

corr_funding_valuation = (
    df[
        [
            "Funding Amount (M USD)",
            "Valuation (M USD)"
        ]
    ]
    .corr()
    .iloc[0,1]
)

corr_employee_revenue = (
    df[
        [
            "Employees",
            "Revenue (M USD)"
        ]
    ]
    .corr()
    .iloc[0,1]
)

st.success(
f"""

{highest_funded}


{highest_valuation}


{highest_revenue}


{best_region}


{corr_funding_valuation:.2f}


{corr_employee_revenue:.2f}
"""
)

st.subheader("Key Recommendations")

recommendations = [
    f"Invest more in {highest_funded}",
    f"Explore opportunities in {best_region}",
    f"Focus on industries with high valuation like {highest_valuation}",
    "Increase workforce efficiency",
    "Monitor startups with strong revenue but low funding"
]

for rec in recommendations:
    st.write("✅", rec)
