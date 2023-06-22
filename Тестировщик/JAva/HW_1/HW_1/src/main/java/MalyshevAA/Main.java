package MalyshevAA;

import java.util.Scanner;
import java.util.Random;

public class Main {

    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Добро пожаловать на решенея домашней работы № 1.");


        while (true) {
            System.out.println("Задание 1: Вычислить n-ое треугольного число (сумма чисел от 1 до n), n! (произведение чисел от 1 до n).");
            System.out.println("Задание 2: Вывести все простые числа от 1 до 1000.");
            System.out.println("Задание 3: Реализовать простой калькулятор.");
            System.out.println("Задание 4: Восстановить выражение до верного равенства.");
            System.out.println("Укажите номер задания или введите 0 для выхода: ");
            int no = Integer.parseInt(scanner.nextLine());
            if (no == 1) {
                task1();
            }
            else if (no == 2) {
                task2();
            }
            else if (no == 3) {
                task3();
            }
            else if (no == 4) {
                task1();
            }
            else if(no == 0) {
                break;
            }
            else {
                System.out.println("Некорректный ввод!");
            }
        }
    }

    public static void task1() {
        System.out.println("Введите число n: ");
        int n = Integer.parseInt(scanner.nextLine());
        int sum = 0;
        int prod = 1;
        for (int i = 1; i <= n; i++) {
            sum += i;
            prod *= i;
        }
        System.out.println("Cумма чисел от 1 до n = " + sum + "\nПроизведение чисел от 1 до n = " + prod);
    }

    public static void task2() {
        System.out.println("2 - Простое число");
        for (int i = 2; i <= 1000; i++) {
            int count = 0;
            for (int k = 2; k < i; k++) {
                if (i % k == 0) {
                    break;
                } else {
                    count += 1;
                }
                if (count == i - 2) {
                    System.out.println(i + " - Простое число");
                }
            }
        }
    }

    public static void task3() {
        System.out.println("Введите число: ");
        double a = Integer.parseInt(scanner.nextLine());
        while (true) {
            System.out.println("Введите действие (+, -, *, /), для выхода нажмите 'e'");
            char oper = scanner.next().charAt(0);
            ;
            if (oper == '+') {
                System.out.println("Введите число: ");
                double b = scanner.nextInt();
                a += b;
            } else if (oper == '-') {
                System.out.println("Введите число: ");
                double b = scanner.nextInt();
                a -= b;
            } else if (oper == '*') {
                System.out.println("Введите число: ");
                double b = scanner.nextInt();
                a *= b;
            } else if (oper == '/') {
                System.out.println("Введите число: ");
                double b = scanner.nextInt();
                a /= b;
            } else if (oper == 'e' || oper == 'е') {
                System.out.println("Вы вышли из калькулятора");
                break;
            } else {
                System.out.println("Вы ввели неверное действие!");
            }
            System.out.println("Результат равен: " + a);
        }
    }

    public static void task4() {
        int a = new Random().nextInt(9);
        int b = new Random().nextInt(9);
        int c = new Random().nextInt(200);
        System.out.printf("Задано выражение: %d? + ?%d = %d\n", a, b, c);
        int count = 0;
        for (int i = 1; i < 10; i++) {
            for (int k = 1; k < 10; k++) {
                if ((a * 10 + i) + (k * 10 + b) == c) {
                    count += 1;
                    System.out.println("Решение: " + (a * 10 + i) + "+" + (k * 10 + b) + "=" + c);
                }
            }
        }
        if (count == 0) {
            System.out.println("Решения нет");
        }


    }
}
