### POSTGRES WAL Turn Off
Logs gets stored in DB if it fails then it will not have an issue
so team will turn off the wal writer

Postgres WAL turn off
for faster writing the data in postgres DB.

Write ahead layer.
Unlogged table - so that we can turn off the WAL

1 client - 10 connection -> PGBOUNCER

### Redis Memory
Its a in memory DB, stores like a key-value pair

we can store the value of 500 MB.

we store the retrieve the details from cache. so we will get a faster response.

Its stores the value from RAM.

When to use -> mostly If the data is a static and repeatable details then go for the Redis DB.

Normal flow

Client -> Server -> DB (PostGres) 

Redis flow

Client -> Server -> DB Redis (In memory DB)

Flow with in-memory DB will take O(1) response time which is always a constant time.



We can use the DB usecases like 

streaming,

Geospatial

Pubsub connection.

Rich data structures.

Cache.

supports JSON.



term used like business object cache memory.



Query:

we can use like a normal DB query??

yes, we can use the redis with similar SQL query.


Redis installation.

I am using windows so I will be using the .exe for installation

best options is go from docker, so you can use for safely.



After connecting to redis.

we have a logical spaces. 0-9 limit, by default space is 0. its basically its a schema. 

Default space will be like you can use it for creating tables and public schema.



limit is 0-9     

Its a single threaded application and written in C programming language.

If you are storing the data in this DB then you need to use the command like GET and SET

commands you can try.

>> SET name "Jegan"

>> GET name

To view all the keys, try the below command.

>> KEYS *

>> SET name "AItech"

>> GET name  -> returns latest values only

>> GET NAME -> returns NIL reason the key name is case sensitive.



To check the key name existing.

>> EXISTS name -> returns 1 means the key with name is exists in redis DB.

>> EXISTS NAME -> returns 0 as the key is case sensitive so it will return False.

>> DEL name -> deletes the key named name.

>> EXISTS name -> returns 0 

>> DEL name -> returns 0 , it will not throw error.



>> SET name "tester"

>> GET name



NAMESPACE - its a random string. ex: while storing information in user detail. then we can give like name:std:section:11

unique value we need to use during the namespace declaration.

Always make sure namespace is defined uniquely so that it will used individually. If we use a id alone like 11 then there is always a chance the name space will be misused.

ex: SET mycomputer:lenovo:2026model:v24.1.1 "Windows OS"

GET mycomputer:lenovo:2026model:v24.1.1

make sure your key is also unique sometimes.

So far we have seen String, now we will look after Numbers/



Numbers 

>> SET page_num 10

>> GET page_num  -> returns 10

>> INCR page_num  -> returns values 11

>> GET page_num -> returns 11

>> DECR page_num  -> returns 10 again.

>> GET page_num -> returns 10


Next set some expiry for the key value pair.

>> SET name "Tester Friend" EX 10

>> TTL name -> retuns the remaining time.

>> GET name -> after 10 seconds the name key will be deleted.

TTL - Time to Live >> will be used mainly during cache in validation- if the cached dataa is not required for longer time then this command will be used.

this will be used during OTP, Session storage.

We will be using these in backend cache mainly. If you see in browser F12 mostly the details will be stored in session cache and improves the performance. similarly  this will stored in backend. you can try in F12 and disable cache options to view the performance.
