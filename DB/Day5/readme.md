Isolation

Transaciton

BEGIN 
...
COMMIT/ROLLBACK


Begin
select * from film limit 10;
select title form film  limit 10;
update film set title = 'changed Tilte' where  title = 'African egg'
select * from film limit 10;

commit 

update film set title = 'changed Tilte' where  title like 'Changed%'
ROLLBACK

Atomicity - Either all success or all failure.

Three types of problem 
# Dirty read
Dirty reads - data reads from temporary fields
# Non repeatable Reads 
Non repeatable reads > Almost like an update query
-> Multiple transaction at a same time
# Phantom reads 
Phantom read: > almost like a insert query
New data got inserted during the transaction. 

Solution: 
Transaction A
BEGIN ISOLATion LEVEL REPEATABLE READ
Select * from accounts limit 10;
select sum(balance) from accounts;

Transaction B
BEGIN 
Update accounts set balance = balance + 5 where id =2;
COMMIT

## SERIALISABLE
Transaction A
BEGIN ISOLATION LEVEL SERIALISABLE;
Update accounts set set balance =1000 where id =1 

Transaction B
BEGIN ISOLATION LEVEL SERIALISABLE;
Update accounts set set balance =1000 where id =1 
Waiting for the Transation to be completed until the TRansaction A to complete.

# md file commands

- [x] Task completed
- [ ] Task pending

