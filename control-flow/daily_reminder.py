# daily_reminder.py

# Prompt for task information
task = input("Enter the task: ")
priority = input("Enter the priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

# Initialize the reminder message
reminder_message = f"Reminder: {task} - "

# Use match-case to handle different priority levels
match priority.lower():
    case "high":
        reminder_message += "This is a HIGH priority task."
    case "medium":
        reminder_message += "This is a medium priority task."
    case "low":
        reminder_message += "This is a low priority task."
    case _:
        reminder_message += "Priority not recognized."

# Add time sensitivity if task is time-bound
if time_bound.lower() == "yes":
    reminder_message += " It requires immediate attention today!"

# Print the final customized reminder
print(reminder_message)
