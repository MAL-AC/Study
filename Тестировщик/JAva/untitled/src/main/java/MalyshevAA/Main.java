package MalyshevAA;

import java.util.*;

public class Main {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        System.out.println("Добро пожаловать на решения домашней работы № 1.");
        while (true) {
            System.out.println("\nЗадание 4: Пусть дан произвольный список целых чисел.");
            System.out.println("Задание 1: Удалить из него чётные числа.");
            System.out.println("Задание 2: Найти минимальное значение.");
            System.out.println("Задание 3: Найти максимальное значение");
            System.out.println("Задание 4: Найти среднее значение.");
            System.out.println("Укажите номер задания или введите 0 для выхода: ");
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

    public class ReturnArrayList {
        public static ArrayList<Integer> myList() {
            ArrayList<Integer> list = new ArrayList<>();
            for (int i = 0; i < 10; i++)
                list.add(new Random().nextInt(15));
            return list;
        }

    }

    public static void task1() {
        ArrayList<Integer> list = ReturnArrayList.myList();
        System.out.println("Список из случайных значений: " + list);
        ListIterator<Integer> iterator = list.listIterator();
        while (iterator.hasNext()) {
            Integer i = iterator.next();
            if (i % 2 == 0)
                iterator.remove();
        }
        System.out.println("Список из нечетных значений: " + list);
    }

    public static void task2() {
        ArrayList<Integer> list = ReturnArrayList.myList();
        System.out.println("Список из случайных значений: " + list);
        Collections.sort(list);
        System.out.println("Минимальное значение: " + list.get(0));

    }

    public static void task3() {
        ArrayList<Integer> list = ReturnArrayList.myList();
        System.out.println("Список из случайных значений: " + list);
        Collections.sort(list);
        System.out.println("Максимальное значение: " + list.get(list.size() - 1));
    }

    public static void task4() {
        ArrayList<Integer> list = ReturnArrayList.myList();
        System.out.println("Список из случайных значений: " + list);
        Collections.sort(list);
        System.out.println("Среднее значение: " + list.get(list.size() / 2));
        int sum = 0;
        for (int i = 0; i < list.size(); i++)
            sum += list.get(i);
        float midl = (float) sum / list.size();
        System.out.println("Среднее арифметическое значение: " + midl);
    }
}
