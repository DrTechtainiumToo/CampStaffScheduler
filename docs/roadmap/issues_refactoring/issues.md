# Issues 🐛⚠️

## Known Bugs & Problems

1. **Time Measurement Bug**  
   - **Summary**: The entire system heavily depends on time slot logic, but we lack a clear, documented approach to how time is structured.
   - **Impact**: Confusion around end slots, boundary conditions, and scheduling conflicts.
   - **Proposed Fix**: Create a single, centralized “time system” reference or module with detailed documentation.

2. **Unavailability from Min to Max**  
   - **Summary**: When setting unavailability from a start to an end slot, the last slot is excluded.
   - **Impact**: Employees might be incorrectly scheduled for the end slot.
   - **Proposed Fix**: Adjust logic to include end times or create an “all day” flag to handle day-long unavailability.

3. **KeyError: `None`**  
   - **Summary**: Occurs in scheduling logic when `next_time_slot_key` returns `None`.
   - **Impact**: Crashes or halts scheduling sequence.
   - **Proposed Fix**: Add checks before calling `self.time_slot_task_queues[next_time_slot_key]`.

4. **Potential Overuse of Certified Employees**  
   - **Summary**: Tasks without special requirements sometimes consume certified employees who are needed later.
   - **Impact**: Scheduling becomes inefficient, requiring manual fix-ups.
   - **Proposed Fix**: Add a “lookahead” or priority check to keep specialized staff available for upcoming critical tasks.

5. **CSV Data Handling Gaps**  
   - **Summary**: Missing columns or malformed CSV can cause parsing errors or incomplete tasks.
   - **Impact**: Crash or incomplete schedule building.
   - **Proposed Fix**: Validate CSV structure before importing (log warnings, skip rows if needed).

