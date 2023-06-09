//Напишите программу, чтобы найти вхождение в строке (содержащей все символы другой строки).
import java.util.Scanner;


//public class sem_2 {
//    public static void main(String[] args){
//        Scanner scanner = new Scanner(System.in);
//        System.out.println("Input first str: ");
//        String s1 = scanner.nextLine();
//        System.out.println("Input second str: ");
//        String s2 = scanner.nextLine();
//        scanner.close();
//
//        System.out.println(s1.contains(s2));
//
//    }
//}
////Напишите программу, чтобы проверить,
//        являются ли две данные строки вращением друг
//        друга (вхождение в обратном порядке).

public class sem_2 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Input first str: ");
        StringBuilder s1 = new StringBuilder(scanner.nextLine());
        System.out.println("Input second str: ");
        StringBuilder s2 = new StringBuilder(scanner.nextLine());
        scanner.close();

        System.out.println(s1);

    }
}