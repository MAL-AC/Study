DROP DATABASE IF EXISTS HumanFriends;
CREATE DATABASE IF NOT EXISTS HumanFriends;
USE HumanFriends;

-- Создание таблицы AnimalClasses
DROP TABLE IF EXISTS AnimalClasses;
CREATE TABLE IF NOT EXISTS AnimalClasses
( Id INT AUTO_INCREMENT PRIMARY KEY, 
	ClassAnimal VARCHAR(20));
    
-- Заполнение таблицы AnimalClasses
INSERT INTO AnimalClasses (ClassAnimal)
VALUES ('Pets'), ('PackAnimals');

-- Создание таблицы PackAnimals
DROP TABLE IF EXISTS PackAnimals;
CREATE TABLE IF NOT EXISTS PackAnimals
(	Id INT AUTO_INCREMENT PRIMARY KEY,
    TypeAnimal VARCHAR (20),
    ClassId INT,
    FOREIGN KEY (ClassId) REFERENCES AnimalClasses (Id) ON DELETE CASCADE ON UPDATE CASCADE
    );
    
-- Заполнение таблицы PackAnimals
INSERT INTO PackAnimals (TypeAnimal, ClassId) VALUES
('Horses', 1),
('Camels', 1),
('Donkeys', 1);

-- Создание таблицы Horses
DROP TABLE IF EXISTS Horses;
CREATE TABLE IF NOT EXISTS Horses 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(20), 
    Birthday DATE,
    Commands VARCHAR(45),
    TypeId int,
    Foreign KEY (TypeId) REFERENCES PackAnimals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Заполнение таблицы Horses
INSERT INTO Horses (Name, Birthday, Commands, TypeId)
VALUES ('Thunder', '2015-07-21', 'Trot, Canter, Gallop', 1),
('Storm', '2014-05-05', 'Trot, Canter', 1),  
('Blaze', '2016-02-29', 'Trot, Jump, Gallop', 1); 

-- Создание таблицы Camels
DROP TABLE IF EXISTS Camels;
CREATE TABLE IF NOT EXISTS Camels 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(20), 
    Birthday DATE,
    Commands VARCHAR(45),
    TypeId int,
    Foreign KEY (TypeId) REFERENCES PackAnimals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Заполнение таблицы Camels
INSERT INTO Camels (Name, Birthday, Commands, TypeId)
VALUES ('Sandy', '2016-11-03', 'Walk, Carry Load', 2),
('Dune', '2018-12-12', 'Walk, Sit', 2),  
('Sahara', '2015-08-14', 'Walk, Run', 2); 

