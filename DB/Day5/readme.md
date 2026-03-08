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
Dirty reads - data reads from temporary fields

Non repeatable reads 
-> Multiple transaction at ta same time

