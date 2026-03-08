primary key - unique key and not null.
JSONB < decompiled binary format

if any failure happened while inserting in DB - primary key will be calculated. so ID will increment always


================= QUERIES ================
create Database userdb;
\c userdb;  
CREATE TABLe users(id bigserial primary key,
name varchar(100) not null,
email varchar(100) Unique not null,
age smallint check (age >=18) ,
salary numeric(10,2),
is_active boolean default true,
role varchar(20) check (role in ('admin','user','manager')),
created_at timestamptz default now()
);

insert into users (name, email, age, salary, role ) values ('jegan', 'a@a.com', 30, 'test', 100 );
insert into users (name, email, age, role, salary ) values ('jegan3', 'a@a3.com', 30, 'manager', 100 );


insert into users (name, email, age, role, salary ) values ('jegan5', 'a@a5.com', 30, 'manager', 100 ),('jegan6', 'a@a6.com', 30, 'manager', 100 ),('jegan7', 'a@a7.com', 30, 'manager', 100 );

insert into users (name, email, age, role, salary ) values ('jegan8', 'a@a8.com', 30, 'manager', 100 ),('jegan9', 'a@a9.com', 30, 'manager', 100 ),('jegan10', 'a@a10.com', 30, 'manager', 100 ) returning id;

insert into users (name, email, age, role, salary ) values ('jegan11', 'a@a11.com', 30, 'manager', 100 ) returning id

update users set salary = salary+500 where id =3;

update users set salary = salary+500 where id =6 returning id; 

update users set is_active=false where created_at < now() - interval '10 minute';

delete from users where id =1;


schema validation
\d users; 
truncate table users;

alter table user phone_no int; 