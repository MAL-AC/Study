package MalyshevAA;

import java.util.Scanner;

public class Main {

    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        boolean f = true;

        while(true){
            System.out.println("Укажите номер задачи:");
            System.out.println("1 - Задача 1:");
            System.out.println("2 - Задача 2:");
            System.out.println("3 - Задача 3:");
            System.out.println("0 - Завершение работы приложения");
            System.out.print("Введите номер задачи: ");
            int no = Integer.parseInt(scanner.nextLine());

            if (no == 1){
                printName();
            }
            else if (no == 2){
                task2();
            }
            else if (no == 3){
                String str = "Добро пожаловать на курс по Java";
                task3(str);
            }
            else if (no == 0){
                //f = false;
                System.out.println("Завершение работы приложения.");
                break;
            }
        }
    }

    /*
     * Написать программу, которая запросит пользователя ввести <Имя> в консоли.
     * Получит введенную строку и выведет в консоль сообщение “Привет, <Имя>!”
     */
    public static void printName(){
        int i = 12;
        double d = 12.1;
        boolean f = true;
        System.out.print("Введите ваше имя: ");
        String name = scanner.nextLine();
        System.out.println("Привет, " + name + "!");
    }

    /*
     * Дан массив двоичных чисел, например [1,1,0,1,1,1,0,1], вывести
     * максимальное количество подряд идущих 1.
     */
    public static void task2(){

        int[] array = new int[5];
        array[0] = 1;
        array[1] = 0;
        array[2] = 1;
        array[3] = 1;
        array[4] = 0;

        int[] array2 = {1, 0, 1, 0, 1, 1 ,1, 0, 1, 1};


        int max = 0;
        int counter = 0;
        for (int e : array2) {
            if (e == 1){
                counter++; // counter = counter + 1;
            }
            else{
                if (counter > max){
                    max = counter;
                }
                counter = 0;
            }
        }

        String str = "Hello!";
        double index = 14.43455;

        System.out.println("Максимальное кол-во подряд идущих единиц: " + max);
        System.out.printf("Максимальное кол-во подряд идущих единиц: %d   %s    %.2f\n", max, str, index);
        System.out.printf("Максимальное кол-во подряд идущих единиц: %d   %s    %.2f\n", max, str, index);
        System.out.printf("Максимальное кол-во подряд идущих единиц: %d   %s    %.2f\n", max, str, index);
        System.out.printf("Максимальное кол-во подряд идущих единиц: %d   %s    %.2f\n", max, str, index);
    }

    /*
     * * Во фразе "Добро пожаловать на курс по Java" переставить слова в обратном порядке.
     */
    static void task3(String str){
        String[] words = str.split(" ");
        for (int i = words.length - 1; i >= 0; i--){

            System.out.printf("%s ", words[i]);
        }

        System.out.println();

        for (int i = words.length - 1; i >= 0; i--){
            System.out.print(words[i] + " ");
        }

        System.out.println();
    }

}


