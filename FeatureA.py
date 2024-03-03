"""
This module provides functionalities to calculate the average velocity of a sprint team based on historical sprint points.
It allows users to input sprint points interactively and calculates the average velocity from these points.

Functions:
- input_sprint_points: Prompts the user to input points for each completed sprint.
- calculate_average_velocity: Calculates the average sprint velocity from a list of sprint points.
- main: The main function of the script, tying together input collection and velocity calculation.
"""

# Subtask A1: Define a Data Structure for Storing Sprint Points
# This will be a simple list to store points from each sprint.
sprint_points = [10, 12, 8, 14]  # Example data

def input_sprint_points():
    """
    Interactively collects sprint points from the user, allowing for dynamic input until 'done' is entered.
    
    Returns:
        list: A list of integers, each representing the points for a completed sprint.
    """
    sprint_points = []
    print("Enter the points for each sprint completed, type 'done' to finish:")
    while True:
        input_point = input("Sprint points: ")
        if input_point.lower() == 'done':
            break
        try:
            points = int(input_point)
            sprint_points.append(points)
        except ValueError:
            print("Please enter a valid integer or 'done' to finish.")
    return sprint_points

def calculate_average_velocity(sprint_points):
    """
    Calculates the average velocity from a given list of sprint points.
    
    Args:
        sprint_points (list): A list of integers representing sprint points.
    
    Returns:
        float: The average velocity, calculated as the total points divided by the number of sprints.
    """
    if not sprint_points:
        return 0.0  # Avoid division by zero if the list is empty.
    total_points = sum(sprint_points)
    number_of_sprints = len(sprint_points)
    average_velocity = total_points / number_of_sprints
    return average_velocity

def main():
    """
    Main function to execute the script functionalities.
    
    It prompts the user to input sprint points, calculates the average sprint velocity based on these points,
    and prints the result to the console.
    """
    sprint_points = input_sprint_points()
    average_velocity = calculate_average_velocity(sprint_points)
    print(f"Average Sprint Velocity: {average_velocity}")

if __name__ == "__main__":
    main()
