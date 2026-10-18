
# 🛡️ The Auditor's AI: Privacy-Preserving Fraud Detection
**IBM Z Datathon 2026 — Theme 2: AI Secured (Innovation Without Exposure)**

[![Live Demo](https://img.shields.io/badge/Live_Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ibm-z-datathon-auditor-ai-krbwkjlhcrjqywrqxpo498.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.18-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)]()
[![IBM LinuxONE](https://img.shields.io/badge/IBM_LinuxONE-s390x-052FAD?style=for-the-badge&logo=ibm&logoColor=white)]()
[![Video Pitch](https://img.shields.io/badge/▶_Watch_Video_Pitch-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/Mt8geS_b20Y)

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

## 🎥 Project Demo & Video Pitch

Watch the 3-minute video pitch explaining the problem, the architecture, and a live demo of the application running.

👉 **[Click here to watch the Video Pitch](https://youtu.be/Mt8geS_b20Y)**

*Video covers: Problem Statement → Architecture → Jupyter Notebook Evidence → Live Streamlit Demo.*

---

### 🚀 Live Interactive Demo
Experience the enterprise dashboard yourself. The Streamlit app includes a **Real-Time Simulator** and a **Batch Processing Module** for CSV uploads.

👉 **[Click here to launch the Live Web App](https://ibm-z-datathon-auditor-ai-krbwkjlhcrjqywrqxpo498.streamlit.app/)**

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


## 📊 Model Performance & Accuracy

Our LSTM model achieved a **99.86% accuracy** rate on the test dataset. Because this is a fraud detection task, we prioritized **Recall (100%)** to ensure we caught every single fraudulent transaction, even if it meant flagging a few false positives.

*(Note: The trained model is exported as `fraud_lstm.onnx` for production deployment. Due to its binary format, it cannot be opened directly in a browser, but the training logs and precision/recall metrics are shown below.)*

<img width="1280" height="524" alt="image" src="https://github.com/user-attachments/assets/e8efd31f-4313-4ecd-84f9-4cb61df1ca06" />
<img width="1280" height="553" alt="image" src="https://github.com/user-attachments/assets/681fe15c-f433-4246-89a0-01051a971949" />
<img width="1280" height="367" alt="image" src="https://github.com/user-attachments/assets/76cb6e0c-109a-4503-8d62-8f5fd38c9330" />


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


