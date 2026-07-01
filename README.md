# ♻️ Copper Recycling Decision System

## 📌 Project Overview

Every weekend, I noticed trucks driving through my neighborhood in Argentina buying old refrigerators, batteries, washing machines, microwaves, and clothes dryers.

This observation led me to ask a simple but powerful business question:

> **How profitable is the copper recycling business?**

To answer this question, I designed a data analytics project focused on understanding the economics of urban copper recycling, analyzing market trends, and developing a decision-support system for recyclers.

---

## 🎯 Research Question

**How profitable is the urban copper recycling business in Argentina, and when is the optimal time for a recycler to sell accumulated copper?**

---

## 📊 Project Objectives

This project aims to:

* Analyze the profitability of urban copper recycling.
* Study the copper value chain, from collectors to foundries.
* Investigate historical international copper prices.
* Compare international and local copper prices.
* Analyze the behavior and decision-making process of urban recyclers.
* Build a decision-support system to determine the optimal selling time.

---

## 🔍 Research Process

The project was developed following a business analytics approach:

### 1. Observation

* Informal collection networks operate actively in urban areas.
* Trucks regularly purchase discarded appliances and scrap materials.

### 2. Business Question

* Is copper recycling a profitable business?
* Who captures the most value in the supply chain?
* Is it better to sell immediately or accumulate inventory?

### 3. Data Collection

* International copper prices (LME).
* Local copper prices in Argentina.
* Estimated copper recovery from household appliances.
* Market trends and seasonality.

### 4. Analysis

* Historical price evolution.
* Profitability scenarios.
* Supply chain analysis.
* Behavioral analysis of recyclers.
* Decision modeling.

### 5. Product Development

Development of a decision-support dashboard using Streamlit.

---

## ♻️ Copper Supply Chain Model

Urban Recycler
↓
Local Scrap Dealer
↓
Regional Wholesaler
↓
Foundry
↓
Industrial Market

---

## 📈 Initial Findings

Preliminary analysis suggests:

* Copper prices for recyclers in Argentina have increased significantly during the last two years.
* The decision to sell depends not only on price but also on accumulated inventory volume.
* Most urban recyclers appear to follow a conservative strategy, prioritizing immediate liquidity over speculation.
* Market timing and international copper trends may influence profitability.

---

## 🧠 Decision Model

The project proposes a decision-support model based on three variables:

### Inventory Level

* Amount of copper accumulated.

### Market Conditions

* International copper prices.
* Local market prices.
* Seasonal patterns.

### Market Indicator ("Copper Traffic Light")

* 🟢 Bullish market.
* 🟡 Neutral market.
* 🔴 Bearish market.

The final objective is to answer:

> **Should I sell my copper today or wait?**

---

## 🛠️ Technologies

* Python
* Streamlit
* Pandas
* Git
* GitHub
* Data Analytics
* Business Analytics

---

## 📂 Project Structure

```text
copper-recycling-decision-system/

├── app/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── docs/
├── images/
├── README.md
└── requirements.txt
```

---

## 🚀 Future Development

Planned features include:

* Automatic international copper price updates.
* Historical trend visualization.
* Scenario simulation.
* Predictive models.
* Interactive decision dashboard.
* Profitability optimization analysis.

---

## 👨‍💻 Author

This project was developed as an independent data analytics and business research project focused on urban recycling economics and decision support systems.
