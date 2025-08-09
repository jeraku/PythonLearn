task_list=[]
def add_task(task_list,task_name,task_desc):
    task_list.append([task_name,task_desc])
    print("list added")
    save_task(task_list)
def list_task(task_list):
    for index, task in enumerate(task_list):
        print(f"index is {index}, task is {task}")
def save_task(task_list):
    task_file = open("./python/examples/test.txt", "a")
    for task_name,task_desc in task_list:
        test_content= f"{task_name}||{task_desc}\n"
        task_file.write(test_content)
    task_file.close

if(__name__=="__main__"):
    add_task(task_list, "jegan1", "jegan1descj")
    add_task(task_list, "jegan2", "jegan1descj")
    add_task(task_list, "jegan3", "jegan1descj")
    list_task(task_list)
    # save_task()