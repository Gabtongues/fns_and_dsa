
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unknown priority level"


if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message = message.replace("Reminder", "Note")
    message += ". Consider completing it when you have free time."

message = f"Reminder: '{task}' ..."
print(message)

