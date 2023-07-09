package ru.geekbrains.lesson6;

import java.util.*;

public class Program {

    static Random random = new Random();

    public static void main(String[] args) {
        task1();
        task2();
        task3();
    }

    public static void task3(){
        Fraction fraction1 = new Fraction(3, 4);
        //fraction1.numerator = 3;
        //fraction1.denominator = 4;
        System.out.println(fraction1);

        Fraction fraction2 = new Fraction();
        fraction2.setNumerator(1);
        fraction2.setDenominator(3);
        System.out.println(fraction2);
        System.out.println(fraction2.getDenominator());

        Fraction fraction3 = fraction2.plus(fraction1);
        Fraction fraction4 = fraction1.plus(fraction2);

        System.out.println(fraction1.getFraction()  + " + " + fraction2.getFraction() + " = " + fraction4.getFraction());

        Fraction fraction5  = Fraction.plus(fraction4, fraction1);
        System.out.println(fraction4  + " + " + fraction1 + " = " + fraction5);

        HashSet<Fraction> hashSet = new HashSet<>();
        hashSet.add(new Fraction(3, 4));
        hashSet.add(new Fraction(-1, 2));
        hashSet.add(new Fraction(3, 4));
        hashSet.add(new Fraction(5, 7));
        hashSet.add(new Fraction(3, 4));
        hashSet.add(new Fraction(4, 9));
        System.out.println(hashSet);
        System.out.println(new Fraction(3, 4).equals(new Fraction(3, 4)));
    }

    /**
     * Задача:
     * 1. Напишите метод, который заполнит массив из 1000 элементов случайными цифрами от 0 до 24.
     * 2. Создайте метод, в который передайте заполненный выше массив и с помощью Set
     * вычислите процент уникальных значений в данном массиве
     * и верните его в виде числа с плавающей запятой.
     * Для вычисления процента используйте формулу:
     * процент уникальных чисел = количество уникальных чисел * 100 / общее количество чисел в массиве.
     */
    public static void task2(){
        Integer[] array = new Integer[10];
        for (int i = 0; i < array.length; i++){
            array[i] = random.nextInt(0, 25);
        }
        calc(array);
    }

    public static void  calc(Integer[] array){
        HashSet<Integer> hashSet = new HashSet<>(Arrays.asList(array));
        //hashSet.addAll(Arrays.asList(array))
        System.out.println("% уникальных чисел: " + (double)hashSet.size() * 100 / array.length);
    }


    public static void task1(){
        HashSet<Integer> hashSet1 = new HashSet<>();
        LinkedHashSet<Integer> linkedHashSet1 = new LinkedHashSet<>();
        TreeSet<Integer> treeSet = new TreeSet<>();
        int size = random.nextInt(10, 21);
        System.out.println("Общее кол-во элементов: " + size);
        System.out.print("Случайные числа: ");
        for (int i = 0; i < size; i++){
            int number = random.nextInt(-9, 10);
            System.out.printf("%d ", number);
            hashSet1.add(number);
            linkedHashSet1.add(number);
            treeSet.add(number);
        }
        System.out.println();
        System.out.println("HashSet: " + hashSet1);
        System.out.println("LinkedHashSet: " + linkedHashSet1);
        System.out.println("TreeSet: " + treeSet);
    }

}
