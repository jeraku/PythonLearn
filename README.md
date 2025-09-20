# PythonLearn
My github repo.
https://github.com/jeraku/PythonLearn/tree/myfirstproject


Plan:
packaging: Venv
DB: Postgres DB
<!-- Frontend: Django flask -->
backed API: Fast API
<!-- cache mechanism: redis cache
pydantic model -->

Step1 : 
check for test.py worked properly once the initial setup is completed.

Step 2: 
Venv setpup for packaging
go to the project path. 

>> python -m venv venv
>> ./venv/Scripts/activate   --------- command for activation
>> source ./venv/Scripts/activate   --------- command for activation in git bash

To confirm venv step up is fine.
>> pip install pandas
>> pip freeze > requirements.txt

for cleanup unused packages.
>> pip install pipreqs
>> pipreqs /path/to/your/project

>> pip install -r requirement.txt ------ for installing from the requirements.txt file
>> deactivate ----------- command for deactivation
Note: I tried in command shell and worked.

Step 3: DB information (Plan via docker steup)
data store from DB - How to achieve step by step.
>> docker ps
precondition: Create docker-compose.yaml file and docker volumes to be created
>> docker-compose up -d  --------- docker compose down
>> http://localhost:8081/login
Login with jegan@admin.com and admin and register with the below connection
![alt text](image.png)

DB validation:
>> docker exec it <containername> sh
>> psql -U admin -d mydatabase
>> \dt \l \du

<!-- to check mount values - to be checked -->
**
To check for the mount values.**
- Verify the bind mount in your container
docker inspect postgres
- Look for "Mounts" → "Source": "C:\\jegan\\automation\\myLocal\\local"

<!------------------working one-------------------->
For backup in your local
docker exec -t postgres_c pg_dumpall -c -U admin > backup_today.sql

restore the backup:
cat backup_today.sql | docker exec -i postgres_c psql -U admin -d mydatabase

<!------------------alternate option in zip format-------------------->

PS C:\jegan\automation\github_J\PythonLearn\backup> .\backup_shell_program.ps1
PS C:\jegan\automation\github_J\PythonLearn\backup>

<!-------------------------------------->

Step 4: 
>> pip install fastapi uvicorn pydantic psycopg2-binary redis

