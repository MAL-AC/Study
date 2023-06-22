// Создать словарь с ключом число и значением - случайное число. 
// Вывести в консоль только пары в которых значение кратно двум!
package Sem5;

import java.util.HashMap;
import java.util.Random;

//Создать словарь с ключом число и значением - случайное число. Вывести в консоль только пары в которых значение кратно двум!
public class Sem5_1 {
    public static void main(String[] args) {
        HashMap<Integer,Integer> map = map1();
        System.out.println(map);
        for (int i: map.values()) {
            if (i % 2 == 0){
                System.out.println(i);
            }
        }


    }
    public static HashMap<Integer,Integer> map1(){
        HashMap<Integer,Integer> map1 = new HashMap<>();
        for (int i = 0; i < 10; i++){
            map1.put(i, new Random().nextInt(10));

        }
        return map1;
    }

}



















List<Person> persons = new ArrayList<>();
    persons.add(new Person("tarun", 28));
    persons.add(new Person("arun", 29));
    persons.add(new Person("varun", 12));
    persons.add(new Person("arun", 22));

    Collections.sort(persons, new Comparator<Person>() {

        public int compare(Person t, Person t1) {
            int comp = t.getFname().compareTo(t1.getFname());
            if (comp != 0) {    // names are different
                return comp;
            }
            return t.getAge() - t1.getAge();
        }
    });
    System.out.println(persons);

}}

// Создать два словаря, ключи это случайные числа до 25 
// а значения первого списка мужские имена а второго женские. 
// Вывести в консоль сумму значений только пар у которых есть ключ в обоих словарях.








import java.util.HashMap;
import java.util.Map;

public class Seminar_5 {
    public static void main(String[] args) {
        Map tb = new HashMap<>(0, 0);

}
}
