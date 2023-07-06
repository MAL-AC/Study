package MAlyshevAA;

import java.util.LinkedList;
import java.util.Random;
import java.util.Scanner;

public class Main {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Добро пожаловать на решенея домашней работы № 4.");
        while (true) {
            System.out.println("\nЗадание 1: Пусть дан LinkedList с несколькими элементами. Реализуйте метод, который вернет “перевернутый” список.");
            System.out.println("Задание 2: . Реализуйте очередь с помощью LinkedList со следующими методами:\n" +
                    "enqueue() - помещает элемент в конец очереди,\n" +
                    "dequeue() - возвращает первый элемент из очереди и удаляет его,\n" +
                    "first() - возвращает первый элемент из очереди, не удаляя.");
            System.out.println("Укажите номер задания или введите 0 для выхода: ");
            int no = Integer.parseInt(scanner.nextLine());
            if (no == 1) {
                task1();
            } else if (no == 2) {
                task2();
            } else if (no == 0) {
                System.out.println("Вы вышли из домашней работы.");
                break;
            } else {
                System.out.println("Некорректный ввод!");
            }
        }
    }

    public static void task1() {
        LinkedList list = new LinkedList();
        list.add("H");
        list.add("O");
        list.add("M");
        list.add("E");
        System.out.println(list);
        LinkedList reverslist = new LinkedList();
        for (int i = list.size() - 1; i >= 0; i--) {
            reverslist.add(list.get(i));
        }
        System.out.println(reverslist);
    }

    public static void task2() {
        LinkedList<Integer> list = new LinkedList<>();
        for (int i = 0; i < 10; i++)
            list.add(new Random().nextInt(15)); //заполняем случайными числами

        System.out.println("Список заполненный случайными числами: " + list);
        System.out.println("Помещение случайного числа в конец очереди: " + enqueue(list, new Random().nextInt(15)));
        System.out.print("Удалёно первое число: " + dequeue(list)); // удалили первый элемент
        System.out.println(". Результат: " + list);
        System.out.print("Первое число без удаления : " + first(list));
        System.out.println(". Результат: " + list);
    }

    public static LinkedList<Integer> enqueue(LinkedList<Integer> list, int num) {// помещает элемент в конец очереди
        list.addLast(num);
        return list;
    }

    public static int dequeue(LinkedList<Integer> list) {
        int num = list.get(0);
        list.remove(0);
        return num;
    }

    public static int first(LinkedList<Integer> list) {
        int num = list.get(0);
        return num;
    }
}
