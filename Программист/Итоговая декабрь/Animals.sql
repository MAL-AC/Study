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
('Donkey', 1);

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
('Donkeys', 2);

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

