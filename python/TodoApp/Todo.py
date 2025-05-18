import datetime
import os
import sys

from numpy import delete

# taskname, taskdescription, duedate, taskstatus, Taskcategory, taskPriority
cwd = os.getcwd()
# fileName= os.path.join(cwd, "TodoApp" , "file.txt")
fileName = os.path.join(cwd, "file.txt")

def add_task(taskList, taskName, taskDescription):
    taskList.append([taskName,taskDescription,datetime.date.today().strftime("%b-%d-%Y"),"PENDING",])
    print(f"Task {taskName} is added successfully.")
    save_task(taskList)

def view_task(taskList):
    if len(taskList) == 0:
        print("Empty To do List")
    for index, task in enumerate(taskList):
        print(f"{index} {task}")

def save_task(taskList):
    task_file = open(fileName, "w")
    for taskName, taskDescription, dueDate, taskStatus in taskList:
        content = f"{taskName}||{taskDescription}||{dueDate}||{taskStatus}\n"
        task_file.write(content)
    task_file.close()

    def load_task(taskList):
    print("-------------load_task-------------------")
    task_file = open(fileName, "r")
    tasks = task_file.readlines()
    for task in tasks:
        task = task.strip().split("||")
        taskList.append(task)
    task_file.close()
    print("--------------------------------")

def delete_task(taskList, taskIndex):
    task = taskList[taskIndex-1]
    taskList.remove(task)
    save_task(taskList)

def update_task(taskList, taskIndex, taskName=None, taskDescription=None, taskStatus=None):
    if taskIndex >= len(taskList):
        print("Invalid task index")
    else:
        task = taskList[taskIndex]
        print(task)
        # print(f" {taskIndex}, {taskName},{taskDescription}, {taskStatus}")
        if taskName != None:
            task[0] = taskName
        if taskDescription != None:
            task[1] = taskDescription
        if taskStatus != None:
            task[3] = taskStatus
        save_task(taskList)

def done_task(taskList, taskIndex):
    task = taskList[taskIndex-1]
    # print(task) 
    # print(taskList) 
    task[3] = "COMPLETED"
    save_task(taskList)
    print("Task is marked as Done")

def help_menu():
    print("""\n📝 Command Line To-Do List
    Usage:
    python Todo.py add  "addTaskName" 'addTaskDescription'     → Add a new task
    python Todo.py view                       → Show all tasks
    python Todo.py update "rowNumber" "addTaskName" 'addTaskDescription'     → Update a new task
    python Todo.py done <task-number>         → Mark task as done
    python Todo.py delete "rowNumber"       → Delete a task
    python Todo.py help                       → Show this help \n """)

taskList = []
load_task(taskList)
# add_task(taskList, "test1", "test1Description")
# add_task(taskList, "test2", "test2Description")
# add_task(taskList, "test3", "test3Description")
# update_task( taskList,3,taskName=None,taskDescription="Updated Description",taskStatus="COMPLETED")
# update_task( taskList,3,taskName="3333333333333",taskDescription="Updated Description",taskStatus="COMPLETED",)
# view_task(taskList)
# save_task(taskList)

if(sys.argv[1]) == "add" and len(sys.argv)==4:
    taskName, taskDescription = sys.argv[2], sys.argv[3]
    add_task(taskList, taskName,taskDescription)
elif(sys.argv[1]) == "update" and len(sys.argv)>3:
    # print(sys.argv[3])
    # print(sys.argv[4])
    # print(sys.argv[2])
    taskIndex, taskName,taskDescription = int(sys.argv[2]), sys.argv[3],sys.argv[4]
    # Todo.py update 3 taskName TaskDescription
    # print(f" {taskIndex}, {taskName},{taskDescription}, {taskStatus}")
    update_task(taskList,taskIndex,taskName,taskDescription)
elif(sys.argv[1]) == "delete" and len(sys.argv)==3:
    taskIndex = int(sys.argv[2])
    delete_task(taskList, taskIndex)
elif(sys.argv[1]=="done" and len(sys.argv)==3):
    taskIndex= int(sys.argv[2]) 
    done_task(taskList, taskIndex)
elif sys.argv[1] == "view":
    view_task(taskList)
elif sys.argv[1] == "help":
    help_menu()
