### Window function.
RANKING and AGGREGATION

select AVG(salart) from department;
select emp_name, salary, avg_salary from employees as e inner join (select AVG(salary), salary, a.dep form employee as a GRPoup by a.department) as a on a.department = e.department


Aggregation/ order
    1. Partition by
    2. order by 
    3. rows 

1. Ranking function
    Row number -> [order by, Group by]
    Row, Rank, Dense Rank, NTILE
2. Aggregation function
    Sum
    AVG
    Min
    Max
    Count
3. Value
4. Distribution


## Ranking Function Examples

select emp_id, emp_name ,dept_id , salary, ROW_NUMBER() OVER (ORDER BY SALARY desc) from employee; 
select emp_id, emp_name ,dept_id , salary, ROW_NUMBER() OVER (PARTITION BY dept_id order by salary desc) from employee; 

Rank (Ranking order: 1,1,2,3) and Dense Rank (Ranking order: 1,1,3,4)

select emp_id, emp_name, dept_id, salary, Rank() over (PARTITION BY dept_id order by SALARY desc) from employee;
select emp_id, emp_name, dept_id, salary, DENSE_RANK() over (PARTITION BY dept_id order by SALARY desc) from employee;

# splits in to a group based on the NTILE
select emp_id, emp_name, dept_id, salary, NTILE(4) over (order by Salary desc) as QUARTILE from employee;
select emp_id, emp_name, dept_id, salary, NTILE(100) over (order by Salary desc) as QUARTILE from employee;

## Aggreation examples
select emp_id, emp_name, dept_id ,salary, sum(salary) over (partition by dept_id) as total_sum from employee;

select * from transactions;

select account_id, amount, sum( amount) over (partition by account_id order by txn_date) from transcations;
