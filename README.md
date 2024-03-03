# ACS_HW6
Sprint Plan & Execution

# Sprint Planning and Execution - Feature A and B

## Feature A: Calculate a Sprint Team’s Velocity

### Code Logic
- The logic behind this feature involves collecting an array of integers, where each integer represents the points completed in a previous sprint. The average of these points is then calculated to determine the team's average velocity.

### Inputs
- **Sprint Points (Array of Integers):** Each integer in the array represents the sprint points completed in a previous sprint. These are historical data points indicating the output of the team for each past sprint.

### Output
- **Average Velocity (Float):** A single float value representing the average sprint velocity, which is the average rate of work the team can accomplish in a sprint. This metric is used for planning and forecasting future sprints.

## Feature B: Calculate Team Effort-Hour Capacity

### Code Logic
- This feature requires inputting each team member's details regarding their availability and commitments during the sprint. The available effort-hours per person are calculated by subtracting the hours taken off (PTO) and hours committed to sprint ceremonies from the total hours available, which is the sprint days multiplied by daily hours. The effort-hours for all team members are then summed to find the total team effort-hours.

### Inputs
- **Number of Sprint Days (Integer):** The total number of days in the sprint.
- **Team Member Details (List of Dictionaries):**
  - **PTO (Paid Time Off in Hours):** The number of hours a team member is taking off during the sprint.
  - **Sprint Ceremonies (Hours):** The number of hours a team member will spend in sprint-related ceremonies.
  - **Daily Hours (Hours/Day):** The number of hours per day a team member is available to work on sprint tasks.

### Outputs
- **Available Effort-Hours/Person (Float):** The total number of hours each team member is available to contribute to sprint tasks accounting for PTO and ceremony commitments.
- **Available Effort-Hours for Team (Float):** The sum of all available effort-hours from all team members, providing a total capacity for what the team can accomplish in terms


