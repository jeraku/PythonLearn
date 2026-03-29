### Day 12 - Views & Materialized Views
Basic view: 

CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;



CREATE MATERIALIZED VIEW mat_view_name AS
SELECT column1, column2
FROM table_name;

## View example
select * from departments
select * from employees;

select e.emp_id, e.emp_name, d.dept_name, e.salary from employees e left join department d on e.emp_id = d.dept_id;

create view employees_dept as select e.emp_id, e.emp_id, d.dept_name, e.salary from employees e left join department d on e.emp_id = d.dept_id;

SELECT * FROM  employee_dept;

 If I update the details from existing table and run select query which will pull the latest values.
update employee set salary = 1000 where emp_id=2;
SELECT * FROM  employee_dept;

## Materialised view
Normal view: 
IF you change the original table tthen view table will not get updated.
Materialised view: If you change the original table then calling the view table, which will idsplay the older table only.
create MATERIALISED VIEW employees_dept_mat as SELECT e.emp_id, e.emp_id, d.dept_name, e.salary from employees e left join department d on e.emp_id = d.dept_id;


To pull the data from origingal table use the REFRESH 
REFRESH MATERIALISED VIEW employees_dept_mat ;
\d to check the table type


## Nested Materialised view
CREATE MATERIALISED VIEW emp_dept_2 as SELECT emp_id, emp_name, salary, dept_name from employees_dept_mat;

update employee set salary =23443 where emp_id =3;

