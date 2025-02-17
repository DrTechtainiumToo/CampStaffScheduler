# Backlog 📌📋

A list of tasks/features not yet started or assigned.

- [ ] **Implement “Unavailable All Day” Feature**  
  - Expand the “unavailability” logic to handle an entire day as blocked out.

- [ ] **Add Future Unavailability Check for Tasks**  
  - Ensure tasks are validated against employee future unavailability.

- [ ] **Create Save System for Preference Data**  
  - Avoid storing everything repeatedly in `defaultInfo`, possibly use CSV or JSON with a dedicated converter.

- [ ] **Auto-Generate Employee IDs**  
  - Unique ID assignment upon employee creation.  
  - Use IDs in tasks and logs for clarity.

- [ ] **Batch Editing of Tasks in UI**  
  - Ability to multi-select tasks and apply changes (e.g., tier, day-of-week) in one go.

- [ ] **Implement Weighted Probability for Employee Assignments**  
  - Use preference + future task needs to decide who gets assigned.

- [ ] **Consolidate All Time & Special Events**  
  - Finalize a consistent config for time blocks, special events, or holidays.

- [ ] **Printing & Formatting Options for Excel**  
  - Increase timeslot cell size, set consistent margins, manage color fills, etc.

- [ ] **Logging & QA Strategy**  
  - Clarify plan for unit tests, integration tests, and user acceptance testing.
