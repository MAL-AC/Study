package MalyshevAA;

public class task2 {
    public static void main(String[] args) {
        try {
            int d = 5;
            int[] intArray = new int[]{1,2,3,4,5,6,7,8,9};
            double catchedRes1 = (double)intArray[8] / d;
            System.out.println("catchedRes1 = " + catchedRes1);
        } catch (ArithmeticException e) {
            System.out.println("Catching exception: " + e);
        }
    }
}
