SELECT
    CASE
        WHEN (A+B <= C) OR (B+C<= A) OR (C+A <= B)
            THEN "Not A Triangle"
        WHEN (A=B) AND (A=C)
            THEN "Equilateral"
        WHEN (A=B) OR (B=C) OR (C=A)
            THEN "Isosceles"
        ELSE
            "Scalene"
    END
FROM TRIANGLES
