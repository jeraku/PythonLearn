import datetime
import os
import sys
# taskname, taskdescription, duedate, taskstatus, Taskcategory, taskPriority
cwd=os.getcwd()
# fileName= os.path.join(cwd, "TodoApp" , "file.txt")
fileName= os.path.join(cwd , "file.txt")

def add_task(taskList,taskName,taskDescription):
    taskList.append([taskName, taskDescription, datetime.date.today().strftime("%b-%d-%Y"), "PENDING"])
    print(f"Task {taskName} is added successfully.")
    save_task(taskList)

def view_task(taskList):
    if(len(taskList)==0):
        print("Empty To do List")
    for index,task in enumerate(taskList):
        print(f"{index} {task}")

def save_task(taskList):
    task_file=open(fileName,"w")
    for taskName, taskDescription, dueDate, taskStatus in taskList:
        content=f"{taskName}||{taskDescription}||{dueDate}||{taskStatus}\n"
        task_file.write(content)
    task_file.close()

def load_task(taskList):
    print("-------------load_task-------------------")
    task_file= open(fileName,"r")
    tasks= task_file.readlines()
    for task in tasks:
        task = task.strip().split("||")
        taskList.append(task)
    task_file.close()
    print("--------------------------------")

# def delete_task(taskList):
    # for task in taskList:
def update_status(taskList,taskIndex,taskStatus):
    task=taskList[taskIndex]
    task[3] = taskStatus
    print(taskList)
    save_task(taskList)
    
taskList=[]
load_task(taskList)
# add_task(taskList, "test1", "test1Description")
# add_task(taskList, "test2", "test2Description")
# add_task(taskList, "test3", "test3Description")

if(sys.argv[1]) == "add" and len(sys.argv)==4:
    taskName, taskDescription = sys.argv[2], sys.argv[3]
    add_task(taskList, taskName,taskDescription)
elif(sys.argv[1]) == "updatestat" and len(sys.argv)>3:
    # taskName, taskDescription = sys.argv[2], sys.argv[3]
    # update_task(taskList, taskName,taskDescription)
    taskIndex, taskStatus = int(sys.argv[2]), sys.argv[3]
    update_status(taskList,taskIndex,taskStatus)
elif sys.argv[1] == "view":
    view_task(taskList)

# view_task(taskList)
# save_task(taskList)

