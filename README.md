# frenz_toolkit_example
This page provides examples to help you get started with using the Frenz Streaming Toolkit.

### **I. Getting started**

You can install the Frenz Streaming Toolkit on your PC using pip:

```bash
pip install frenztoolkit
```

Alternatively, you can download the package and build it from source.

**Product Key Requirement**

A valid product key is required to use the toolkit. Please contact our sales department to obtain your product key.

**System Requirements**

Before using the toolkit, ensure you have the following:

- A Frenz Brainband
- A laptop/desktop (MacOS) with Bluetooth and internet connectivity
- A product key (contact Earable’s sales department if you don’t have one)
- Python 3.9 environment:
### Check if Python 3.9 is installed
```bash
python3.9 --version
```
### Create new virtual environment
```bash
python3.9 -m venv vir_name
```
### Environment activation:
### macOS
```bash
source vir_name/bin/activate  
```
### **I. Example Code**

> ⚠️ **Make sure all dependencies are installed and the environment is activated.**

### 📤 Scanner FRENZ device ID

File: `scanner.py`

**Example Output Device ID:**

```python
["FRENZG15", "DEVICE_2", "DEVICE_3"]
```
---

### 📤 Streaming Data

- Connect to a Frenz Brainband
- Start a session
- Access real-time data
- Stop a session

File: `streaming_data.py`

**Example Output Real-time Data:**

```python
AT TIME:  290.48088693618774
EEG shape: (35379, 6)
PPG shape: (6684, 3)
IMU shape: (14125, 3)
Filtered EEG shape: (4, 34250)
Filtered EOG shape: (4, 34250)
Filtered EMG shape: (4, 34250)
Latest POSTURE: upright
Latest delta_power: [-34.26264236 -35.57368967 -30.60738235 -32.5241039  -33.24195457]
Latest theta_power: [-36.67243783 -39.67207968 -33.32257145 -35.26872573 -36.23395367]
Latest alpha_power: [-38.22353765 -40.95086193 -35.1005497  -37.05063998 -37.83139732]
Latest beta_power: [-34.29642969 -36.17044096 -30.69537941 -32.62457914 -33.4467073 ]
Latest gamma_power: [-37.67633942 -41.05132451 -34.74822132 -36.71283511 -37.54718009]
Latest POAS: 0.15274431585651002
Latest Sleep Stage: 0
Latest Focus Score: 60.4791264419096
Signal Quality Check LF - OTEL - RF - OTER: [1, 0, 1, 1]
```
---

### 📥 Reading and Plotting Data

- Reads raw data from file .dat

File: `reader_raw_data.py`

**Example Output EEG, IMU, PPG Raw Data:**

# Channel description:
# LF: left forehead
# OTEL: over the ear right
# REF1: left reference
# REF2: right reference
# RF: right forehead
# OTER: over the ear left
# GREEN: green LED
# RED: red LED
# INFRARED: infrared LED
# X: x-axis
# Y: y-axis
# Z: z-axis

```python
EEG DATA:
 LF          OTEL        REF1    RF     OTER        REF2
[[-100195.   77583.       0.  -87289.   65165.       0.]
 [-100196.   77548.       0.  -87297.   65085.       0.]
 [-100191.   77648.       0.  -87305.   65195.       0.]
 ...
 [-103974.   71144.       0.  -87340.   58539.       0.]
 [-103986.   71680.       0.  -87331.   58832.       0.]
 [-103989.   71231.       0.  -87336.   58594.       0.]]

--------------------------------

PPG DATA:
  GREEN    RED    INFRARED
[[     0.  85028. 147502.]
 [     0.  85022. 147517.]
 [     0.  85144. 147526.]
 ...
 [     0.  83209. 143922.]
 [     0.  83097. 144005.]
 [     0.  83200. 143946.]]
--------------------------------

IMU DATA:
  X             Y            Z
[[ 634.703125  -47.46875    -9.49375 ]
 [-591.675    -126.175      80.2375  ]
 [-592.440625 -124.64375    84.83125 ]
 ...
 [-604.5375    -84.83125    68.90625 ]
 [-600.55625   -84.525      70.13125 ]
 [-592.746875  -79.93125    69.059375]]
```


- Plots the real-time processed data (Focus score, Sleep stage, PoAS, Posture...)

File: `reader_processed_data.py`

**Example Output Focus Score:**

```python
[40, 40, 40, 40, 40.0, 39.99999999999997, 40.12766772782202, 40.561565017143344, 41.4082156256315, 43.10299038990237, 45.472087116573455, 48.74391187090239, 52.24061530716966, 55.60602305133689, 58.679040962640684, 62.18110934363549, 65.14715231299175, 68.02080813392078, 70.90584790357892, 73.55213246059323, 75.15588285140683, 76.47206224616545, 77.60785020893118, 78.4955176672901, 78.62229982451035, 78.3885666852457, 77.4115503825933, 75.75179777982981, 73.66542059721976, 71.96536767124985, 70.48599527626322, 69.74081135506184, 69.69574827772887, 69.67955939998745, 69.47138500905257, 68.6731180879701, 66.83801060478645, 63.92612785317225, 60.222929411120354, 56.08215648747377, 52.01314753099665, 48.36627998286406, 45.060605588479476, 42.25080500048814, 39.8846423996156, 37.90671187849681, 36.51019137239177, 36.09388113475098, 37.0245762557948, 39.34660640670969, 42.75964145377674, 46.576742345145156, 49.96553650773667, 52.2702299218743, 53.47123615744823, 54.10436210964932, 54.96046849984769, 56.884750140896244, 59.543829922368104, 62.012692934353524, 64.49350372598443, 66.61720332706498, 67.87778789873232, 68.41556392091044, 68.68703561203017]
```
---

## 📚 License & Support

For licensing and support inquiries, please contact **Earable’s sales department**.