# 🔐 SentinelAI: Cybersecurity Intrusion Detection & Monitoring System

## 🚀 Overview

**SentinelAI** is a real-time cybersecurity system that detects, analyzes, and visualizes potential threats from system and network logs.
It combines **rule-based detection**, **machine learning**, **IP tracking**, and **interactive dashboards** to simulate a real Security Operations Center (SOC).

---

## 🎯 Features

### 🔍 Threat Detection

* Detects:

  * Brute Force Attacks
  * SQL Injection Attempts
  * Unauthorized Access
  * Scanning Activities

### 🤖 AI Anomaly Detection

* Uses **Isolation Forest (Machine Learning)**
* Identifies abnormal log patterns automatically

### 🌍 IP Tracking & Geolocation

* Extracts IP from logs
* Displays:

  * Country 🌎
  * City 🏙️
  * ISP 🌐
* Shows live map using Google Maps

### 📊 Dashboard & Visualization

* Interactive charts using **Chart.js**
* Displays:

  * Attack distribution
  * Threat ratios

### 💾 Log Storage

* Stores logs securely using **SQLite database**

### 🚨 Alert System

* Sends email alerts for detected threats

### 🔐 (Optional) Blockchain Integration

* Stores logs on blockchain (Ganache + Web3)
* Ensures tamper-proof security

---

## 🛠️ Tech Stack

| Layer                 | Technology            |
| --------------------- | --------------------- |
| Backend               | Python                |
| Framework             | Django                |
| Frontend              | HTML, CSS, JavaScript |
| Charts                | Chart.js              |
| Machine Learning      | Scikit-learn          |
| Database              | SQLite                |
| API                   | ip-api (IP tracking)  |
| Blockchain (Optional) | Web3 + Ganache        |

---

## 📁 Project Structure

```
cyber_security_project/
│
├── analyzer/
│   ├── detector.py
│   ├── ml_model.py
│
├── database/
│   ├── db.py
│
├── alerts/
│   ├── alerts.py
│
├── app/
│   ├── views.py
│   ├── templates/
│
├── webapp/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Project

```bash
git clone <your-repo-link>
cd cyber_security_project
```

### 2️⃣ Install Dependencies

```bash
pip install django
pip install scikit-learn
pip install requests
```

### 3️⃣ Create Database

```bash
python manage.py migrate
```

### 4️⃣ Run Server

```bash
python manage.py runserver
```

### 5️⃣ Open Browser

```
http://127.0.0.1:8000/
```

---

## 🧪 Sample Test Logs

Try these inputs:

```
Failed password for root from 192.168.1.1
```

```
SELECT * FROM users WHERE id=1 OR 1=1
```

```
Normal login from user
```

---

## 📸 Screenshots (Optional)

* Dashboard UI
* Threat Detection Result
* Charts
* IP Map

---

## 🎓 Use Cases

* Final Year Project
* Cybersecurity Learning
* SOC Simulation
* Internship Portfolio

---

## 🚀 Future Enhancements

* 🌍 Multi-IP live tracking map
* 📡 Real-time updates (WebSockets)
* 🔐 Smart contract integration
* 🚫 Auto-block malicious IPs
* 📊 Timeline attack analysis

---

## 👨‍💻 Author

**Ashvik**

---

## ⭐ Conclusion

SentinelAI demonstrates how modern cybersecurity systems combine **AI, visualization, and real-time monitoring** to detect and prevent threats effectively.

---

## 📜 License

This project is for educational purposes.

