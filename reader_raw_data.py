import numpy as np

channel_eeg = 6
channel_ppg = 3
channel_imu = 3

# Load the recorded session from your experiment folder
memmap_eeg_data = np.memmap('recorded_data/1746519272.376085/eeg.dat', dtype=np.float64, mode='r')
l_eeg = int(len(memmap_eeg_data)//channel_eeg)

memmap_ppg_data = np.memmap('recorded_data/1746519272.376085/ppg.dat', dtype=np.float64, mode='r')
l_ppg = int(len(memmap_ppg_data)//channel_ppg)

memmap_imu_data = np.memmap('recorded_data/1746519272.376085/imu.dat', dtype=np.float64, mode='r')
l_imu = int(len(memmap_imu_data)//channel_imu)

# EEG DATA
# Reshape the data into a 2D array
# l_eeg is the number of samples in the eeg data
# channel_eeg is the number of channels in the eeg data
eeg_data = np.array(memmap_eeg_data)[:l_eeg*channel_eeg].reshape((l_eeg, channel_eeg))

print("\nEEG DATA:\n LF          OTEL        REF1    RF      OTER       REF2")
print(eeg_data)
print("\n--------------------------------")

# PPG DATA
# Reshape the data into a 2D array
# l_ppg is the number of samples in the ppg data
# channel_ppg is the number of channels in the ppg data
ppg_data = np.array(memmap_ppg_data)[:l_ppg*channel_ppg].reshape((l_ppg, channel_ppg))
print("\nPPG DATA:\n GREEN     RED    INFRARED")
print(ppg_data)
print("--------------------------------")

# IMU DATA
# Reshape the data into a 2D array
# l_imu is the number of samples in the imu data
# channel_imu is the number of channels in the imu data
imu_data = np.array(memmap_imu_data)[:l_imu*channel_imu].reshape((l_imu, channel_imu))
print("\nIMU DATA:\n X               Y             Z")
print(imu_data)