import json
import os
import plotext as plt
from datetime import datetime
from typing import List, Dict, Any

def load_test_results(filename: str = 'stats.json') -> List[Dict[str, Any]]:
    """
    Loads test results from the JSON file.
    Returns a list of dictionaries.
    """
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return []
    
    if os.path.getsize(filename) == 0:
        print(f"Error: File '{filename}' is empty.")
        return []

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                print(f"Warning: '{filename}' does not contain a JSON list. Loading no data.")
                return []
            return data
    except json.JSONDecodeError:
        print(f"Error: '{filename}' is not a valid JSON file.")
        return []
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
        return []

def plot_overall_percentage(results: List[Dict[str, Any]]) -> None:
    """
    Plots the overall percentage of test results in the console.
    """
    if not results:
        print("No results available to plot.")
        return

    timestamps_dt: List[datetime] = []
    percentages: List[float] = []
    
    for entry in results:
        try:
            dt_object = datetime.fromisoformat(entry["timestamp"])
            timestamps_dt.append(dt_object)
            percentages.append(entry["overall_percentage"])
        except (ValueError, KeyError) as e:
            print(f"Warning: Invalid data entry skipped - {entry}. Error: {e}")
            continue

    if not timestamps_dt or not percentages:
        print("Not enough valid data available to plot.")
        return

    sorted_data = sorted(zip(timestamps_dt, percentages), key=lambda x: x[0])
    sorted_timestamps_dt, sorted_percentages = zip(*sorted_data)

    test_indices = list(range(len(sorted_percentages)))

    print("\n--- Sorted Data (Test Index, Timestamp, Percentage) ---")
    for i in range(len(test_indices)):
        print(f"Test {test_indices[i]+1}: {sorted_timestamps_dt[i].isoformat()}, Percentage: {sorted_percentages[i]:.1f}%")
    print("------------------------------------------")

    plt.clf()

    plt.plot(test_indices, list(sorted_percentages), 
             label="Overall Percentage", marker="hd", color="cyan")
    
    tick_positions = []
    tick_labels = []
    
    step = max(1, len(test_indices) // min(len(test_indices), 5))
    
    for i in range(0, len(test_indices), step):
        tick_positions.append(test_indices[i])
        tick_labels.append(sorted_timestamps_dt[i].strftime("%d.%m. %H:%M"))

    if (len(test_indices) - 1) % step != 0 and len(test_indices) > 0:
        tick_positions.append(test_indices[-1])
        tick_labels.append(sorted_timestamps_dt[-1].strftime("%d.%m. %H:%M"))

    plt.xticks(tick_positions, tick_labels)
    
    plt.title("Development of Test Results")
    plt.xlabel("Test No. (Date and Time of Test)")
    plt.ylabel("Percentage (%)")
    plt.grid(True)
    plt.canvas_color("default")
    plt.axes_color("default")
    plt.ticks_color("default")
    
    plt.ylim(0, 100) 
    
    plt.show()

def run_plot_feature(filename: str = 'stats.json') -> None:
    """
    Loads test results and plots the overall percentage in the console.
    This is the main function to call from outside.
    """
    print(f"\n--- Plotting Test Results from '{filename}' ---")
    results = load_test_results(filename)
    plot_overall_percentage(results)
    print("--- Plotting finished ---")

if __name__ == "__main__":
    run_plot_feature()



# Copyright 2025 Maik Tizziani
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.