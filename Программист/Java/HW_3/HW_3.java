import java.util.ArrayList;
import java.util.Collections;
import java.util.ListIterator;
import java.util.Random;


public class HW_3 {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            list.add(new Random().nextInt(15));
        }
        System.out.println("Список из случайных значений: " + list);

        ListIterator<Integer> iterator = list.listIterator();
        int sum = 0;
        while (iterator.hasNext()) {
            Integer i = iterator.next();
            
            if (i % 2 == 0) {
                iterator.remove();
            }
            else sum+=i;
        }
        System.out.println("Список из нечетных значений: " + list);
        Collections.sort(list);
    
        System.out.println("Минимальное значение: " + list.get(0));
        System.out.println("Максимальное значение: " + list.get(list.size() - 1));
        System.out.println("Среднее значение: " + list.get(list.size() / 2));
        float midl = (float)sum/list.size();
        System.out.println("Среднее арифметическое значение: "+ midl);
    }

}