Postgres Setup
https://courses.parottasalna.com/database-engineering/installing-postgresql

How to run and connect
Start containers:
bash
1) 
docker compose up -d
2)
Open browser at http://localhost:8080 and log in with:
Email: admin@pgadmin.com
Password: password
3) 
In pgAdmin, add a new server:
Name: anything (e.g. Local Postgres)
Host: postgres (the service name, not localhost)
Port: 5432
Username: admin
Password: password
Database: my_database (or leave blank to use default)

4)

to login form command line.
docker exec -it postgres_db psql -U admin -d my_database
pwd: password

5) docker cp dvdrental.tar 86243781d2cb:/home/dvdrental.tar


6) docker exec -it 86243781d2cb bash > hope its postgres_db 
pg_restore -U admin -d my_database /home/dvdrental.tar


Commands: 
>> \du - list of users.
>> CREATE ROLE sb_developer;
Access to the role
>>  CREATE ROLE jeganlogin with LOGIN Password 'test123';

>> GRANT sb_developer TO jeganlogin
>> GRANT SELECT ON <TableName> to db_developer; 


///// SCHEMA >> ITS a folder like structure.
>> CREATE ROLE analytics_team;
>> GRANT SELECT on ALL TABLES in SCHEMA PUBLIC to analytics_team;
>> ALTER ROLE sb_developer WITH SUPERUSER;

>> GRANT analytics_team to jegan_user;
>> REVOKE analytics_team from jegan_user;

DB level previlages:  Login details
logged in user. RBAC - Role based access control.

Table previlages: Table level details.
select, Insert, update, delete, Trigger, Trancate



/c dbname = To connect ot database.
/l = list database
select current_database(); to show current db
\dt > List of relation
\d <table name> - displays the permission of the table.  
CHECKPOINT;
show WAL_;
show WAL_Buffers;
COMMIT -> record stores in WAL and later writes into disk by checkpointer.
SHOW Sync; > shows synchrosnous COMMIT
SET synchronous_commit = 'off';


| Property    | Meaning                                       | Example                                             |
| ----------- | --------------------------------------------- | --------------------------------------------------- |
| Atomicity   | All-or-nothing transaction                    | Money transfer succeeds completely or not at all    |
| Consistency | Maintains database rules                      | Account balance cannot be negative                  |
| Isolation   | Transactions do not interfere with each other | Two users updating same account see correct results |
| Durability  | Changes persist after commit                  | Deposit remains even after a crash                  |
