# 🔥 ML-Based Real-Time Thermal Throttling Optimizer

This project predicts CPU temperature **3–5 seconds ahead** using a lightweight machine-learning model and proactively reduces CPU frequency **before overheating occurs**.  
The goal is to improve **system stability, thermal safety, and battery efficiency** compared to traditional **reactive throttling** used in most operating systems.

---

## 🧠 Project Idea

Conventional OS thermal control reduces CPU frequency **only after** the temperature crosses a critical threshold. This causes:

- Sudden performance drops  
- Higher heat spikes  
- Reduced hardware lifespan  

This project implements **predictive thermal management**:

> Predict temperature → Detect risk early → Prevent overheating proactively

---

## ⚙️ Features

- ✔ Collects real CPU sensor data in real time  
- ✔ Trains regression-based ML model on system behavior  
- ✔ Predicts future CPU temperature (3 seconds ahead)  
- ✔ Automatically switches CPU frequency governor  
- ✔ Prevents heat spikes instead of reacting late  

---

## 🏗️ Tech Stack

- **Operating System:** Ubuntu Linux  
- **Programming Language:** Python  
- **Libraries:** psutil, pandas, scikit-learn, joblib  
- **System Tools:** lm-sensors, cpufrequtils, stress  

---

## 📂 Project Structure

thermal_ml_os/
├─ collect_data.py # CPU temp/load data collection
├─ train_model.py # Train ML prediction model
├─ predictor.py # Real-time temperature prediction
├─ controller.py # Predictive throttling controller
├─ cpu_data.csv # Recorded dataset (sample)
├─ thermal_model.pkl # Trained ML model
├─ docs/ # PPT / Report
└─ media/ # Demo video / Screenshots

---

## 🔍 How the System Works

### 1️⃣ Data Collection
The system records:
- CPU temperature  
- CPU usage percentage  
- CPU frequency  

Data is collected under both:
- Idle / normal load  
- High load (generated using `stress --cpu 4`)

---

### 2️⃣ Model Training
A lightweight **Linear Regression model** learns the relationship:

Current Temperature + CPU Load + Frequency → Temperature After 3 Seconds


The model is chosen because it is:
- Fast  
- Resource-efficient  
- Suitable for real-time OS behavior  

---

### 3️⃣ Real-Time Prediction
The trained model runs continuously and predicts upcoming CPU temperature using live sensor data.

---

### 4️⃣ Predictive OS-Level Throttling

If the **predicted temperature exceeds a threshold**:
- CPU governor → `powersave`
- Heat rise is prevented early

Else:
- CPU governor → `performance`

This creates **predictive thermal throttling** instead of reactive control.

---

## 🧪 Results & Outcome

- 🔻 Reduced heat spikes  
- ⚡ Smoother performance  
- 🔋 Better thermal efficiency  
- 🛡️ Improved hardware safety  

---

## 🎥 Project Resources

📊 **Presentation PPT** — stored in `/docs/`  
🎥 **Working Demo Video** — stored in `/media/` (or linked externally)

---

## 🙋 Author

**KANAN JETHWANI**

---

## 📝 Academic Note

This project demonstrates the integration of:

- Operating System concepts (CPU frequency scaling)
- Machine Learning for predictive control
- Real-time system monitoring
- Practical Linux-based implementation

Suitable for:
- Operating Systems project / Mini Project  
- ML + Systems integration prototype  
- Academic evaluation, presentation, and viva  

---
