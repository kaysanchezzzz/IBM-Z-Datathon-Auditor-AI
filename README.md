The Auditor's AI: Privacy-Preserving Fraud Detection
IBM Z Datathon 2026 - Theme 2: AI Secured (Innovation Without Exposure)
Author: Syakir Kauthar Bin Sahril (Bachelor of Accounting Hons Student)

Live Interactive Demo
Try the live Streamlit web app here: https://ibm-z-datathon-auditor-ai-nwzue7nydzoym9cshvmre.streamlit.app

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
