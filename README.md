The Auditor's AI: Privacy-Preserving Fraud Detection
IBM Z Datathon 2026 - Theme 2: AI Secured (Innovation Without Exposure)
Author: Syakir Kauthar Bin Sahril (Bachelor of Accounting Hons Student)

Live Interactive Demo
Try the live Streamlit web app here: https://ibm-z-datathon-auditor-ai-krbwkjlhcrjqywrqxpo498.streamlit.app/

Project Overview
Financial auditors cannot trust "black box" AI models, and banks cannot send sensitive data to public cloud AIs due to compliance laws (GDPR, SOX). This project solves that by deploying a Hybrid AI system entirely on an IBM LinuxONE mainframe.

Architecture
1. Predictive AI (TensorFlow LSTM): Analyzes 24 million transactions for anomalous patterns (99.86% accuracy).
2. Risk Engine: Categorizes transactions into Low, Medium, High, and Critical risk.
3. Generative AI (IBM Granite LLM Simulation): Generates human-readable, natural-language audit trails for flagged transactions.

Tech Stack
- Hardware: IBM LinuxONE (s390x architecture)
- Environment: Docker, Jupyter Lab
- Libraries: TensorFlow, Pandas, Matplotlib
- Deployment: Model exported to .onnx format.

Evidence
- Auditor_AI_Project.ipynb: The main project notebook.
- app.py: The Streamlit web app code.
- fraud_lstm.onnx: The exported predictive model.

You want the GitHub `README.md` to match the absolute fire of your pitch deck. Let's turn it from a simple text file into a professional, eye-catching project landing page. 

GitHub uses Markdown, so we can add bold text, emojis, headers, and even a "badges" section at the top that makes it look like real enterprise software.

Copy everything below and paste it directly into your `README.md` on GitHub. 

***

# 🛡️ The Auditor's AI: Privacy-Preserving Fraud Detection
**IBM Z Datathon 2026 — Theme 2: AI Secured (Innovation Without Exposure)**

[![Live Demo](https://img.shields.io/badge/Live_Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](YOUR_STREAMLIT_LINK_HERE)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.18-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)]()
[![IBM LinuxONE](https://img.shields.io/badge/IBM_LinuxONE-s390x-052FAD?style=for-the-badge&logo=ibm&logoColor=white)]()

> **Author:** Syakir Kauthar Bin Sahril (Bachelor of Accounting Hons. Student)  
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

👉 **[Click here to launch the Live Web App](YOUR_STREAMLIT_LINK_HERE)**

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

***

### 🚨 ACTION ITEMS FOR YOU:
1. **Find and Replace:** In the text above, replace `YOUR_STREAMLIT_LINK_HERE` with your actual Streamlit URL (there are two places to do this).
2. **Paste it into GitHub:** Click the pencil icon on your `README.md` file, delete the old text, paste this in, and click **Commit changes**.
3. **Look at your repo:** GitHub will automatically render the badges and bold text. It's going to look like a professional open-source software project.

**Once you commit this, go straight to H2S and hit submit. You are literally out of time!**
