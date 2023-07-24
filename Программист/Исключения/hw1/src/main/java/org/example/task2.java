package org.example;

public class task2 {
    public static void main(String[] args) {
        int[] a = new int[]{1, 2, 3};
        int[] b = new int[]{1, 2, 3};
        int[] c = new int[3];
        if (a.length!=b.length)
            System.out.println(new int[1]);
        else {
            for (int i = 0; i < a.length; i++) {
                c[i] = a[i] - b[i];
            }
            for (int i = 0; i < c.length; i++) {
                System.out.println(c[i]);
            }
        }


    }

}
