 --- SQL Queries for Google Salaries Database
SELECT *
FROM google_salaries
WHERE salary > 50000;

--- Query to find employees with 'Ma' in their first name
SELECT first_name, department, education
FROM google_salaries
WHERE first_name LIKE 'Ma%';

--- Query to find distinct departments
SELECT DISTINCT department
FROM google_salaries;

--- Query to calculate total salary by education level
SELECT education, SUM(salary) AS total_salary
FROM google_salaries
GROUP BY education;
