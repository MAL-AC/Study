package org.example;

public class Answer {
    public static void arrayOutOfBoundsException() {
        int[] myIntArray = new int[]{1, 2, 3};
        System.out.println(myIntArray[5]);
        //        return myIntArray[9];

    }

    public static void divisionByZero() {
        int a = 5;
        int b = 0;
        System.out.println(a/b);
        //        return a/b;

    }

    public static void numberFormatException() {
        String a = "abc";
        int b = Integer.parseInt(a);
        System.out.println(b);

    }
}