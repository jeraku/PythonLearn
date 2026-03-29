### Day 11 - Indexing in Postgres - BTree, Hash, Unique, Partial

Indexing -> Faster Fetch
BTREE indexing > 
---
for strings - we can go for hash indexing. 
For Ranges like between or greater or lesser then go for BTREE indexing 
Partial indexing = for specific set of index values go for partial indexing.
unique indexing for unique values. 
---

1) BTREE indexing
If your query is uses >, <,<=, >=, =, Between
then use the BTREE indexing. in this condition we need to go for indexing.
If your query is between ranges then we need to go for BTree indexing concept
select * from users where age =30;

EXPLAIN analyze select * from users where age =30;
CREATE INDEX idx_users_age on Users(age);

select * from users where age =30;
EXPLAIN analyze select * from users where age =30;
<!-- check for time now -->
---

2) Hash indexing
direct match > then we need to go for HAsh indexing.
ex: email - search in hash memory and response.

drop index idx_users_age;

select * from users where email = 'user_400000@test.com';

EXPLAIN ANALYZE select * from users where email = 'user_400000@test.com';

CREATE INDEX idx_user_email ON users using hash(email);

---
3) PARTIAL Indexing
Based on query, column like is_active  is boolean then all query age > 80. 
then partial indexing will be used.
 select * from users where is_active = TRUE;
EXPLAIN ANALYZE select * from users where is_active = TRUE;

CREATE index idx_act_users on users(is_active) where is_active=true;

count <60% 
then no point in using it.

so we need to go for the lesser data.


EXPLAIN ANALYZE select * from users where is_active = FALSE;

CREATE index idx_inact_users on users(is_active) where is_active=FALSE;
---
4) UNIQUE indexing.
CREATE UNIQUE INDEX idx_unique_email on users(email);
EXPLAIN ANALYZE select * from users where email = 'user_400000@test.com';

---
