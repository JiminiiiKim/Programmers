# 특정 물고기를 잡은 총 수 구하기
SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO AS F
JOIN FISH_NAME_INFO AS N
ON F.FISH_TYPE = N.FISH_TYPE
WHERE FISH_NAME IN ('BASS', 'SNAPPER');