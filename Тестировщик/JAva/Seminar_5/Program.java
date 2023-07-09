package ru.geekbrains.lesson5;

import java.util.*;

public class Program {

    public static void main(String[] args) {

        System.out.println(task2("egg", "add"));
        System.out.println(task2("paper", "title"));
        System.out.println(task2("kick", "side"));
        System.out.println(task2("foo", "bar"));

        String[] data = {
                "321456 Васильев",
                "234561 Петрова",
                "234432 Иванов",
                "123456 Петрова",
                "345678 Иванов",
                "123456 Иванов",
        };

        task1V1(data);
        task1V2(data);


        String[] students = {
                "Григорьев Анатолий 4 5 2",
                "Фокин Глеб 1 5 2",
                "Шестаков Клим 4 3 2",
                "Хохлов Мартин 2 5 2",
                "Шубин Лазарь 4 5 2",
                "Гущина Арьяна 4 3 3",
                "Брагина Виоланта 2 5 2",
                "Афанасьева Екатерина 1 1 2",
                "Рыбакова Снежана 4 2 2",
                "Лазарева Алла 4 3 2",
                "Бирюков Владлен 4 5 2",
                "Копылов Панкратий 4 4 4",
                "Горбунов Рубен 4 5 3",
                "Лыткин Герман 1 5 2",
                "Соколов Орест 1 1 5"

                //...
        };

        //Student student1 = new Student("Алла", "Лазарева", 4.3);
        //System.out.println(student1);
        task3(students);
    }

    static HashMap<Double, List<Student>> statistics = new HashMap<>();

    static void task3(String[] students){
        for (String studentStr : students){
            String[] studentParts = studentStr.split(" ");
            int a = Integer.parseInt(studentParts[2]);
            int b = Integer.parseInt(studentParts[3]);
            int c = Integer.parseInt(studentParts[4]);
            double r = (double) (a + b + c) / 3;

            Student student = new Student(studentParts[1], studentParts[0], r);

            if (statistics.containsKey(r)){
                statistics.get(r).add(student);
            }
            else {
                ArrayList<Student> lst = new ArrayList<>();
                lst.add(student);
                statistics.put(r, lst);
            }

        }

        TreeMap<Double, List<Student>> sortedStatistics = new TreeMap<>(new RatingComparator());
        sortedStatistics.putAll(statistics);

        System.out.println("\nТОП3 худших средних баллов среди студентов:");
        int counter = 1;
        for (Map.Entry<Double, List<Student>> element : sortedStatistics.entrySet()) {
            System.out.printf("%d место - средний балл %f\n", counter, element.getKey());
            for (Student student : element.getValue()){
                System.out.println(student);
            }
            counter++;
            if (counter > 3)
                break;
        }

        System.out.println();
    }

    static HashMap<String, List<Integer>> personalInformation = new HashMap<>();

    static HashMap<Integer, String> personalInformationV2 = new HashMap<>();

    /**
     * Задача:
     * Создать структуру для хранения Номеров паспортов и Фамилий сотрудников организации.
     * 123456 Иванов
     * 321456 Васильев
     * 234561 Петрова
     * 234432 Иванов
     * 654321 Петрова
     * 345678 Иванов
     * Вывести данные по сотрудникам с фамилией Иванов.
     */
    static  void task1V1(String[] data){
        for (String person : data){
            String[] personParts = person.split(" ");
            if (personalInformation.containsKey(personParts[1])){
                List<Integer> list = personalInformation.get(personParts[1]);
                list.add(Integer.parseInt(personParts[0]));
            }
            else {
                ArrayList<Integer> arrayList = new ArrayList<>();
                arrayList.add(Integer.parseInt(personParts[0]));
                personalInformation.put(personParts[1], arrayList);
            }
        }

        System.out.println("Иванов:");
        System.out.println("~~~~~~~");

        for (Integer no : personalInformation.get("Иванов")) {
            System.out.println(no);
        }

    }

    static  void task1V2(String[] data){
        for (String person : data){
            String[] personParts = person.split(" ");
            if (!personalInformationV2.containsKey(Integer.parseInt(personParts[0]))){
                personalInformationV2.put(Integer.parseInt(personParts[0]), personParts[1]);
            }
        }

        System.out.println("Иванов:");
        System.out.println("~~~~~~~");

        for (Map.Entry<Integer, String> element : personalInformationV2.entrySet())
        {
            if (element.getValue().equals("Иванов")){
                System.out.println(element.getKey());
            }
        }

    }

    /**
     * Задача:
     * Даны 2 строки, написать метод, который вернет true,
     * если эти строки являются изоморфными и false, если нет.
     * Строки изоморфны, если одну букву в первом слове можно
     * заменить на некоторую букву во втором слове, при этом
     *
     * 1. повторяющиеся буквы одного слова меняются на одну и ту же букву с
     * сохранением порядка следования. (Например, add - egg изоморфны)
     * 2. буква может не меняться, а остаться такой же. (Например, note - code)
     *
     * egg add
     * kick side
     *
     */
    static boolean task2(String firstString, String secondString){
        if (firstString.length() != secondString.length())
            return false;

        Map<Character, Character> letterMap = new HashMap<>();

        for (int i = 0; i < firstString.length(); i++){
            char letterFirst = firstString.charAt(i);
            char letterSecond = secondString.charAt(i);

            if (!letterMap.containsKey(letterFirst)){
                letterMap.put(letterFirst, letterSecond);
            }
            else if (letterMap.get(letterFirst) != letterSecond){
                return false;
            }
        }
        return true;
    }

}
