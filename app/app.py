import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------------------------
# CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Urban Mining Economics",
    layout="wide"
)

# ----------------------------------
# TITLE
# ----------------------------------

st.title("♻️ Urban Mining Economics in Argentina")

st.subheader(
    "A Data Analytics Approach to Urban Copper Recovery"
)

st.markdown("""
### Research Question

Can urban copper recovery become a profitable economic activity through data-driven decision making?
""")

# ----------------------------------
# LOAD DATA
# ----------------------------------

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(
    BASE_DIR / "data" / "raw" / "urban_mining_field_data.csv"
)
# ----------------------------------
# CALCULATIONS
# ----------------------------------

precio_cobre = 15500
factor_recuperacion = 0.85

df["Cobre_Semanal_kg"] = (
    df["Cantidad_Semanal"]
    * df["Cobre_kg_por_unidad"]
)

df["Cobre_Mensual_kg"] = (
    df["Cobre_Semanal_kg"]
    * 4
)

df["Cobre_Real_Mensual_kg"] = (
    df["Cobre_Mensual_kg"]
    * factor_recuperacion
)

df["Ingreso_Real_Mensual_ARS"] = (
    df["Cobre_Real_Mensual_kg"]
    * precio_cobre
)

df["Costo_Mensual_ARS"] = (
    df["Cantidad_Semanal"]
    * 4
    * df["Precio_Compra_ARS"]
)

df["Ganancia_Bruta_ARS"] = (
    df["Ingreso_Real_Mensual_ARS"]
    - df["Costo_Mensual_ARS"]
)

df["ROI_pct"] = (
    df["Ganancia_Bruta_ARS"]
    / df["Costo_Mensual_ARS"]
) * 100

ranking = df.sort_values(
    "Ganancia_Bruta_ARS",
    ascending=False
)
# Nombres amigables para mostrar
nombres_activos = {
    "Motor_secarropas": "Dryer Motor",
    "Motor_lavarropas": "Washing Machine Motor",
    "Transformador_microondas": "Microwave Transformer",
    "Aire_acondicionado": "Air Conditioner",
    "Heladera": "Refrigerator"
}

ranking["Activo"] = ranking["Activo"].replace(nombres_activos)
# ----------------------------------
# KPI
# ----------------------------------

st.header("Key Findings")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Copper Recovery",
        f"{df['Cobre_Real_Mensual_kg'].sum():.2f} kg"
    )

with col2:
    st.metric(
        "Monthly Revenue",
        f"${df['Ingreso_Real_Mensual_ARS'].sum():,.0f}"
    )

with col3:
    st.metric(
        "Monthly Profit",
        f"${df['Ganancia_Bruta_ARS'].sum():,.0f}"
    )

with col4:
    st.metric(
        "Best ROI",
        f"{df['ROI_pct'].max():.2f}%"
    )

# ----------------------------------
# MAIN DISCOVERY
# ----------------------------------

st.success("""
🏆 Main Discovery

Air conditioners generated an estimated ROI of 558.75%,
while refrigerators generated only 5.4%.

Urban mining profitability depends primarily on asset selection.
""")

# ----------------------------------
# RANKING
# ----------------------------------

st.header("Urban Mining Asset Ranking")

st.dataframe(
    ranking[
        [
            "Activo",
            "Ganancia_Bruta_ARS",
            "ROI_pct"
        ]
    ]
)

# ----------------------------------
# CHART
# ----------------------------------

st.header("Gross Profit by Asset")

fig, ax = plt.subplots(figsize=(10,5))

ax.bar(
    ranking["Activo"],
    ranking["Ganancia_Bruta_ARS"]
)

ax.set_title(
    "Gross Profit by Asset"
)

ax.set_ylabel(
    "ARS"
)

plt.xticks(rotation=45)

st.pyplot(fig)

# ----------------------------------
# RESEARCH QUESTIONS
# ----------------------------------

st.header("Research Questions Answered")

st.markdown("""
✅ Is urban mining profitable?

✅ Which asset generates the highest ROI?

✅ Can urban mining be modeled using data analytics?

✅ Can field observation be transformed into a decision model?
""")

# ----------------------------------
# CONCLUSIONS
# ----------------------------------

st.header("Research Conclusions")

st.markdown("""
- Air conditioners are the highest-value urban mining asset.

- Microwave transformers show exceptional profitability.

- Electric motors are the primary economic unit.

- Urban mining behaves like a portfolio of assets.

- Asset selection determines profitability.
""")

# ----------------------------------
# METHODOLOGY
# ----------------------------------

st.header("Methodology")

st.markdown("""
This project combines:

- Field observation
- Data collection
- Economic modeling
- ROI analysis
- Decision science
- Data analytics
""")

# ----------------------------------
# TOOLS
# ----------------------------------

st.header("Tools Used")

st.markdown("""
- Python
- Pandas
- Jupyter Notebook
- Streamlit
- GitHub
""")

# ----------------------------------
# FOOTER
# ----------------------------------

st.divider()

st.caption(
    "Case Study #1 — Urban Mining Economics in Argentina | Independent Data Analytics Research Project"
)