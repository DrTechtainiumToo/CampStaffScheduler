
# **✅ Completed Tasks List**  

# Done Tasks ✅🏁

1. **Standardized Font & Style in Excel**
   - Implemented auto-sizing, consistent font, and basic color schemes.

2. **Initial Program Flow Setup**
   - Created main UI flow for date input, schedule modification, and basic scheduling.

3. **Basic Employee Availability**
   - Added front-end inputs for setting unavailability blocks.
   - Merged data into scheduling logic.


## **📌 General / Miscellaneous**  
- ✅ **Editor Improvements**: Remove incomplete tasks that take remaining slots and require user input from the display.  
- ✅ **Sorting Optimization**: Sorted objects and durations together using dictionaries to improve efficiency.  
- ✅ **Bug Fix**: Windowed tasks weren’t updating unless the queue was prematurely full—fixed by adding them to the list earlier.  
- ✅ **Encoding Issue Fix**: Solved `\ufeff` problem by adding an encoding parameter to `open()`.  
  ```python
  employee_names.append(name)  # Add names to list
  ```
- ✅ **Unavailability Handling**: Now properly tracks unavailable employees.  
- ✅ **Edge Case Handling**: Improved handling of previously problematic cases.  
- ✅ **Privatized Nested Functions**: Converted applicable nested functions to private methods.  
- ✅ **Data Structure Optimization**: Converted unnecessary dictionaries to sets for faster lookups.  
- ✅ **Performance Boost**: Replaced list membership tests with set-based lookups.  

---

## **🧠 Algorithm Improvements**  
- ✅ **Multi-Timeblock System**: Supports tasks spanning multiple time blocks.  
- ✅ **Master Roster Integration**: Merged all input data into a master roster for scheduling.  
  - ✅ **Sorting & Data Arrangement**: Prepares structured data before selection.  
  - ✅ **Anti-Overlap System**: Prevents task conflicts.  
  - ✅ **Multi-Time Windowed Tasks**: Properly handles windowed tasks.  
  - ✅ **Unavailability Displayer**: Displays unavailability dynamically.  
- ❌ **Console Output Formatting**: **Scrapped** – not needed for final implementation.  
- ✅ **Algorithm Validation**:  
  - **Checked behavior when leaving "Frequency" column empty** (defaults correctly to `1`).  
  - **Verified duration handling** in the algorithm.  
  - **Tested gender requirements & min number of people logic** for edge cases.  
  - **Handled exceptions properly** for missing or invalid data.  

---

## **📊 Excel Output**  
🚧 *(No completed tasks listed, potentially pending development?)*  

---

## **⚙️ Settings Improvements**  
- ✅ **Refactored Settings Storage**: Created a **dictionary** for all configuration variables (including Excel-related ones).  
- ✅ **Unpacked Configuration Variables**: Extracted settings dynamically for easier function calls.  

---

## **🖥️ GUI Development**  
🚧 *(No completed tasks listed, potentially pending development?)*  

---

## **🔧 Backend Improvements**  
- ✅ **Trait-Based Employee Filtering**: Only retrieves employees with specific traits **who are also available**.  
- ✅ **Time System Enhancements**:  
  - Handles **input blocks or time/date-based** scheduling.  
  - Implemented a **smart function** to calculate duration based on two time values.  
  - Built **CSV readers & converters** to standardize inputs.  
- ✅ **Task Requirements Handling**: Can now determine if a task has **no eligible people** due to missing requirements.  
- ✅ **Unavailability Tracking**:  
  - Supports **individual unavailability**.  
  - Handles **all-day unavailability** by refactoring the system to be **attribute-based**.  
- ✅ **Master Task List**: Created and populated an **initial list of tasks** (80% complete).  

---

## **📂 Data Management**  
- ✅ **Night Chore Data Structure**: Created a **list and supporting data structures** for night chores.  
- ✅ **CSV Parameterization**: Converted **column values from the tasks CSV into keyword arguments** for the `Task` class.  
- ✅ **Night Chores Handling**: Evaluated whether night chores should have a **separate dictionary** and determined the best approach for assignment.  
- ✅ **DefaultInfo CSV Overhaul**:  
  - **Refactored file storage & retrieval logic**.  
  - **Added a gender column** for improved sorting.  

---