# daily_reminder.py

def get_task_details():
    # Asks user for task description
    task = input("Enter your task: ")

    # Asks for the task's priority level (high, medium, low)
    priority = input("Priority (high/medium/low): ").lower()

    # Asks if the task is time-sensitive (yes/no)
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    return task, priority, time_bound

def process_task_reminder(task, priority, time_bound):
    # Starts constructing the reminder message
    if time_bound == "yes":
        time_message = "requires immediate attention today!"
    else:
        time_message = "Consider completing it when you have free time."

    # Creates a message based on priority using match-case
    match priority:
        case 'high':
            reminder = f"Reminder: '{task}' is a high priority task that {time_message}"
        case 'medium':
            reminder = f"Reminder: '{task}' is a medium priority task that {time_message}"
        case 'low':
            reminder = f"Reminder: '{task}' is a low priority task that {time_message}"
        case _:
            reminder = "Invalid priority level."

    return reminder

def main():
    task, priority, time_bound = get_task_details()
    
    # Prints the customized reminder based on the task's details
    reminder = process_task_reminder(task, priority, time_bound)
    print(reminder)

if __name__ == "__main__":
    main()
