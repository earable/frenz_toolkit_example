import numpy as np
import matplotlib.pyplot as plt
from frenztoolkit.reader import load_experiment

# Load the recorded session from your experiment folder
# find the folder contains your recorded data by timestamp
session_data = load_experiment("./recorded_data/1746436416.925101")

# Access EEG and Focus score history
eeg = session_data["DATA"]["RAW"]["EEG"]
print(eeg.shape)
focus_list = session_data["SCORE"]["array__focus_score"]
# print(focus_list.shape)
start_time = session_data["SCORE"]["start_time"]
print(start_time)
# Plot the Focus score over time
plt.plot(np.array(focus_list).flatten())
plt.title("Focus Score Over Time")
plt.xlabel("Time Steps")
plt.ylabel("Focus Score (0–100)")
plt.grid(True)
plt.show()