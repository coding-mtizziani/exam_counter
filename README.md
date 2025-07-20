# Exam Counter
## including Statistics and Graphical Evaluation

---

## Brief Summary

This Python program offers a flexible countdown timer equipped with optional acoustic warnings at defined remaining times. After the timer expires, it allows for the recording of testing results, including the total number of questions, the actually answered questions, and the correct answers. The program evaluates these inputs and displays a total percentage score, where unanswered questions are counted as incorrect to ensure a realistic performance assessment.

---

## Installation

To set up and run this project, follow these steps:

1.  **Clone the Repository (if applicable):**
    If the project is hosted on a version control system (e.g., GitHub), clone it to your local machine:

    ```bash
    git clone https://github.com/coding-mtizziani/exam_counter.git
    cd exam_conter
    ```

    or download the repository as a ZIP file and extract it to your desired location from [github](https://github.com/coding-mtizziani/exam_counter).

2.  **Create and Activate a Virtual Environment (Recommended):**
    It's best practice to use a virtual environment to manage project dependencies separately from your system's global Python packages.

    * **Create the virtual environment:**
        ```bash
        python -m venv .venv
        ```
        This creates a folder named `.venv` in your project directory.

    * **Activate the virtual environment:**
        * **On Windows:**
            ```bash
            .venv\Scripts\activate
            ```
        * **On macOS / Linux:**
            ```bash
            source .venv/bin/activate
            ```
        You should see `(.venv)` at the beginning of your command prompt, indicating that the virtual environment is active.

3.  **Install Dependencies:**
    With the virtual environment activated, install the required libraries using `pip` and the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

    This command will install all necessary packages (like `plotext`, `keyboard`, `winsound` etc.) into your virtual environment.

---

## Starting the Program
To run the program, ensure your virtual environment is activated and execute the following command in your terminal:

```bash
python exam_counter.py
```

## Functionalities

### 1. Countdown Timer

The core of the program is a customizable countdown timer that helps you manage time for tasks or tests.

* **Runtime Input:** You will be prompted to enter the desired duration of the countdown in minutes. Only positive whole numbers are accepted.
* **Optional Warning Time:** You can set at how many minutes remaining an acoustic and visual warning should occur.
    * Leave the input empty if you do not want a warning.
    * The warning time must be a positive whole number and less than the total runtime. Invalid inputs will be rejected.
* **Dynamic Display:** The timer updates in the console, showing the remaining time in `MM:SS` (Minutes:Seconds) format. Additionally, the option to abort is now displayed throughout the countdown.
* **Variable Update Rate:** To optimize CPU usage, the timer's update rate dynamically adjusts:
    * Over 5 minutes remaining: Updates every 30 seconds.
    * Over 2 minutes remaining: Updates every 10 seconds.
    * 2 minutes or less remaining: Updates every second.
* **Acoustic and Visual Warning:** If the remaining time reaches the defined warning threshold, a one-time acoustic warning (double beep) and a persistent text message will appear in the console.
* **End Alarm:** Once the countdown reaches zero, a more distinct acoustic alarm (five beeps) will be triggered to signal the end of the time.
* **Enhanced Abort Option:** The timer can be terminated prematurely at any time:
    * **Manual Interruption:** Press **`Alt+Q`** to cleanly end the timer and proceed to the next program step. The pressed `Q` will not be written to the console.
    * **Standard Abort:** Press **`Ctrl+C`** to also interrupt the timer. Here too, the system signal is caught, and the program continues cleanly with a corresponding message.
    * After abortion, a shorter alarm sounds, and the program proceeds to the result collection.

### 2. Statistics Collection & Evaluation

After the countdown timer has expired (or if it was not aborted), you will be prompted to enter your test results, which will then be automatically evaluated.

* **Testing Parameter Collection:**
    * **Total Questions:** You enter the total number of questions **possible** in the test (positive whole number).
    * **Answers Given:** You specify how many questions you actually **answered** (positive whole number, must not exceed the total questions).
    * **Correct Answers:** You enter the number of **correct** answers (positive whole number, must not exceed the given answers).
* **Evaluation Logic:**
    * **Unanswered Questions:** Questions that were not answered (Total Questions - Answers Given) are **counted as incorrect** in the final evaluation.
    * **Overall Percentage:** The percentage score is calculated based on the **correct answers relative to the total number of possible questions**.
* **Clear Result Overview:** The program outputs a summary of your performance, e.g.:
    `8 out of 10 questions answered, 6 correct. This is an overall result of 60.00%`

### 3. Graphical Evaluation of Test Results

The program provides a console-based plotting feature for visualizing your test results over time.

* **Development Overview:** The program generates a console graph that displays the percentage test results over time.
* **Chronological Progression:** The X-axis shows the sequence of tests performed (Test No.), while the corresponding timestamps serve as labels for orientation. The Y-axis represents the achieved percentage.

---

## Outlook

This program is designed modularly, allowing the timer component and the test statistics collection to be easily separated and, if necessary, outsourced to separate modules or integrated into other applications.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Issues
If you encounter any issues or bugs, please report them in the [Issues](https://github.com/coding-mtizziani/exam_counter/issues) section of the repository.
## Contact
For any questions or feedback, you can reach me at [coding.maik.tizziani@gmail.com](mailto:coding.maik.tizziani@gmail.com).
## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.