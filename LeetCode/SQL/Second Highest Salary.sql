# This is giving an error if the table has two same salary values
SELECT FirstName, LastName , City , State
FROM Person LEFT JOIN Address ON Person.PersonID = Address.PersonID

#So...
SELECT MAX(Salary) AS SecondHighestSalary FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee)
