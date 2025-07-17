task = input("Enter the task: ").lower()
time_bound = input("Is the task time-bound? (yes/no): "),lower()
priority = input("Enter the priority (high/medium/low): ").lower()

reminder_message = ""
match priority:
    case "high":
        reminder_message = f"Reminder: Your '{task}' is a HIGH priority task."
    case "medium":
        reminder_message = f"Reminder: Your '{task}' is a MEDIUM priority task."
    case "low":
        reminder_message = f"Reminder: Your '{task}' is a LOW priority task."
    case _: 
        reminder_message = f"Reminder: Your '{task}' has an UNKNOWN priority."
if time_bound == "yes":
    if reminder_message: reminder_message  += " that requires immediate attention today!"
    else:
        reminder_message = f"your task requires immediate attention today!"
print(reminder_message)
