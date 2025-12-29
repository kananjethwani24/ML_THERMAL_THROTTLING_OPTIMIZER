import psutil
import joblib
import time
import os
import pandas as pd

model = joblib.load("thermal_model.pkl")
THRESHOLD = 75  # degrees Celsius

while True:
    temp = psutil.sensors_temperatures()['coretemp'][0].current
    load = psutil.cpu_percent()
    freq = psutil.cpu_freq().current

    X = pd.DataFrame([[temp, load, freq]], columns=["temp", "cpu_load", "freq"])
    predicted = model.predict(X)[0]

    if predicted > THRESHOLD:
        os.system("cpufreq-set -g powersave")
        print("⚠ Predictive throttling enabled")
    else:
        os.system("cpufreq-set -g performance")
        print("✔ Normal performance mode")

    time.sleep(2)

