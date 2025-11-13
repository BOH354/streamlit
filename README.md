🖥️ Infrastructure Monitoring Dashboard
A Streamlit-Based System Health & Resource Monitoring Tool

📘 Overview
This project is an infrastructure monitoring dashboard developed for a university assignment as part of a broader exploration into system administration, security, and system visualisation.
The application provides a real-time view of system health, resource usage, and diagnostic information using a clean, multipage Streamlit interface.

This final version extends an earlier beta prototype originally built using HTML, CSS, PHP, and JavaScript. It has now been re-implemented using Python and Streamlit to improve portability, streamline development, and enable simplified deployment on virtualised environments.

🎯 Project Objectives
Design, build, and deploy a functional system monitoring dashboard
Provide real-time system metrics (CPU, memory, disk, processes)
Support testing within a controlled virtual environment (e.g., Kali Linux VM)
Demonstrate the evolution from a traditional LAMP-style stack to a Python framework
Show understanding of virtualisation, OS interaction, and local infrastructure tooling

🧩 Features
System Information Panel
Hostname
Operating system
Architecture
Uptime
Resource Monitoring
CPU usage
Memory consumption
Disk utilisation
Processes Overview
Active processes
High-resource tasks
Multipage Streamlit Layout
Organised pages for metrics, system information, and diagnostics
Lightweight Deployment
Runs locally on any Linux VM with Python

📦 Installation
Requirements
Python 3.8+
Streamlit
pandas
psutil

Linux environment (tested on Kali Linux)

Install dependencies
pip install streamlit pandas psutil

▶️ Running the Application
Local run
python -m streamlit run app.py

Access in a browser:
http://localhost:8501

Remote access (within VM network)
python -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501


From another device:
http://<vm-ip>:8501

🏗️ Project Structure
Streamlit/
 ├── app.py
 ├── pages/
 ├── Images/
 └── README.md

Add log analysis and threat-detection modules

Containerise the application using Docker
