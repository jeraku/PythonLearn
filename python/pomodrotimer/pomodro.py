import time
import sys
import os
import requests
from plyer import notification
DEFAULT_POMODORO_TIME = 2
DEFAULT_SHORT_BREAK_TIME = 1
DEFAULT_LONG_BREAK_TIME = 1
DEFAULT_CYCLE_FOR_LONG_BREAK = 2

def clear_window():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def time_run(minutes):
    """Runs a countdown timer for the specified minutes."""
    total_sec = minutes * 60
    total_sec=10
    while total_sec:
        minutes_left = total_sec // 60
        seconds_left = total_sec % 60
        print(f"\rTotal time left: {minutes_left:02d}:{seconds_left:02d}", end="")
        time.sleep(.1)
        total_sec -= 1
    print("\nTime's up!")

def pomodoro_timer(tasks):
    """Runs the Pomodoro timer with cycles and breaks."""
    cycle = 1
    task_counter=0

    while cycle<len(tasks):
        print(f"\nStarting Pomodoro for task: {tasks[task_counter]}")
        time_run(DEFAULT_POMODORO_TIME)

        if cycle < DEFAULT_CYCLE_FOR_LONG_BREAK:
            print("\nShort break started")
            time_run(DEFAULT_SHORT_BREAK_TIME)
            task_counter+=1
        else:
            print("\nLong break started")
            time_run(DEFAULT_LONG_BREAK_TIME)
            print("\nPomodoro session completed!")
            task_counter+=1
            sys.exit()

        cycle += 1
        print(f"\nNext Pomodoro cycle: {cycle}")

def notify():
    notification.notify(title="pomodorotest", message="test Notifcaiton", timeout=10)
    requests.post("https://ntfy.sh/pyclass_test", data="test message fro pomodoro.py")
def get_task():
    """Prompts the user for a task name."""
    is_task=True
    tasks=[]
    while is_task:
        task = input("Enter your task name: ")
        tasks.append(task)
        any_more_task=input("do you have any task Y/N:")
        if any_more_task.strip().lower()=="n":
            is_task=False
    return tasks

def main():
    """Main function to start the Pomodoro timer."""
    tasks = get_task()
    pomodoro_timer(tasks)
    print("notift")
    notify()
    print("notiftasdf")

if __name__ == "__main__":
    print("mainsss")
    main()