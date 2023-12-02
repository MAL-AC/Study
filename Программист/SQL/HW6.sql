DROP DATABASE IF EXISTS HW6;
CREATE DATABASE HW6;
USE HW6;
DELIMITER //

/*Задание 1: Создайте функцию, которая принимает кол-во сек и формат их в кол-во дней часов. Пример: 123456 ->'1 days 10 hours 17 minutes 36 seconds ' */
DROP FUNCTION IF EXISTS TASK1//
CREATE FUNCTION TASK1(seconds INT)
RETURNS TEXT DETERMINISTIC
BEGIN
DECLARE days INT;
  DECLARE hours INT;
  DECLARE minutes INT;
  DECLARE result VARCHAR(255);

  SET days = FLOOR(seconds / 86400);
  SET seconds = seconds % 86400;

  SET hours = FLOOR(seconds / 3600);
  SET seconds = seconds % 3600;

  SET minutes = FLOOR(seconds / 60);
  SET seconds = seconds % 60;

  SET result = CONCAT(days, ' days ', hours, ' hours ', minutes, ' minutes ', seconds, ' seconds');

  RETURN result;
END //

SELECT TASK1(123456)//


/* Задание 2: Выведите только четные числа от 1 до 10. Пример: 2,4,6,8,10 */
DROP PROCEDURE IF EXISTS TASK2//
CREATE PROCEDURE TASK2 ()
BEGIN
  DECLARE i INT DEFAULT 0;
  DROP TABLE IF EXISTS nums;
  CREATE TABLE nums (n INT);
  WHILE i < 10 DO
	SET i = i + 2;
	INSERT INTO nums(n) VALUES(i);
  END WHILE;
  SELECT GROUP_CONCAT(n SEPARATOR', ') AS nums FROM nums;
END//

CALL TASK2()//