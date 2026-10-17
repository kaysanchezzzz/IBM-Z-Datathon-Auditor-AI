
# 🛡️ The Auditor's AI: Privacy-Preserving Fraud Detection
**IBM Z Datathon 2026 — Theme 2: AI Secured (Innovation Without Exposure)**

[![Live Demo](https://img.shields.io/badge/Live_Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ibm-z-datathon-auditor-ai-krbwkjlhcrjqywrqxpo498.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.18-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)]()
[![IBM LinuxONE](https://img.shields.io/badge/IBM_LinuxONE-s390x-052FAD?style=for-the-badge&logo=ibm&logoColor=white)]()

> **Author:** Syakir Kauthar Bin Sahril (Bachelor of Accounting Hons. UNITEN Student)  
> **Objective:** To bridge the gap between forensic accounting and enterprise AI by providing transparent, explainable, and secure fraud detection.

---

### 📖 The Problem: The Compliance Nightmare
Financial auditors cannot trust "black box" AI models, and banks cannot send sensitive customer data to public AI clouds due to strict banking regulations (GDPR, SOX). 

**The Solution:** A Hybrid AI pipeline running entirely on an **IBM LinuxONE mainframe**. By keeping the predictive model, the risk engine, and the generative AI audit trail entirely inside the bank's infrastructure, we achieve **Innovation Without Exposure**.

---

### ⚙️ Architecture & Pipeline

| Module | Technology | Function |
| :--- | :--- | :--- |
| **Input** | Pandas / NumPy | Ingests transaction history (245,864 records). |
| **Predictive AI** | TensorFlow LSTM | Analyzes sequences of 7 transactions to detect anomalies (99.86% accuracy). |
| **Risk Engine** | Python Logic | Translates probability scores into actionable tiers (Low to Critical). |
| **Generative AI** | IBM Granite LLM (Simulated) | Generates plain-language audit trails for every flagged transaction. |

---

### 🚀 Live Interactive Demo
Experience the enterprise dashboard yourself. The Streamlit app includes a **Real-Time Simulator** and a **Batch Processing Module** for CSV uploads.

👉 **[Click here to launch the Live Web App]((https://ibm-z-datathon-auditor-ai-krbwkjlhcrjqywrqxpo498.streamlit.app/))**

*Demo Test Cases:*
*   Try `$15.00` at `Starbucks` -> ✅ CLEARED
*   Try `$8900.00` at `Offshore Crypto` -> 🚨 CRITICAL RISK

---

### 📂 Repository Contents
*   📓 `Auditor_AI_Project.ipynb` - The complete Jupyter Notebook (Data ingestion, Risk Engine, Benford's Law Forensic Check).
*   🐍 `app.py` - The Streamlit front-end web application code.
*   🧠 `fraud_lstm.onnx` - The trained LSTM model exported to the industry-standard ONNX format.
*   📄 `requirements.txt` - Python dependencies for cloud deployment.

---

### 🏆 Key Achievements
*   Trained an LSTM model on **245,864 transactions** achieving **99.86% accuracy**.
*   Deployed a fully functional web app via **Streamlit Cloud**.
*   Integrated **Benford's Law** mathematical anomaly detection for forensic accounting.
*   Containerized the entire environment using **Docker** on the IBM Z (s390x) architecture.

---

### 💻 How to Run Locally
1. Clone the repository: `git clone https://github.com/kaysanchezzzz/IBM-Z-Datathon-Auditor-AI.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Launch the Streamlit app: `streamlit run app.py`

---
*Created for the IBM Z Datathon 2026. Built with passion for forensic accounting and secure AI.*


