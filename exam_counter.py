#!/usr/bin/env python3

import timer_module
import statistics_module
import plot_results_module 

def main():
    print("Welcome to the Test Application!") # Changed
    
    timer_module.run_timer_application()
    
    statistics_module.run_statistics()
    
    plot_results_module.run_plot_feature() # Using the plotext module as confirmed
    
    print("\nApplication finished.") # Changed

if __name__ == "__main__":
    main()

    

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