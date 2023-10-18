-- list all records from second_table.
-- dont't list rows withous a name value.
-- in descecnding order.

SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
