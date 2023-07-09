package MAlyshevAA;

import java.util.HashSet;

public class Main {
    public static void main(String[] args) {
        Cat cat1 = new Cat("Filya", "Maine Coon", 5);
        Cat cat2 = new Cat("Barsik", "Abyssinian", 5);
        Cat cat3 = new Cat("Barsik", "Abyssinian", 5);
        HashSet<Cat> hashSet1 = new HashSet<>();
        hashSet1.add(cat1);
        hashSet1.add(cat2);
        hashSet1.add(cat3);
        for (Cat cat : hashSet1) {
            System.out.println(cat.toString());
        }
        System.out.println(cat2.equals(cat3));
        System.out.println(cat1.equals(cat3));


    }
}