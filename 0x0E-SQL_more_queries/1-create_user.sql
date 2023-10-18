-- creates the MYSQL server user user_Od_1.
-- user_od_1 should have all privileges on your MySLQ server
-- password set to user_od_1_pwd.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;

