import redis
import time

r=redis.Redis(host="localhost", port=6379,db=0)
jobs=[
    "HARshitha", "Harshitha", "HARshithaSuba"
]

for job in jobs:
    r.lpush("task_queue", job)
    print(f"producer: {job}")   
    time.sleep(1)

# ///////////// consumer//////////////

print("[Consumer] Waiting for jobs...")
while True:
   job = r.brpop("task_queue",timeout =2)
   print(job)
   if job:
       queue_name, job_data = job
    #    print(f"{queue_name} and {job_data}")
       print(f"[Consumer] Processing job: {job_data.decode()}")
       time.sleep(2)
