### Topic
Subquery and CTE > common Table Expression

Subquery -> innerquery

Dept
employee
project 
users

select emp_name, salary from employees where salary > (select AVG(Salary) from employees);
