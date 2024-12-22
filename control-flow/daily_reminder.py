# daily_reminder.py

def get_task_details():

    task = input("Enter your task: ")


    priority = input("Priority (high/medium/low): ").lower()


    time_bound = input("Is it time-bound? (yes/no): ").lower()

    return task, priority, time_bound

def process_task_reminder(task, priority, time_bound):

    match priority:
        case 'high':
            reminder = f"Reminder: '{task}' is a high priority task"
        case 'medium':
            reminder = f"Reminder: '{task}' is a medium priority task"
        case 'low':
            reminder = f"Reminder: '{task}' is a low priority task"
        case _:
            reminder = "Invalid priority level."


    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    return reminder

def main():
    task, priority, time_bound = get_task_details()

    reminder = process_task_reminder(task, priority, time_bound)
    print(reminder)

if __name__ == "__main__":
    main()
