--2. Première Partie du test SQL
SELECT date, SUM(prod_price*prod_qty) AS ventes
FROM TRANSACTION
WHERE date BETWEEN '2010-01-01' AND '2010-12-31'
GROUP BY date
ORDER BY date ASC

--3. Deuxième Partie du test SQL
SELECT a.client_id as client_id,
SUM(CASE WHEN b.product_type = 'MEUBLE' THEN prod_price*prod_qty ELSE 0 END) AS ventes_meuble,
SUM(CASE WHEN b.product_type = 'DECO' THEN prod_price*prod_qty ELSE 0 END) AS ventes_deco
FROM TRANSACTION a
INNER JOIN PRODUCT_NOMENCLATURE b on a.prop_id = b.product_id
WHERE a.date BETWEEN '2010-01-01' AND '2010-12-31'
GROUP BY a.client_id