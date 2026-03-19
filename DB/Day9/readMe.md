### Windows Function.
Ranking -> ROW number, Ntile, Rank, dense rank, 
Aggregation -> sum, max, min, avg, count

## Today's Topic
=============
3. Value funtions
4. Distribution functions.

Extra topic -> ROWS

Explanation
------
Value functions
- LAG 
- LEAD
- FIRSTVALUE
- LASTVALUE

# LAG
only 1 row will be used and compared.
compare previous ROW and current row.

select * from monthly_sales;
select region, month, sales_amount, LAG(sales_amount) over (partition by REGION order by month) as last_month_Sales from monthly_Sales;

previous month sales will be displayed in a single row

Output
======
region	month	sales_amount	last_month_sales
North	Jan	1000	NULL
North	Feb	1200	1000
North	Mar	900	1200
South	Jan	800	NULL
South	Feb	950	800

select region, month, sales_amount, LAG(sales_amount,2) over (partition by REGION order by month) as last_month_Sales from monthly_Sales;


Output
======
region	month	sales_amount	last_month_sales
North	Jan	1000	NULL
North	Feb	1200	Null
North	Mar	900	1000
South	Jan	800	NULL
South	Feb	950	800

select region, month, sales_amount, LAG(sales_amount,2,0) over (partition by REGION order by month) as last_month_Sales from monthly_Sales;


Output
======
region	month	sales_amount	last_month_sales
North	Jan	1000	0
North	Feb	1200	0
North	Mar	900	1000
South	Jan	800	0
South	Feb	950	800

# LEAD

Lead is also a similar one. >  from last record it will starts its calculation

select region, month, sales_amount, LAG(sales_amount,2,0) over (partition by REGION order by month) as 
last_month_Sales from monthly_Sales;

# FIRST_VALUE
this picks the first record and entries will be published
select id, region, month, sales_amount, FIRST_VALUE(SALES_amount) over ( PARTITION BY region ORDER BY month) as last_month_sales from monthly_sales;
Output
======
region	month	sales_amount	last_month_sales
North	Jan	    1000	        1000
North	Feb	    1200	        1000
North	Mar	   	900         	1000
South	Jan		800		        800
South	Feb	    950	            800

select id, region, month, sales_amount, LAST_VALUE(SALES_amount) over ( PARTITION BY region ORDER BY month) as last_month_sales from monthly_sales;
Output
======
region	month	sales_amount	last_month_sales
North	Jan	    1000	        1000
North	Feb	    1200	        1000
North	Mar	   	900         	1000
South	Jan		800		        800
South	Feb	    950	            800


===
Next TOPIC

over {
    partition by
    group by
    order by
    ROWS between 0 and 2
    Rows  between PRECEDING and following
    Rows  between PRECEDING and unbounded following
    Rows  between unbounded PRECEDING and  following
     Rows  between current_row and  following
}


select id, region, month, sales_amount, LAST_VALUE(SALES_amount) over ( PARTITION BY region ORDER BY month ROWS BETWEEN UNBOUNDED PRECEDING and UNBOUNDED FOLLOWING) as last_month_sales from monthly_sales;

========
PANDAS
SPARK

Below is used mostly during SPARK.
percent rank  >  0 to 1 
Cumulative distribuiton > current row above how many rows and below rows 

Ex: 
select * from  monthly_sales
select id, region, month, sales_amount, PERCENT_RANK() OVER (PARTITION BY region ORDER BY month) as percent_rank from employee;

select id, region, month, sales_amount, CUME_DIST() OVER (PARTITION BY region ORDER BY month) as cum_dist from employee;


ROWS
UNBOUNDED PRECEDING -> START from first row
CURRENT ROW -> start from current row
UNBOUNDED FOLLOWING -> until last row
PRECEDING n -> n row before -> 
following -> n rows after 

ROWS BETWEEN __ and __; this is used in Query.


select id, region, month, sales_amount, sum(sales_amount) over (PARTITION BY region OVER BY month ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) as row_Val from monthly_sales;


select id, region, month, sales_amount, sum(sales_amount) over (PARTITION BY region OVER BY month ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) as row_Val from monthly_sales;