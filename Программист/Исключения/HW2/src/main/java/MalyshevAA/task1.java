package MalyshevAA;


import java.util.Scanner;

/*
Реализуйте метод, который запрашивает у пользователя ввод дробного числа (типа float),
и возвращает введенное значение. Ввод текста вместо числа не должно приводить к падению приложения,
вместо этого, необходимо повторно запросить у пользователя ввод данных.
 */
public class task1 {
    public static void main(String[] args) {
        Number();
    }

    public static float Number() {
        try {
            Scanner in = new Scanner(System.in);
            System.out.println("Введите число:");
            float num = in.nextFloat();
            System.out.println(num);
            return num;
        } catch (Exception e) {
            System.out.println("Некорректный ввод данных, повторите");
            Number();
            return 0;
        }
    }
}