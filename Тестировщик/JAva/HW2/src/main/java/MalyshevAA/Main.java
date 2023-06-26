package MalyshevAA;

import java.io.File;

import java.io.FileWriter;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Main {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Добро пожаловать на решения домашней работы № 2.");

        while (true) {
            System.out.println("\nЗадание 1: Дана строка sql-запроса \"select * from students where \". \n" +
                    "Сформируйте часть WHERE этого запроса, используя StringBuilder. \n" +
                    "Данные для фильтрации приведены ниже в виде json-строки.\n" +
                    "Если значение null, то параметр не должен попадать в запрос.\n" +
                    "Параметры для фильтрации: {\"name\":\"Ivanov\", \"country\":\"Russia\", \"city\":\"Moscow\", \"age\":\"null\"}");
            System.out.println("\nЗадание 2: Реализуйте алгоритм сортировки пузырьком числового массива, " +
                    "\nрезультат после каждой итерации запишите в лог-файл.");
            System.out.println("\nЗадание 3: Дана json-строка (можно сохранить в файл и читать из файла)\n" +
                    "[{\"фамилия\":\"Иванов\",\"оценка\":\"5\",\"предмет\":\"Математика\"},{\"фамилия\":\"Петрова\",\"оценка\":\"4\",\"предмет\":\"Информатика\"},{\"фамилия\":\"Краснов\",\"оценка\":\"5\",\"предмет\":\"Физика\"}]\n" +
                    "Написать метод(ы), который распарсит json и, используя StringBuilder, создаст строки вида: Студент [фамилия] получил [оценка] по предмету [предмет].\n" +
                    "Пример вывода:\n" +
                    "Студент Иванов получил 5 по предмету Математика.\n" +
                    "Студент Петрова получил 4 по предмету Информатика.\n" +
                    "Студент Краснов получил 5 по предмету Физика.");
            System.out.println("\nЗадание 4: К калькулятору из предыдущего ДЗ добавить логирование.");
            System.out.println("\nУкажите номер задания или введите 0 для выхода: ");

            int no = Integer.parseInt(scanner.nextLine());
            if (no == 1) {
                task1();
            } else if (no == 2) {
                task2();
            } else if (no == 3) {
                task3();
            } else if (no == 4) {
                task4();
            } else if (no == 0) {
                System.out.println("Вы вышли из домашней работы.");
                break;
            } else {
                System.out.println("Некорректный ввод!");
            }
        }
    }

    public static void task1() {
        String str1 = "\"name\":\"Ivanov\", \"country\":\"Russia\", \"city\":\"Moscow\", \"age\":\"null\"";
        String[] strings = str1.replaceAll("\"", "").replaceAll(":", " = ").split(",");
        StringBuilder builder1 = new StringBuilder();
        builder1.append(strings[0]).append(",").append(strings[1]).append(",").append(strings[2]).append(".");
        System.out.println(builder1);
    }

    public static void task2() {
        try {
            File logFile = new File("log.txt");
            FileWriter fileWriter = new FileWriter(logFile);
            int[] array = new int[10];
            for (int i = 0; i < array.length - 1; i++) {
                array[i] = new Random().nextInt(15);

            }
            System.out.println("Неотсортированный массив: " + Arrays.toString(array));

            for (int i = 0; i < array.length - 1; i++) {
                for (int j = 0; j < array.length - i - 1; j++) {
                    if (array[j + 1] < array[j]) {
                        int temp = array[j];
                        array[j] = array[j + 1];
                        array[j + 1] = temp;
                        fileWriter.write(Arrays.toString(array) + "\n");
                    }
                }
            }
            fileWriter.close();
            System.out.println("Отсортированный массив: " + Arrays.toString(array) + ".\nРезультат каждой итерации сортировки записан в файл 'log.txt'");
        } catch (Exception e) {
            System.out.println("Что то пошло не так...");
        }
    }

    public static void task3() {
        String str1 = "{\"фамилия\":\"Иванов\",\"оценка\":\"5\",\"предмет\":\"Математика\"},{\"фамилия\":\"Петрова\"," +
                "\"оценка\":\"4\",\"предмет\":\"Информатика\"},{\"фамилия\":\"Краснов\",\"оценка\":\"5\",\"предмет\":\"Физика\"}";
        str1 = str1.replaceAll("фамилия", "Студент ").
                replaceAll("\"", "").
                replaceAll("оценка", " получил ").
                replaceAll("предмет", " по предмету ").
                replaceAll("\\p{P}", "").
                replaceAll("аС", "а=С");
        String[] strings = str1.split("=");
        StringBuilder builder1 = new StringBuilder();
        builder1.append(strings[0]).append(".\n").append(strings[1]).append(".\n").append(strings[2]).append(".");
        System.out.println(builder1);
    }

    public static void task4() {
        try {
            File logFile = new File("text.txt");
            FileWriter fileWriter = new FileWriter(logFile);
            System.out.println("Введите число: ");
            double a = Integer.parseInt(scanner.nextLine());
            while (true) {
                System.out.println("Введите действие (+, -, *, /), для выхода нажмите 'e'");
                char oper = scanner.next().charAt(0);
                ;
                if (oper == '+') {
                    System.out.println("Введите число: ");
                    double b = scanner.nextInt();
                    fileWriter.write(a + " " + oper + " " + b);
                    a += b;
                } else if (oper == '-') {
                    System.out.println("Введите число: ");
                    double b = scanner.nextInt();
                    fileWriter.write(a + " " + oper + " " + b);
                    a -= b;
                } else if (oper == '*') {
                    System.out.println("Введите число: ");
                    double b = scanner.nextInt();
                    fileWriter.write(a + " " + oper + " " + b);
                    a *= b;
                } else if (oper == '/') {
                    System.out.println("Введите число: ");
                    double b = scanner.nextInt();
                    fileWriter.write(a + " " + oper + " " + b);
                    a /= b;
                } else if (oper == 'e' || oper == 'е') {
                    System.out.println("Вы вышли из калькулятора, все действия записаны в 'text.txt' файл");
                    scanner.nextLine();
                    break;
                } else {
                    System.out.println("Вы ввели неверное действие!");
                }
                fileWriter.write(" = " + a + "\n");

                System.out.println("Результат равен: " + a);
            }
            fileWriter.close();
        } catch (Exception e) {
            System.out.println("Что то пошло не так...");
        }
    }
}