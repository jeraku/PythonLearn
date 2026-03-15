### Atomicity
either all success or either all fail. 
eX: 
jegan =100
BEGIN 
Jegan =100+5 
Issue occurred
then JEGAN = 100 only

Two transactions are started at same time and different entries are changed in 1 and changed in another. so all will fail or all will success.
Mainly this is COMMIT/ROLLBACK

WAL > 
Temporary storage - > enters the data got changed. 
when I give commit then data gets stored in buffer, but data gets stored in WAL -> then after crash then it retrieves the data and stores in DB.

</> markdown
BEGIN
SELECT * from accounts
UPDATE acccounts set balance = 'abbcd' > this will throw error as balance is numerals. In UI it will show error with ! symbol.
COMMIT

Transaction 2
BEGIN 
UPDATE acccounts set balance = 101 where id =3
UPDATE acccounts set balance = 'abbcd' 
COMMIT
then 
SELECT * from Accocuts
Above added 101 balacne will also be reverted back.

###  ISOLATION 
So 
BEGIN
select * from accounts
update accounts set balance =101 where id =3;
SAVEPOINT SP1; # this will stores temporarily
UPDATE acccounts set balance = 'abbcd' 

ROLLBACK to SP1; # * symbol will be displayed, display showing you have successful commit in place.
COMMIT
then 
SELECT * from Accocuts > updated accounts value will be displayed.

### Durability
# problems in durability
Crashes
Reboot
power outage

# solution  -> Power to enable the durability 
Write Ahead logging => WAL
checkpointing (Pending in memory) >> Command CHECKPOINT; writes from buffer to disk. perioidically it store the inforation and pass it on
Fsync and Synchronous commit >> Write into the Disk


Commands used:
SHOW WAL_;
show WAL_Buffers;
COMMIT -> 1) record stores in WAL and later writes into disk by checkpointer. 2) write directly write into disk.
For smaller DB level option 2 is better. for larger project option 1 is requried.
SHOW Sync; > shows synchrosnous COMMIT
SET synchronous_commit = 'off';

BACKUps:
