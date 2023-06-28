package ru.geekbrains.api.lesson3;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
import java.util.Iterator;


public class Program{


        static final String[] words = {"apple", "orange", "lemon", "banana", "pepper", "avocado", "broccoli", "carrot", "cherry",
            "apple", "apple", "melon", "apple", "kiwi", "mango", "mushroom", "lemon", "olive", "carrot", "peanut",
            "banana", "pepper", "lemon", "pumpkin", "apple"};


    static Random random = new Random();


    public static void task2(){
        ArrayList<String> arrayList = new ArrayList<>();
        Collections.addAll(arrayList, words);
        for (int i = arrayList.size() - 1; i >= 0; i--)
            for (int j = arrayList.size() - 1; j >= 0; j--)
                if (i != j && arrayList.get(i).equals(arrayList.get(j))){
                        arrayList.remove(i);
                        break;
                }
        System.out.println(arrayList);
    }

    public static void task2_2(){
        ArrayList<String> arrayList = new ArrayList<>();
        Collections.addAll(arrayList, words);
        Collections.sort(arrayList);
        String prev = null;
        Iterator<String> iterator =  arrayList.iterator();
        while(iterator.hasNext()){
            String word = iterator.next();
            if (word.equals(prev))
                iterator.remove();
            else
                prev = word;
        }

        System.out.println(arrayList);
    }



    /**
     * Заполнить список десятью случайными числами. Отсортировать список методом sort() и вывести его на экран.
     */
    public static void task1(){
         int size = random.nextInt(10, 21);
         ArrayList<Integer> arrayList = new ArrayList<>(100);
         for (int i = 0; i < size; i++){
            arrayList.add(random.nextInt(-9, 10));
         }
         System.out.println(arrayList);
         Collections.sort(arrayList);
          System.out.println(arrayList);
    }


    public static void main(String[] args) {

        task2_2();
        task1();

        int a = 12;
        int b = -7;
        int c = 12;


        Person person1 = new Person();
        person1.name = "User";
        person1.age = 30;

        
        Person person2 = new Person();
        person2.name = "User";
        person2.age = 30;

        String str1 = "Hello!";
        String str2 = "Hello!";
        String str3 = "Hello!";
        String str4 = "Hello!";
        String str5 = "He" + "ll" + "o!";
        String str6 = new String("Hello!");

        System.out.println(a + " " + b + " " + str1 + " " + false + " " + person2);

        System.out.println(a == c);
        System.out.println(person1 == person2);
        System.out.println(person1.equals(person2));
        System.out.println(str1 == str6);
        System.out.println(str1.equals(str6));

        ArrayList list = new ArrayList();
        list.add(str3);
        list.add(person1);
        list.add(person2);
        list.add(12);
        list.add(true);
        list.add('c');

   

        for (Object element : list) {
            if (element instanceof Person){
                Person p = (Person)element;
                System.out.println("Возраст: " + p.age);
            }
            
        }


        Object[] strArr = new Object[1000];
        MyList myList = new MyList(strArr);
        myList.add("123");
        myList.add(12);
        myList.add(false);


        Person[] personArr = new Person[1000];

        PersonList personList = new PersonList(personArr);
        personList.add(person2);
        personList.add(person1);

        MyList<Person> list2 = new MyList<Person>(personArr);
        list2.add(person2);
        //list2.add("asdasdasd");
        


    }

}



class PersonList{
    Person[] arr;
    int capacity;
    int size = 0;

    public PersonList(Person[] arr){
        this.arr = arr;
        capacity = arr.length;
    }

    public void add(Person obj){
        arr[size] = obj;
        size++;
    }

}


class MyList<E>{
    E[] arr;
    int capacity;
    int size = 0;

    public MyList(E[] arr){
        this.arr = arr;
        capacity = arr.length;
    }

    public void add(E obj){
        arr[size] = obj;
        size++;
    }

}

class Person{
    String name;
    int age;

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Person){
            Person p =  (Person)obj;
            if (age == p.age)
                return true;
            else
                return false;
        }
        else
            return false;
    }

    @Override
    public String toString() {
        return "[" + name + "; " + age + "]";
        //return super.toString();
    }

}

