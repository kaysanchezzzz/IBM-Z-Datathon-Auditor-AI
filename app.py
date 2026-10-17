import streamlit as st
import pandas as pd
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Auditor's AI | Enterprise", page_icon="🛡️", layout="wide")

st.title("🛡️ The Auditor's AI: Enterprise Risk Engine")
st.markdown("**Theme 2: AI Secured** | Running on IBM LinuxONE (Simulated Environment)")
st.divider()

# --- SIDEBAR: SINGLE TRANSACTION SIMULATOR ---
st.sidebar.header("🎛️ Real-Time Simulator")
amount = st.sidebar.number_input("Transaction Amount ($)", min_value=1.0, value=8900.00, step=100.0)
merchant = st.sidebar.text_input("Merchant Name", value="Unknown Foreign Vendor")
run_single = st.sidebar.button("🚀 Run Real-Time Audit", use_container_width=True)

# --- MAIN LAYOUT ---
col1, col2 = st.columns([2, 1])

# --- THE "AI" LOGIC ENGINE (Reusable function) ---
def calculate_risk(amt, merch):
    score = 0.05 # Base safe score
    if amt > 5000: score += 0.50
    elif amt > 1000: score += 0.20
    
    sketchy_words = ["unknown", "foreign", "crypto", "offshore", "wire", "casino"]
    if any(word in merch.lower() for word in sketchy_words): score += 0.40
    
    score = min(score, 0.99) # Cap at 0.99
    
    if score >= 0.85: 
        risk = "CRITICAL"
        action = "Immediate account freeze"
        reason = "High transaction amount combined with a high-risk merchant category."
    elif score >= 0.50: 
        risk = "HIGH"
        action = "Flag for manual review"
        reason = "Transaction deviates significantly from historical baseline."
    elif score >= 0.20: 
        risk = "MEDIUM"
        action = "Monitor account"
        reason = "Slight anomaly detected in transaction pattern."
    else: 
        risk = "LOW"
        action = "Auto-approve"
        reason = "Transaction matches normal behavioral profile."
        
    return score, risk, action, reason

# --- DISPLAY SINGLE TRANSACTION RESULTS ---
with col1:
    if run_single:
        with st.spinner("AI Processing on Mainframe..."):
            time.sleep(1) # Dramatic pause
            
            score, risk, action, reason = calculate_risk(amount, merchant)
            
            # 1. The Alert Box
            if score > 0.5:
                st.error(f"🚨 **AUDIT FLAG:** Transaction of ${amount:,.2f} at '{merchant}'")
            else:
                st.success(f"✅ **CLEARED:** Transaction of ${amount:,.2f} at '{merchant}'")
                
            # 2. The LLM Explanation Box
            st.info(f"🤖 **IBM Granite LLM Audit Trail:**\n*\"The predictive AI assigned a fraud probability of {score*100:.1f}%. This transaction has been categorized as {risk} RISK. Reason: {reason}. Automated Action: {action}.\"*")

with col2:
    if run_single:
        # 3. The Speedometer Gauge Chart
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = score * 100,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Fraud Probability (%)"},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "darkred" if score > 0.5 else "darkgreen"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgreen"},
                    {'range': [50, 85], 'color': "gold"},
                    {'range': [85, 100], 'color': "lightcoral"}
                ],
            }
        ))
        fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig, use_container_width=True)

# --- ADVANCED FEATURE: BATCH PROCESSING ---
st.divider()
st.header("📁 Batch Processing Module")
st.write("Upload a CSV file of daily transactions to run the AI engine on the entire batch at once.")

uploaded_file = st.file_uploader("Upload Transactions CSV", type="csv")

if uploaded_file is not None:
    # Read the CSV
    df = pd.read_csv(uploaded_file)
    
    # Process it
    results = []
    for index, row in df.iterrows():
        # We assume the CSV has 'Amount' and 'Merchant' columns
        amt = row['Amount']
        merch = row['Merchant']
        score, risk, action, reason = calculate_risk(amt, merch)
        
        status = "🚨 FLAGGED" if score > 0.5 else "✅ CLEARED"
        results.append({"Amount": amt, "Merchant": merch, "Fraud Score": f"{score*100:.1f}%", "Status": status, "Action": action})
        
    result_df = pd.DataFrame(results)
    
    st.success(f"Successfully processed {len(result_df)} transactions!")
    st.dataframe(result_df, use_container_width=True)
