import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load collected CPU data
df = pd.read_csv("cpu_data.csv")

# Predict temperature 3 seconds ahead
df["future_temp"] = df["temp"].shift(-3)
df.dropna(inplace=True)

X = df[["temp", "cpu_load", "freq"]]
y = df["future_temp"]

# Train regression model
model = LinearRegression()
model.fit(X, y)

# Save trained model
joblib.dump(model, "thermal_model.pkl")

print("Thermal prediction model trained successfully")
