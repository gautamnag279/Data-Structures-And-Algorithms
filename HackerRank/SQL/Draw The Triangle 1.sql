SET @NUMBER = 21;
SELECT REPEAT('* ' , @NUMBER := @NUMBER -1) FROM INFORMATION_SCHEMA.TABLES;

INFORMATION_SCHEMA is the information database, the place that stores information about all the other databases that the MySQL server maintains.
Inside INFORMATION_SCHEMA there are several read-only tables. They are actually views, not base tables, so there are no files associated with them.
