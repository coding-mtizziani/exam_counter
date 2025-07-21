import time
import winsound
import os
import keyboard # For Alt+Q detection
import threading # For non-blocking Alt+Q listener
from typing import Optional

def play_sound(frequency: int, duration: int) -> None:
    """Plays a sound using winsound."""
    if os.name == 'nt': # Only available on Windows
        winsound.Beep(frequency, duration)
    else:
        # Fallback for non-Windows (e.g., Linux, macOS), might require external tools like 'beep' or 'play'
        # For simplicity, we'll just print a message.
        print(f"\n[Sound: Beep at {frequency} Hz for {duration} ms]\n")

def run_timer_application() -> None:
    """Runs the main timer application."""
    print("\n--- Countdown Timer ---")

    timer_minutes: Optional[int] = None
    while timer_minutes is None:
        try:
            user_input = input("Enter countdown duration in minutes (e.g., 25): ")
            timer_minutes = int(user_input)
            if timer_minutes <= 0:
                print("Please enter a positive whole number for minutes.")
                timer_minutes = None
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    warning_minutes: Optional[int] = None
    while True:
        try:
            user_input = input(
                f"Enter warning time in minutes (e.g., 5, leave empty for no warning): "
            )
            if user_input == "":
                warning_minutes = None
                break
            
            warning_minutes = int(user_input)
            if warning_minutes <= 0 or warning_minutes >= timer_minutes:
                print(f"Warning time must be a positive whole number and less than {timer_minutes} minutes.")
                warning_minutes = None
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number or leave empty.")

    remaining_seconds = timer_minutes * 60
    warning_threshold_seconds = warning_minutes * 60 if warning_minutes is not None else -1

    last_print_time = 0
    warning_sound_played = False
    
    print("\nStarting countdown... (Press Alt+Q to stop prematurely)")

    abort_event = threading.Event()

    # Function to listen for Alt+Q
    def listen_for_abort():
        keyboard.add_hotkey('alt+q', abort_event.set)
        abort_event.wait() # Wait until the event is set
        keyboard.remove_hotkey('alt+q')

    abort_listener_thread = threading.Thread(target=listen_for_abort, daemon=True)
    abort_listener_thread.start()

    try:
        while remaining_seconds >= 0:
            if abort_event.is_set():
                print("\nTimer terminated prematurely by key press.")
                break

            current_time = time.time()
            # Dynamic update rate
            if remaining_seconds > 5 * 60:
                update_interval = 30
            elif remaining_seconds > 2 * 60:
                update_interval = 10
            else:
                update_interval = 1

            if current_time - last_print_time >= update_interval or remaining_seconds == 0:
                mins, secs = divmod(remaining_seconds, 60)
                print(f"\rRemaining Time: {mins:02d}:{secs:02d}", end="", flush=True)

                # Warning
                if warning_minutes is not None and remaining_seconds == warning_threshold_seconds and not warning_sound_played:
                    print(f"\nWarning: {warning_minutes} minutes remaining!")
                    play_sound(1000, 200) # Short beep
                    play_sound(1000, 200) # Another short beep
                    warning_sound_played = True

                last_print_time = current_time
            
            time.sleep(1) # Sleep for 1 second, but allow keyboard input during this
            remaining_seconds -= 1

        print("\n--- Time EXPIRED! (Countdown finished) ---") if not abort_event.is_set() else None
        if abort_event.is_set():
            play_sound(500, 150) # Short beep for abort
        else:
            # End alarm
            for _ in range(5):
                play_sound(800, 300) # Longer beep
                time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n--- Time EXPIRED! (Aborted) ---")
        play_sound(500, 150) # Short beep for abort
    finally:
        print("\nCountdown finished (prematurely)." if abort_event.is_set() or "KeyboardInterrupt" in locals() else "\nCountdown finished.")
        # Clean up hotkey if thread is still running and not explicitly stopped by abort_event
        if abort_listener_thread.is_alive():
            keyboard.remove_hotkey('alt+q')


# No change needed to the main guard in this module
if __name__ == "__main__":
    run_timer_application()



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