import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_sensor_data.csv")

# Group by health status
status_counts = df['machine_status'].value_counts()

# Plot
status_counts.plot(kind='bar', color=['green', 'orange', 'red'])
plt.title("Machine Health Status Overview")
plt.xlabel("Status")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
