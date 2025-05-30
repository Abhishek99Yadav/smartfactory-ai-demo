import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load sample sensor data
df = pd.read_csv("sample_sensor_data.csv")

# Feature columns & target
features = ['temperature', 'vibration', 'pressure']
X = df[features]
y = df['maintenance_required']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Sample Predictions:", predictions[:10])
