import streamlit as st

st.set_page_config(page_title="Auditor AI", page_icon="🛡️")
st.title("🛡️ The Auditor's AI")
st.subheader("Privacy-Preserving Fraud Detection on IBM LinuxONE")

amount = st.number_input("Transaction Amount ($)", value=8900.00)
merchant = st.text_input("Merchant Name", value="Unknown Foreign Vendor")
score = st.slider("AI Fraud Probability Score", 0.0, 1.0, 0.95)

if st.button("Run AI Audit"):
    if score >= 0.85: risk, action = "CRITICAL RISK", "Immediate account freeze."
    elif score >= 0.50: risk, action = "HIGH RISK", "Flag for manual review."
    elif score >= 0.20: risk, action = "MEDIUM RISK", "Monitor account."
    else: risk, action = "LOW RISK", "Auto-approve."
    
    st.markdown("---")
    if score > 0.5: st.error(f"🚨 FLAGGED: ${amount} at {merchant}")
    else: st.success(f"✅ CLEARED: ${amount} at {merchant}")
    
    st.write(f"**Risk Level:** {risk}")
    st.write(f"**Action:** {action}")