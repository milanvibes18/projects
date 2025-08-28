# 🧑‍⚕️ AI-Powered Digital Twin Assistant

## 📌 Project Overview

This project is an **AI-Powered Digital Twin for Personalized Health & Lifestyle Assistance**.
It collects health and activity data (currently simulated, later via Arduino IoT sensors) and provides **real-time monitoring, anomaly detection, and visual dashboards**.

---

## ✅ Current Progress (Phase 1 Completed)

* **Database (SQLite):** Stores timestamped health data.
* **AI Rules:** Detect abnormal heart rates (Low <50, High >120).
* **Flask Backend:**

  * `/get_data` → Full history (JSON)
  * `/latest` → Latest reading + status (JSON)
  * `/dashboard` → HTML dashboard with table + auto-updating chart
* **Frontend (Dashboard):**

  * Real-time table of values
  * Live graph (Chart.js) auto-refreshing every 5s
* **Fake Data Generator:** Simulates heart rate readings continuously

---

## 🚀 Next Steps (Planned)

* Integrate **Arduino Uno/ESP32 + Sensors**:

  * MAX30102 (Pulse & SpO₂)
  * MPU6050 (Steps & Activity)
  * LDR (Sleep environment)
* Extend AI analysis (sleep patterns, daily activity detection).
* Privacy-first storage & optional cloud sync.
* Mobile-friendly dashboard.

---

## 🛠️ Tech Stack

* **Hardware (Upcoming):** Arduino Uno / ESP32, IoT sensors
* **Backend:** Flask (Python)
* **Database:** SQLite
* **Frontend:** HTML, CSS, Chart.js
* **AI/ML:** Rule-based logic (current), TensorFlow/Scikit-learn (future)

---

## 📂 Project Structure

```
digital-twin-project/
│
├── app.py             # Flask API + dashboard routes
├── insert_data.py     # Fake data generator (simulates Arduino sensor input)
├── health_data.db     # SQLite database (auto-created)
└── templates/
    └── dashboard.html # Dashboard (table + live graph)
```

---

## 📸 Screenshots (Optional)

<img width="1828" height="927" alt="image" src="https://github.com/user-attachments/assets/3df215f4-b378-4c03-95bc-66a922b31347" />


---

## ⚡ How to Run

1. Clone the repo:

   ```bash
   git clone https://github.com/<your-username>/projects.git
   cd projects/digital-twin-project
   ```
2. Install dependencies:

   ```bash
   pip install flask matplotlib
   ```
3. Run the fake data generator in one terminal:

   ```bash
   python insert_data.py
   ```
4. Run the Flask app in another terminal:

   ```bash
   python app.py
   ```
5. Open in browser:

   * `http://127.0.0.1:5000/get_data` → JSON history
   * `http://127.0.0.1:5000/latest` → Latest reading
   * `http://127.0.0.1:5000/dashboard` → Dashboard with table + live chart

---

## 👨‍💻 Author

* **Name:** Milan
* **B.Tech CSE (2024–2028)**
* **Focus Areas:** IoT, Blockchain, Cybersecurity

---
