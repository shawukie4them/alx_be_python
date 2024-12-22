# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


match priority:
    case "high":
        priority_message = "high priority task"
    case "medium":
        priority_message = "medium priority task"
    case "low":
        priority_message = "low priority task"
    case _:
        priority_message = "an unknown priority task" 


if time_bound == "yes":
    reminder_message = f"Reminder: '{task}' is a {priority_message} that requires immediate attention today!"
elif time_bound == "no":
    reminder_message = f"Reminder: '{task}' is a {priority_message}. Consider completing it when you have free time."
else:
    reminder_message = "Invalid input for time sensitivity. Please enter 'yes' or 'no'."

print(reminder_message)
