# 자동차 대여 기록 별 대여 금액 구하기
SELECT HISTORY_ID, 
round(DAILY_FEE * (DATEDIFF(END_DATE,START_DATE)+1)
    * (CASE 
    WHEN DATEDIFF(END_DATE,START_DATE)+1 < 7 THEN 1
    WHEN DATEDIFF(END_DATE,START_DATE)+1 < 30 THEN 0.95
    WHEN DATEDIFF(END_DATE,START_DATE)+1 < 90 THEN 0.92
    ELSE 0.85 END)) as FEE
FROM CAR_RENTAL_COMPANY_CAR AS C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
ON C.CAR_ID = H.CAR_ID
WHERE C.CAR_TYPE = '트럭'
ORDER BY FEE DESC, HISTORY_ID DESC;