-- Создание таблицы Donkeys
DROP TABLE IF EXISTS Donkeys;
CREATE TABLE IF NOT EXISTS Donkeys 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(20), 
    Birthday DATE,
    Commands VARCHAR(45),
    TypeId int,
    Foreign KEY (TypeId) REFERENCES PackAnimals (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Заполнение таблицы Donkeys
INSERT INTO Donkeys (Name, Birthday, Commands, TypeId)
VALUES ('Eeyore', '2017-09-18', 'Walk, Carry Load, Bray', 3), 
('Burro', '2019-01-23', 'Walk, Bray, Kick', 3); 


-- Создание таблицы Pets
DROP TABLE IF EXISTS Pets;
CREATE TABLE IF NOT EXISTS Pets
(	Id INT AUTO_INCREMENT PRIMARY KEY,
    TypeAnimal VARCHAR (20),
    ClassId INT,
    FOREIGN KEY (ClassId) REFERENCES AnimalClasses (Id) ON DELETE CASCADE ON UPDATE CASCADE
    );
    
-- Заполнение таблицы PackAnimals
INSERT INTO Pets (TypeAnimal, ClassId) VALUES
('Dogs', 2),
('Cats', 2),
('Hamsters', 2);

-- Создание таблицы Dogs
DROP TABLE IF EXISTS Dogs;
CREATE TABLE IF NOT EXISTS Dogs 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(20), 
    Birthday DATE,
    Commands VARCHAR(45),
    TypeId int,
    Foreign KEY (TypeId) REFERENCES Pets (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Заполнение таблицы Dogs
INSERT INTO Dogs (Name, Birthday, Commands, TypeId)
VALUES ('Fido', '2020-01-01', 'Sit, Stay, Fetch', 1),
('Buddy', '2018-12-10', 'Sit, Paw, Bark', 1),  
('Bella', '2019-11-11', 'Sit, Stay, Roll', 1); 

-- Создание таблицы Cats
DROP TABLE IF EXISTS Cats;
CREATE TABLE IF NOT EXISTS Cats 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(20), 
    Birthday DATE,
    Commands VARCHAR(45),
    TypeId int,
    Foreign KEY (TypeId) REFERENCES Pets (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Заполнение таблицы Cats
INSERT INTO cats (Name, Birthday, Commands, TypeId)
VALUES ('Whiskers', '2019-05-15', 'Sit, Pounce', 2),
('Smudge', '2020-02-20', 'Sit, Pounce, Scratch', 2),  
('Oliver', '2020-06-30', 'Meow, Scratch, Jump', 2); 

-- Создание таблицы Hamster
DROP TABLE IF EXISTS Hamsters;
CREATE TABLE IF NOT EXISTS Hamsters 
(       
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    Name VARCHAR(20), 
    Birthday DATE,
    Commands VARCHAR(45),
    TypeId int,
    Foreign KEY (TypeId) REFERENCES Pets (Id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Заполнение таблицы Hamsters
INSERT INTO Hamsters (Name, Birthday, Commands, TypeId)
VALUES ('Hammy', '2021-03-10', 'Roll, Hide', 3), 
('Peanut', '2021-08-01', 'Roll, Spin', 3); 


-- Удалить записи о верблюдах и объединить таблицы лошадей и ослов.
SET SQL_SAFE_UPDATES = 0;
DELETE FROM camels;

SELECT Name, Birthday, Commands FROM horses
UNION SELECT  Name, Birthday, Commands FROM donkeys;

-- Создать новую таблицу для животных в возрасте от 1 до 3 лет и вычислить их возраст с точностью до месяца.
CREATE TEMPORARY TABLE animals AS 
SELECT *, 'Лошади' as genus FROM horses
UNION SELECT *, 'Ослы' AS genus FROM donkeys
UNION SELECT *, 'Собаки' AS genus FROM dogs
UNION SELECT *, 'Кошки' AS genus FROM cats
UNION SELECT *, 'Хомяки' AS genus FROM hamsters;

DROP TABLE IF EXISTS YangAnimal;
CREATE TABLE IF NOT EXISTS YangAnimal AS
SELECT Name, Birthday, Commands, genus, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) AS AgeInMonth
FROM animals WHERE Birthday BETWEEN ADDDATE(curdate(), INTERVAL -3 YEAR) AND ADDDATE(CURDATE(), INTERVAL -1 YEAR);
 
SELECT * FROM YangAnimal;

-- Объединить все созданные таблицы в одну, сохраняя информацию о принадлежности к исходным таблицам.
SELECT h.Name, h.Birthday, h.Commands, pa.TypeAnimal, ya.AgeInMonth 
FROM horses h
LEFT JOIN YangAnimal ya ON ya.Name = h.Name
LEFT JOIN PackAnimals pa ON pa.Id = h.TypeId
UNION 
SELECT d.Name, d.Birthday, d.Commands, pa.TypeAnimal, ya.AgeInMonth 
FROM donkeys d 
LEFT JOIN YangAnimal ya ON ya.Name = d.Name
LEFT JOIN PackAnimals pa ON pa.Id = d.TypeId
UNION
SELECT c.Name, c.Birthday, c.Commands, ha.TypeAnimal, ya.AgeInMonth 
FROM cats c
LEFT JOIN YangAnimal ya ON ya.Name = c.Name
LEFT JOIN Pets ha ON ha.Id = c.TypeId
UNION
SELECT d.Name, d.Birthday, d.Commands, ha.TypeAnimal, ya.AgeInMonth 
FROM dogs d
LEFT JOIN YangAnimal ya ON ya.Name = d.Name
LEFT JOIN Pets ha ON ha.Id = d.TypeId
UNION
SELECT hm.Name, hm.Birthday, hm.Commands, ha.TypeAnimal, ya.AgeInMonth 
FROM hamsters hm
LEFT JOIN YangAnimal ya ON ya.Name = hm.Name
LEFT JOIN Pets ha ON ha.Id = hm.TypeId;