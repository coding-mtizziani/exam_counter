import json
from datetime import datetime
import os
from typing import Dict, Any, List, Optional

def run_statistics(save_to_file: str="") -> None:
    """
    Collects results from the user, calculates statistics, and saves them.
    """
    print("\n--- Statistics ---")

    total_questions: Optional[int] = None
    while total_questions is None:
        try:
            user_input = input("Enter total number of questions: ") # Changed
            total_questions = int(user_input)
            if total_questions <= 0:
                print("Please enter a positive whole number.") # Changed
                total_questions = None
        except ValueError:
            print("Invalid input. Please enter a whole number.") # Changed

    given_answers: Optional[int] = None
    while given_answers is None:
        try:
            user_input = input("Enter number of answered questions: ") # Changed
            given_answers = int(user_input)
            if given_answers < 0 or given_answers > total_questions:
                print(f"Number of answered questions cannot be negative or exceed {total_questions}.") # Changed
                given_answers = None
        except ValueError:
            print("Invalid input. Please enter a whole number.") # Changed

    correct_answers: Optional[int] = None
    while correct_answers is None:
        try:
            user_input = input("Enter number of correct answers: ") # Changed
            correct_answers = int(user_input)
            if correct_answers < 0 or correct_answers > given_answers:
                print(f"Number of correct answers cannot be negative or exceed {given_answers}.") # Changed
                correct_answers = None
        except ValueError:
            print("Invalid input. Please enter a whole number.") # Changed

    # Calculate overall percentage. Unanswered questions count as incorrect.
    # Total correct answers relative to total possible questions.
    overall_percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0

    print(f"\n{given_answers} out of {total_questions} questions answered, {correct_answers} correct. " # Changed
          f"This is an overall result of {overall_percentage:.2f}%") # Changed

    # Prepare data for saving
    statistic_data: Dict[str, Any] = {
        "timestamp": datetime.now().isoformat(),
        "total_questions": total_questions,
        "given_answers": given_answers,
        "correct_answers": correct_answers,
        "overall_percentage": round(overall_percentage, 2)
    }

    if save_to_file:
        save_results(statistic_data, save_to_file)
    else:
        save_results(statistic_data)
    
    print("--- Statistics Finished ---") # Changed

def save_results(data: Dict[str, Any], filename: str = 'stats.json') -> None:
    """
    Saves a single result entry to a JSON file.
    Appends to the file if it exists, otherwise creates a new one.
    """
    file_exists = os.path.exists(filename)
    file_is_empty = not file_exists or os.path.getsize(filename) == 0

    results: List[Dict[str, Any]] = []

    if file_exists and not file_is_empty:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                results = json.load(f)
            if not isinstance(results, list):
                # If file exists but is not a list, reset it (or handle error)
                print(f"Warning: '{filename}' exists but is not a valid JSON list. Starting with new data.") # Changed
                results = []
        except json.JSONDecodeError:
            print(f"Error decoding JSON from '{filename}'. File might be corrupted. Starting with new data.") # Changed
            results = []
        except IOError as e:
            print(f"Error reading file '{filename}': {e}. Starting with new data.") # Changed
            results = []

    results.append(data)

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4)
        print(f"Results saved to '{filename}'.") # Changed
    except IOError as e:
        print(f"Error saving results to '{filename}': {e}") # Changed

# No change needed to the main guard in this module
if __name__ == "__main__":
    run_statistics(save_to_file='sample_stats.json')  # Example usage


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