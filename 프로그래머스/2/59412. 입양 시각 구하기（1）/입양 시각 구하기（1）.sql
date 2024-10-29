SELECT DATE_FORMAT(DATETIME,"%H") AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
GROUP BY DATE_FORMAT(DATETIME,"%H")
HAVING HOUR>=9 AND HOUR<20
ORDER BY HOUR