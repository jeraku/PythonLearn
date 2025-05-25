import redis 
r = redis.Redis(host="localhost", port=6379, db=0)

def add_task(task):
    r.lpush("task_queue", task)
    print(f"task has been added successfully {task}")

def list_task():
    tasks = r.lrange("task_queue", 0, -1)
    print("printing current tasks")
    for id, task in enumerate(tasks):
        print(f" task id is {id} and task value is {task}")
    return tasks

def remove_task():
    removed = r.lem()