# 가격대 별 상품 개수 구하기
SELECT 
(CASE WHEN
    PRICE < 10000 THEN 0
    ELSE TRUNCATE(PRICE, -4) END) AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP;