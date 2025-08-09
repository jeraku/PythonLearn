task_list=[]
def add_task(task_name, task_description):
    task_list.append([task_name, task_description])
    print(f"task added")
def list_task():
    for index, task_ele in enumerate(task_list):
        print(f"index {index}, task_element is {task_ele} ")

if(__name__=="__main__"):
    add_task("jegan", "jegan_desc")
    add_task("jegan2", "jegan_desc")
    add_task("jegan3", "jegan_desc")
    print("-------------------------")
    list_task()




# dictionary - ordered
# tuple - no ordered
# list - ordered
# set - no duplicate