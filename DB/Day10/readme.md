### Topic
Subquery and CTE > common Table Expression

Subquery -> innerquery

Dept
employee
project 
users

select emp_name, salary from employees as e where salary > (select AVG(Salary) from employees where dept_id = e.dept_id);


correlated sub query>
Line by line it executes and response , example is above query.

mostly subquery is used during the JOINS

Subquery are always slower. to impprove this only we are going with the CTE ->  which is temporary return table.

CTE -> Temporary named Result Set
1) readability
2) reusability
3) Recurssion
4) Durability
5) Debugging


WITH avg_salary AS (
    SELECT 
        dept_id,
        AVG(salary) AS avg_sal
    FROM employees
    GROUP BY dept_id
)
SELECT 
    e.emp_name,
    e.salary,
    a.avg_sal
FROM employees AS e
JOIN avg_salary AS a
    ON e.dept_id = a.dept_id
WHERE e.salary >= a.avg_sal;

my_database=# EXPLAIN ANALYSE select * from employee
my_database-# ;
                                             QUERY PLAN
----------------------------------------------------------------------------------------------------
 Seq Scan on employee  (cost=0.00..1.09 rows=9 width=230) (actual time=0.187..0.204 rows=9 loops=1)
 Planning Time: 1.821 ms
 Execution Time: 0.484 ms
(3 rows)


To generate dummy details in DB 
go with MD5
generate_Series


psql -U admin -d my_database -f /mnt/windows_function.sql