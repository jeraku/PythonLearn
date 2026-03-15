Topic:
Joins

create table employee (emp_id serial primary key, emp_name varchar(100), dept_id integer, salary integer);
insert into employee (emp_name, dept_id, salary) values ('jegan', 1, 100), ('jegan1', 1, 101),('jegan2', 1, 102);
select * from employee;
insert into employee (emp_name, dept_id, salary) values ('Raj', 2, 100), ('Raj1', 2, 101), ('Raj3', 2, 103);
insert into employee (emp_name, dept_id, salary) values ('Raj', 2, 103), ('Rajk1', 3, 1031), ('Rajk3', 3, 1033);

update employee set dept_id = 3 where emp_name='Raj' and emp_id = 5;
select * from employee;

create department (dept_id serial primary  key, dept_name varchar(100) not null);
insert into department (dept_name) values ('hr', 'cse');
select * from department;

ALTER TABLE employees
ADD COLUMN dept_id INTEGER NOT NULL;
ALTER TABLE employees
ALTER COLUMN dept_id TYPE INTEGER;

select e.emp_name, e.dept_id, e.salary, d.dept_name from employee as e, department as d where e.dept_id = d.dept_id;

select e.emp_name, e.dept_id, e.salary, d.dept_name from employee as e inner join department as d on e.dept_id = d.dept_id;

select e.emp_name, e.dept_id, e.salary, d.dept_name from employee as e right join department as d on e.dept_id = d.dept_id;

select e.emp_name, e.dept_id, e.salary, d.dept_name from employee e left join department d on e.dept_id = d.dept_id;

select e.emp_name, e.dept_id, e.salary, d.dept_name from employee e full outer join department d on e.dept_id = d.dept_id;


show wal_ tab
show wal_synchronous_commit; > if its ON then if I give commit, wal_buffer and then in WAL_disk.

this will show the allocation in postgres db. below is for performance.
increase WAL size 
or 
syn commit off then not write in disc; 

show WAL_buffers;

