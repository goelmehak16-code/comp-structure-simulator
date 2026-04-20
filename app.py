import streamlit as st

st.set_page_config(page_title="CompStruct", layout="wide")

st.title("💼 Compensation Structure Simulator")
st.markdown("Design salary structures & analyze compliance + cost impact")

# Sidebar Input
st.sidebar.header("📥 Input Salary")

basic = st.sidebar.number_input("Basic", value=30000)
da = st.sidebar.number_input("DA", value=5000)
hra = st.sidebar.number_input("HRA", value=20000)
special = st.sidebar.number_input("Special Allowance", value=15000)
bonus = st.sidebar.number_input("Bonus", value=5000)

# Calculations
total = basic + da + hra + special + bonus
wages = basic + da
wage_percent = (wages / total) * 100 if total > 0 else 0

pf = 0.12 * wages
gratuity = (15/26) * wages * 10

# Dashboard
col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Salary", f"₹{total:,.0f}")
col2.metric("⚖️ Wage %", f"{wage_percent:.1f}%")
col3.metric("🏦 PF (Monthly)", f"₹{pf:,.0f}")

# Compliance
st.subheader("⚖️ Compliance Check")

if wage_percent >= 50:
    st.success("✔ Compliant (≥50%)")
else:
    st.error("❌ Not Compliant (<50%)")

# Financial Impact
st.subheader("💸 Financial Impact")

st.write(f"Gratuity (10 yrs): ₹{gratuity:,.0f}")
st.write(f"Annual PF: ₹{pf*12:,.0f}")

# What-if
st.subheader("🔄 Scenario Simulator")

new_basic = st.slider("Adjust Basic Salary", 0, int(total), basic)

new_wages = new_basic + da
new_percent = (new_wages / total) * 100 if total > 0 else 0

st.write(f"New Wage %: {new_percent:.1f}%")

if new_percent >= 50:
    st.success("✔ New Structure Compliant")
else:
    st.warning("⚠ Still Non-Compliant")

# Insight
st.info("Increasing basic improves compliance but increases PF & gratuity.")
