import psutil
import joblib
import time
import pandas as pd

model = joblib.load("thermal_model.pkl")

while True:
    temp = psutil.sensors_temperatures()['coretemp'][0].current
    load = psutil.cpu_percent()
    freq = psutil.cpu_freq().current

    X = pd.DataFrame([[temp, load, freq]], columns=["temp", "cpu_load", "freq"])
    predicted = model.predict(X)[0]

    print(f"Current Temp: {temp}°C | Predicted (3s): {predicted:.2f}°C")
    time.sleep(1)
