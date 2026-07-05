import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Urban Mining Economics",
    layout="wide"
)

st.title("♻️ Urban Mining Economics in Argentina")
st.subheader(
    "A Data Analytics Approach to Urban Copper Recovery"
)

# Datos
df = pd.read_csv(
    "data/raw/urban_mining_field_data.csv"
)

# Parámetros
precio_cobre = 15500
factor_recuperacion = 0.85

# Cálculos
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

# KPIs
st.header("Key Findings")

col1, col2, col3 = st.columns(3)

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

# Ranking
st.header("Urban Mining Asset Ranking")

ranking = df.sort_values(
    "Ganancia_Bruta_ARS",
    ascending=False
)

st.dataframe(
    ranking[
        [
            "Activo",
            "Ganancia_Bruta_ARS",
            "ROI_pct"
        ]
    ]
)

# Gráfico
st.header("Gross Profit by Asset")

fig, ax = plt.subplots(figsize=(8,4))

ax.bar(
    ranking["Activo"],
    ranking["Ganancia_Bruta_ARS"]
)

plt.xticks(rotation=45)

st.pyplot(fig)

# Conclusiones
st.header("Research Conclusions")

st.markdown("""
- Air conditioners are the highest-value urban mining asset.
- Microwave transformers show exceptional profitability.
- Electric motors are the primary economic unit.
- Urban mining behaves like a portfolio of assets.
- Asset selection determines profitability.
""")