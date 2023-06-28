package MalyshevAA;

import java.util.Random;

public class Cat {
    public String name;
    private int age;
    public static boolean isBlack;

    private Cat(String name, int age){
        if (name != null) this.name = name;
        setAge(age);
    }
    public Cat(String name){
        this(name, new Random().nextInt(30));

    }
    public int getAge() {
        return age;
    }
    public static boolean isaCat(){
        return new Random().nextBoolean();
    }
    public boolean setAge(int age) {
        if (age < 0 || age > 30) {
            age = 0;
            return false;
        }
        this.age = age;
        return true;
    }
}
