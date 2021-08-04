# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:47:32 2021

@author: Inbar
"""

#xp
#Basic Select Statement

#1
select first_name firstname, last_name lastname
from employees;

#2
select distinct employee_id
from employees;

#3
select * 
from employees
order by first_name DESC;

#4
select first_name, last_name, salary*0.15 as fifteen_percent_of_salary
from employees

#5
select employee_id, first_name, last_name, salary
from employees
order by salary;

#6
select sum(salary)
from employees

#7
select employee_id, first_name, last_name, min(salary) min_salary, max(salary) max_salary
from employees
group by employee_id, first_name, last_name

#8
select AVG(salary::float)
from employees;

#or:
select ROUND(AVG(salary))
from employees;

#9
select DISTINCT COUNT(employee_id)
from employees;

#10
select UPPER(first_name)
from employees;

#11
select substring(first_name from 1 for 3)
from employees;

#12
select CONCAT(first_name, ' ', last_name) 
from employees;

#13
select char_length(CONCAT(first_name, ' ', last_name))-1 fullname_length
from employees;

#14
select * from employees where first_name ~ '\d';

#15
select * 
from employees
limit 10;


#Restricting And Sorting
#1
select employee_id, salary from employees where salary between 10000 and 15000;

#2
select employee_id, hire_date from employees where hire_date between '1987-01-01' and '1987-12-31';

#3
select first_name 
from employees 
where first_name like '%c%'and first_name like '%e%';

#4
select last_name, job_title, salary
from employees e
join jobs j
on j.job_id = e.job_id
where job_title != 'Shipping Clerks' or job_title != 'Programmers'
and (salary != 4500 or salary != 10000 or salary != 15000)

#5
select last_name
from employees
where char_length(last_name) = 6;

#6
select last_name
from employees
where position('e' in last_name) = 3;

#7
select distinct job_title
from jobs

#8
select *
from employees
where upper(last_name) in('JONES', 'BLAKE', 'SCOTT', 'KING', 'FORD')




