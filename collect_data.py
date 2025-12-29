import time
import psutil
import pandas as pd

data = []

print("Collecting CPU data... Press Ctrl+C to stop")

try:
    while True:
        temp = psutil.sensors_temperatures()['coretemp'][0].current
        cpu_load = psutil.cpu_percent()
        freq = psutil.cpu_freq().current

        data.append([temp, cpu_load, freq])
        print(f"Temp: {temp}°C | Load: {cpu_load}% | Freq: {freq} MHz")

        time.sleep(1)

except KeyboardInterrupt:
    df = pd.DataFrame(data, columns=["temp", "cpu_load", "freq"])
    df.to_csv("cpu_data.csv", index=False)
    print("\nData saved to cpu_data.csv")

