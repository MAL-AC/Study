package ru.geekbrains.lesson1;

import java.util.ArrayList;
import java.util.concurrent.atomic.AtomicInteger;

public class Program {

    public static void main(String[] args) {

        int lastNumber = 43;
        AtomicInteger counter = new AtomicInteger();
        System.out.printf("(1) Сумма всех чисел от 1 до %d равна %d\n", lastNumber,  sum(lastNumber, counter));
        System.out.println("Кол-во итераций: " + counter.get());

        System.out.printf("(2) Сумма всех чисел от 1 до %d равна %d\n", lastNumber,  sumV2(lastNumber));

        counter.set(0);
        System.out.printf("Простые числа в диапазоне от 1 до %d:\n%s\n", lastNumber,
                findSimpleNumbers(lastNumber, counter));
        System.out.println("Кол-во итераций: " + counter.get());

        f(4);



        long startTime = System.currentTimeMillis();
        System.out.printf("Число Фибоначчи для номера %d равно: %d (РЕКУРСИЯ)\n", lastNumber, fb1(lastNumber, counter));
        System.out.println("Кол-во итераций: " + counter.get());
        long endTime = System.currentTimeMillis();
        System.out.printf("Операция выполнена за %d мс.", endTime - startTime);

        counter.set(0);
        startTime = System.currentTimeMillis();
        System.out.printf("Число Фибоначчи для номера %d равно: %d\n", lastNumber, fb2(lastNumber, counter));
        System.out.println("Кол-во итераций: " + counter.get());
        endTime = System.currentTimeMillis();
        System.out.printf("Операция выполнена за %d мс.", endTime - startTime);
    }

    /**
     * [1] Необходимо написать алгоритм, считающий сумму всех чисел от 1 до N.
     */
    public static int sum(int lastNumber, AtomicInteger c){
        int sum = 0;
        for (int i = 1; i <= lastNumber; i++){
            sum += i; // sum = sum + i;
            c.getAndIncrement(); // c++;
        }
        return sum;
    }

    public static int sumV2(int lastNumber){
        return ((1 + lastNumber) * lastNumber) / 2;
    }

    /**
     * Написать алгоритм поиска простых чисел (делятся только на себя и на 1)
     */
    public static ArrayList<Integer> findSimpleNumbers(int lastNumber, AtomicInteger counter){
        ArrayList<Integer> arrayList = new ArrayList<>();

        for (int i = 1; i <= lastNumber; i++){
            boolean simple = true;
            for (int j = 2; j < i; j++){
                counter.getAndIncrement();
                if (i % j == 0){
                    simple = false;
                    break;
                }
            }

            if (simple){
                arrayList.add(i);
            }
        }
        return arrayList;
    }


    /**
     * n = 4;
     * @param n
     */
    static void f(int n){
        System.out.println(n);
        if (n >= 3){
            f(n - 1);
            f(n - 2);
            f(n - 2);
        }
    }

    /**
     * [3] Разработать алгоритм поиска нужного числа последовательности Фибоначчи
     *
     * 0 1 2 3 4 5 6  7  8  9 10
     *
     * 0 1 1 2 3 5 8 13 21 34 55 ...
     *
     */
    public static long fb1(int num, AtomicInteger counter){
        counter.getAndIncrement();
        if (num == 0 || num == 1)
            return num;
        return fb1(num - 1, counter) + fb1(num - 2, counter);
    }

    public static int fb2(int num, AtomicInteger counter){
        if (num == 0 || num == 1)
            return num;
        int[] array = new int[num + 1];
        array[0] = 0;
        array[1] = 1;
        for (int i = 2; i < array.length; i++){
            counter.getAndIncrement();
            array[i] = array[i - 1] + array[i - 2];
        }
        return array[num];
    }

}
