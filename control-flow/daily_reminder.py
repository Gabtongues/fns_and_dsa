task = input("Enter the task: ")
priority = input("Enter the priority (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")

reminder_message = f"Reminder: {task} - "

match priority.lower():
    case "high":
        reminder_message += "This is a HIGH priority task."
    case "medium":
        reminder_message += "This is a medium priority task."
    case "low":
        reminder_message += "This is a low priority task."
    case _:
        reminder_message += "Priority not recognized."

if time_bound.lower() == "yes":
    reminder_message += " It requires immediate attention today!"


print(reminder_message)
