### WAL
Write Ahead log
Crash Then data will get backed up from the WAL logs file.

postgres> startup progress

# from DB side

WAL directory  > pg_wal 

SELECT pg_Current_wal_lsn();

ls -lt | head

program files /Postgres > you will see the wal logs files

insert into users(name, amount) values('Jegan', 10);
COMMIT;

CHECKPOINT; > record stores in WAL later it will be written into the disk by the checkpointer 
Writes from buffer to disk.

SELECT pg_Current_wal_lsn();


Point intime recovery > PITR

# Backup
Physical > Table > Queries + SQL
Logical > Table > SQL + Role + Trigger + Constraint

pg_dump -U admin -d dbName --data-only  -f backup.sql

pgbackrest > mechanism for backup
replica > another option to explore
pg_dumpall > all the info about the users will be stored

pg_dumpall -U admin --roles-only > backup_roles.sql


