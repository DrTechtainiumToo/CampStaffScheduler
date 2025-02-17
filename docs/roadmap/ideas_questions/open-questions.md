# Open Questions ❓🔍

1. **Night Chore Scheduling**
   - Should we set night chores by a specific time block, or trigger them after "sweeting"?
   - Could the front-end handle both settings, letting users choose?

2. **Timeslot Logic**
   - How do we handle edge slots (e.g., 11:30 PM – 12:00 AM)? 
   - Do we adopt military time or keep named slots (e.g., `Evening1`, `Night2`)?

3. **Role-Based Access Control**
   - Will we have multiple user types (admin vs. staff)? 
   - Do we need to restrict certain scheduling fields to admins only?

4. **Concurrency & Real-Time Updates**
   - If multiple users edit tasks simultaneously, do we need conflict resolution or locking?

5. **Bulk Editing Interface**
   - Is it mandatory to have multi-task editing from day one, or can this be a future add-on?

6. **Internationalization & Time Zones**
   - Will this system be used in multiple regions? 
   - Do we need time zone awareness or language localization?
