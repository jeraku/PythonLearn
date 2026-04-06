### partitioning and shrading
Partitioning.

List partitioning
hash partitioning

create table orders( id serial,
order_date DATE,
amount INT) PARTITION BY RANGE ( order_date);

create table order_Jan_2026 partition of orders for values from ('2026-01-01') to ('2026-02-01')

If we insert data into orders table then data will be populated into the partition table as well.
## Hash partitioning.
## Range sharing
## 

============
### Shrading.
Single data set > insert records into Multiple machines 
Ex: Billions of records present then spit the db info and inserted into multiple machines.
Ex: yearly 1 server will be splitted.

## Range shrading
## Hash based sharding 
    => Hash id will be created and used.
## Geo based sharding 
    => based onthe location, DB details will be stored in those locations.

