SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS AS A
LEFT JOIN ANIMAL_INS AS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL