task = input("Enter your task:")
priority = input("Enter the task's priority(high,meidum,low):").lower()
time_bound = input("is it time bond?(yes/no):").lower()
match priority:
    case "high":
        reminder_message = f"Reminder: Your '{task}' is a HIGH priority task."
    case "medium":
        reminder_message = f"Reminder: Your '{task}' is a MEDIUM priority task."
    case "low":
        reminder_message = f"Reminder: Your '{task}' is a LOW priority task."
    case _: 
        reminder_message = f"Reminder: Your '{task}' has an UNKNOWN priority."
if time_bound == yes:
    if reminder_message += " that requires immediate attention today!"
    else:
        reminder_message = f"your task requires immediate attention today!"
print(reminder_message)

