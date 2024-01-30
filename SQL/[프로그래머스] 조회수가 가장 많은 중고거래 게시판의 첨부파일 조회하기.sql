# 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기
SELECT CONCAT('/home/grep/src/', F.BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) FIL
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_FILE F
ON B.BOARD_ID = F.BOARD_ID
WHERE VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY FILE_ID DESC;