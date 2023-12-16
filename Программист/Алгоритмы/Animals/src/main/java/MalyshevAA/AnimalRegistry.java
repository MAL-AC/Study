package MalyshevAA;

import java.util.ArrayList;
        import java.util.HashMap;
        import java.util.List;
        import java.util.Map;
        import java.util.Scanner;

import java.util.*;

public class AnimalRegistry {
    private static List<Animal> animals = new ArrayList<>();
    private static Map<String, List<String>> commandsMap = new HashMap<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;

        do {
            printMenu();
            System.out.print("Выберите опцию: ");
            try {
                choice = scanner.nextInt();
                scanner.nextLine(); // Считываем лишний перевод строки

                switch (choice) {
                    case 1:
                        addAnimal();
                        break;
                    case 2:
                        listCommands();
                        break;
                    case 3:
                        trainAnimal();
                        break;
                    case 4:
                        listAnimalsByBirthDate();
                        break;
                    case 5:
                        // Добавьте свою реализацию навигации по меню
                        break;
                    case 6:
                        showAnimalCount();
                        break;
                    case 0:
                        System.out.println("Выход из программы.");
                        break;
                    default:
                        System.out.println("Неверный ввод. Пожалуйста, выберите существующую опцию.");
                }
            } catch (InputMismatchException e) {
                System.out.println("Ошибка ввода. Пожалуйста, введите корректное значение.");
                scanner.nextLine(); // Очистка буфера ввода
                choice = -1; // Присвоение недопустимого значения для продолжения цикла
            }
        } while (choice != 0);

        // Закрываем сканнер после использования
        scanner.close();
    }

    private static void printMenu() {
        System.out.println("1. Добавить новое животное");
        System.out.println("2. Список команд животного");
        System.out.println("3. Обучение новым командам");
        System.out.println("4. Вывести список животных по дате рождения");
        System.out.println("5. Навигация по меню");
        System.out.println("6. Счетчик животных");
        System.out.println("0. Выход");
    }

    private static void addAnimal() {
        System.out.print("Введите имя животного: ");
        String name = scanner.nextLine();
        System.out.print("Введите тип животного (Dog, Cat, Hamster, Horse, Camel, Donkey): ");
        String type = scanner.nextLine();
        System.out.print("Введите дату рождения животного (гггг-мм-дд): ");
        String birthDate = scanner.nextLine();

        Animal animal;
        switch (type.toLowerCase()) {
            case "dog":
                animal = new Dog(name, birthDate);
                break;
            case "cat":
                animal = new Cat(name, birthDate);
                break;
            case "hamster":
                animal = new Hamster(name, birthDate);
                break;
            case "horse":
                animal = new Horse(name, birthDate);
                break;
            case "camel":
                animal = new Camel(name, birthDate);
                break;
            case "donkey":
                animal = new Donkey(name, birthDate);
                break;
            default:
                System.out.println("Неверный тип животного.");
                return;
        }

        animals.add(animal);
        System.out.println("Животное успешно добавлено.");
    }

    private static void listCommands() {
        System.out.print("Введите имя животного: ");
        String name = scanner.nextLine();

        for (Animal animal : animals) {
            if (animal.getName().equalsIgnoreCase(name)) {
                System.out.println("Список команд для " + animal.getName() + ": " + animal.getCommands());
                return;
            }
        }

        System.out.println("Животное с именем " + name + " не найдено.");
    }

    private static void trainAnimal() {
        System.out.print("Введите имя животного: ");
        String name = scanner.nextLine();

        for (Animal animal : animals) {
            if (animal.getName().equalsIgnoreCase(name)) {
                System.out.print("Введите новую команду для обучения: ");
                String newCommand = scanner.nextLine();
                animal.train(newCommand);
                System.out.println("Животное успешно обучено новой команде.");
                return;
            }
        }

        System.out.println("Животное с именем " + name + " не найдено.");
    }

    private static void listAnimalsByBirthDate() {
        List<Animal> sortedAnimals = new ArrayList<>(animals);
        sortedAnimals.sort(Comparator.comparing(Animal::getBirthDate));
        System.out.println("Список животных по дате рождения:");
        for (Animal animal : sortedAnimals) {
            System.out.println(animal.getName() + " (" + animal.getBirthDate() + ")");
        }
    }

    private static void showAnimalCount() {
        System.out.println("Общее количество животных: " + animals.size());
    }
}

// Остальной код остается без изменений...


// Абстрактный класс Animal и его подклассы
abstract class
Animal {
    private String name;
    private String birthDate;
    private List<String> commands;

    public Animal(String name, String birthDate) {
        this.name = name;
        this.birthDate = birthDate;
        this.commands = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public String getBirthDate() {
        return birthDate;
    }

    public List<String> getCommands() {
        return commands;
    }

    public void train(String newCommand) {
        commands.add(newCommand);
    }
}

class Dog extends Animal {
    public Dog(String name, String birthDate) {
        super(name, birthDate);
    }
}

class Cat extends Animal {
    public Cat(String name, String birthDate) {
        super(name, birthDate);
    }
}

class Hamster extends Animal {
    public Hamster(String name, String birthDate) {
        super(name, birthDate);
    }
}

class Horse extends Animal {
    public Horse(String name, String birthDate) {
        super(name, birthDate);
    }
}

class Camel extends Animal {
    public Camel(String name, String birthDate) {
        super(name, birthDate);
    }
}

class Donkey extends Animal {
    public Donkey(String name, String birthDate) {
        super(name, birthDate);
    }
}
