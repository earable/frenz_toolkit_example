from frenztoolkit import Streamer
import time
import matplotlib.pyplot as plt

# Initialize the streamer with your device ID and product key
streamer = Streamer(
    device_id="FRENZXX",
    product_key="YYY",
    data_folder="./recorded_data",
    turn_off_light=True,
)

# Start the streaming session
streamer.start()
try:
    while True:
        if streamer.session_dur > 20*60:
            break

        eeg = streamer.DATA["RAW"]["EEG"]
        ppg = streamer.DATA["RAW"]["PPG"]
        imu = streamer.DATA["RAW"]["IMU"]
        delta_power = streamer.SCORES.get("delta")
        theta_power = streamer.SCORES.get("theta")
        alpha_power = streamer.SCORES.get("alpha")
        beta_power = streamer.SCORES.get("beta")
        gamma_power = streamer.SCORES.get("gamma")
        posture = streamer.SCORES.get("posture")
        poas = streamer.SCORES.get("poas")
        sleep_stage = streamer.SCORES.get("sleep_stage")
        focus_score = streamer.SCORES.get("focus_score")
        sqc_scores = streamer.SCORES.get("sqc_scores")

        print("AT TIME: ", streamer.session_dur)
        print("EEG shape:", eeg.shape)
        print("PPG shape:", ppg.shape)
        print("IMU shape:", imu.shape)
        print("Filtered EEG shape:", streamer.DATA["FILTERED"]["EEG"].shape)
        print("Filtered EOG shape:", streamer.DATA["FILTERED"]["EOG"].shape)
        print("Filtered EMG shape:", streamer.DATA["FILTERED"]["EMG"].shape)
  
        print("Latest POSTURE:", posture)
        # print("List of POSTURE:", streamer.SCORES.get("array__posture"))

        print("Latest delta_power:", delta_power)
        # print("List of Delta Power:", streamer.SCORES.get("array__delta"))
        print("Latest theta_power:", theta_power)
        # print("List of Theta Power:", streamer.SCORES.get("array__theta"))
        print("Latest alpha_power:", alpha_power)
        # print("List of Alpha Power:", streamer.SCORES.get("array__alpha"))
        print("Latest beta_power:", beta_power)
        # print("List of Beta Power:", streamer.SCORES.get("array__beta"))
        print("Latest gamma_power:", gamma_power)
        # print("List of Gamma Power:", streamer.SCORES.get("array__gamma"))

        print("Latest POAS:", poas)
        # print("List of POAS:", streamer.SCORES.get("array__poas"))

        print("Latest Sleep Stage:", sleep_stage)
        # print("List of Sleep Stage:", streamer.SCORES.get("array__sleep_stage"))

        print("Latest Focus Score:", focus_score)
        # print("List of Focus Score:", streamer.SCORES.get("array__focus_score"))

        print("Signal Quality Check LF - OTEL - RF - OTER:", sqc_scores)
        # print("List of Signal Quality Check:", streamer.SCORES.get("array__sqc_scores"))
        print("\n")

        time.sleep(5)
except KeyboardInterrupt:
    print("Keyboard interrupt")
    streamer.stop()
except Exception as e:
    print(f"Error: {e}")
    streamer.stop()
# Stop the session and save data to disk
streamer.stop()