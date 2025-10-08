SELECT 
    g.Empid,
    g.first_name,
    g.last_name,
    g.department,
    g.education,
    g.salary,
    l.LaptopId,
    l.Brand,
    l.Price
FROM 
    google_salaries g
INNER JOIN 
    google_laptop l
ON 
    g.Empid = l.Empid;

SELECT 
    department,
    AVG(salary) AS average_salary
FROM 
    Google_salaries
GROUP BY 
    department;


SELECT 
    department,
    AVG(salary) AS average_salary
FROM 
    Google_salaries
GROUP BY 
    department
ORDER BY 
    average_salary DESC;
