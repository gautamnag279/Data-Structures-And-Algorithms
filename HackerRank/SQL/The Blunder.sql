SELECT CEIL(AVG(SALARY) - AVG(REPLACE(SALARY , '0' , ''))) FROM EMPLOYEES

#The CEIL() function returns the smallest integer value that is bigger than or equal to a number.
