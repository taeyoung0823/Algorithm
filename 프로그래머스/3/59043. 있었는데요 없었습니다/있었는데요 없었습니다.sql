SELECT DISTINCT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS AS A
JOIN ANIMAL_OUTS AS B
ON A.DATETIME>B.DATETIME AND A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY A.DATETIME