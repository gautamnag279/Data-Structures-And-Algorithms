SELECT DISTINCT(CITY) FROM STATION
WHERE CITY REGEXP '^[^aeiou]';

^ indicates the beginning of the string. $ indicates the end of the string. selects those which dont contain AEIOU in the begining. ^[^AEIOU]
