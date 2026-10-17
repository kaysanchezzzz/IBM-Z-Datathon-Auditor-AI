import streamlit as st
import pandas as pd
import time

# Set page config
st.set_page_config(page_title="The Auditor's AI", page_icon="🛡️", layout="wide")

st.title("🛡️ The Auditor's AI Dashboard")
st.subheader("Privacy-Preserving Fraud Detection on IBM LinuxONE")
st.write("A Hybrid AI solution for forensic accounting. Adjust the inputs below to simulate real-time transaction auditing.")

# Layout with columns
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 🎛️ Transaction Simulator")
    amount = st.number_input("Transaction Amount ($)", min_value=1.0, value=8900.00, step=100.0)
    merchant = st.text_input("Merchant Name", value="Unknown Foreign Vendor")
    fraud_score = st.slider("AI Fraud Probability Score", 0.0, 1.0, 0.95, step=0.01)
    
    run_btn = st.button("🚀 Run Real-Time Audit", use_container_width=True)

with col2:
    st.markdown("### 📋 Audit Output")
    if run_btn:
        with st.spinner("AI Processing on Mainframe..."):
            time.sleep(1) # Simulate processing time
            
            if fraud_score >= 0.85: risk, action = "CRITICAL RISK", "Immediate account freeze & forensic audit required."
            elif fraud_score >= 0.50: risk, action = "HIGH RISK", "Flag for manual review by senior auditor."
            elif fraud_score >= 0.20: risk, action = "MEDIUM RISK", "Monitor account for 24 hours."
            else: risk, action = "LOW RISK", "Auto-approve. No action needed."
            
            if fraud_score > 0.5:
                st.error(f"🚨 **AUDIT FLAG:** Transaction of ${amount:,.2f} at {merchant}")
            else:
                st.success(f"✅ **CLEARED:** Transaction of ${amount:,.2f} at {merchant}")
                
            # Dashboard Metrics
            m1, m2, m3 = st.columns(3)
            m1.metric(label="Risk Category", value=risk)
            m2.metric(label="Fraud Probability", value=f"{fraud_score*100:.1f}%")
            m3.metric(label="Action", value=action.split(' ')[0] + " " + action.split(' ')[1])
            
            # Generated Audit Note
            st.markdown("#### 📝 Generated Audit Trail")
            st.info(f"**System Log:** A transaction of ${amount:,.2f} at '{merchant}' was evaluated by the LSTM model. The predictive AI assigned a fraud probability of {fraud_score*100:.1f}%, placing it in the **{risk}** category. **Automated Action:** {action}")

# Add a fake historical log at the bottom to make it look like a real system
if run_btn:
    st.markdown("---")
    st.markdown("### 🗄️ Recent Audit History")
    history_data = pd.DataFrame({
        "Transaction ID": ["TX-1092", "TX-1093", "TX-1094"],
        "Merchant": ["Local Coffee", "Offshore Crypto", "Grocery Store"],
        "Amount": [12.50, 2500.00, 85.00],
        "Score": [0.02, 0.95, 0.10],
        "Status": ["✅ CLEARED", "🚨 FLAGGED", "✅ CLEARED"]
    })
    st.dataframe(history_data, use_container_width=True)
