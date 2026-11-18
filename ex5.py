
import numpy as np

# Get number of sensor readings
n = int(input("Enter number of sensor readings: "))

# Get sensor values from user
sensor_data = []

for i in range(n):
    value = float(input(f"Enter sensor reading {i + 1}: "))
    sensor_data.append(value)

# Convert list into NumPy array
sensor_data = np.array(sensor_data)

# Display sensor data
print("\nIoT Sensor Data Analysis")
print("-----------------------")

print("Sensor Data:", sensor_data)

# Calculate statistical values
print("Mean :", round(np.mean(sensor_data), 2))
print("Median :", round(np.median(sensor_data), 2))
print("Minimum :", np.min(sensor_data))
print("Maximum :", np.max(sensor_data))
print("Std. Dev. :", round(np.std(sensor_data), 2))

# Find values above threshold
threshold = float(input("\nEnter threshold value: "))

high_values = sensor_data[sensor_data > threshold]

print("Values above", threshold, ":", high_values)
