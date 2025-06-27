import numpy as np
import matplotlib.pyplot as plt
from frenztoolkit.reader import create_charts_from_folder


# Set numpy print options to show full numbers instead of scientific notation
np.set_printoptions(suppress=True, precision=9, linewidth=200)

# Test the new CSV processing API with timezone support
print("=== Testing CSV Processing API with Timezone Support ===")
print("=" * 60)

# Process CSV files in the session_scv_file folder with GMT timezone
# print("\n--- Testing with GMT timezone ---")
# csv_results_gmt = create_charts_from_folder("../session_scv_file", timezone='GMT')

# Process CSV files in the session_scv_file folder with local timezone
print("\n--- Testing with Local timezone ---")
csv_results_local = create_charts_from_folder("sample_csv_file", timezone='local')

# # Process state.json files in the recorded_data folder with GMT timezone
# print("\n--- Testing with GMT timezone ---")
# state_results_gmt = create_charts_from_folder("recorded_data/1750936439.5472288", timezone='GMT')

# Process state.json files in the recorded_data folder with local timezone
print("\n--- Testing with Local timezone ---")
state_results_local = create_charts_from_folder("sample_recorded_file", timezone='local')


print("\n" + "=" * 60)
