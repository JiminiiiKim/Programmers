# 취소되지 않은 진료 내역 조회하기
SELECT APNT_NO, PT_NAME, A.PT_NO, A.MCDP_CD, DR_NAME, APNT_YMD
FROM APPOINTMENT AS A
JOIN PATIENT AS P
ON A.PT_NO = P.PT_NO
JOIN DOCTOR AS D
ON A.MDDR_ID = D.DR_ID
WHERE APNT_CNCL_YN = 'N' AND APNT_YMD LIKE "2022-04-13%" AND A.MCDP_CD = 'CS'
ORDER BY APNT_YMD;