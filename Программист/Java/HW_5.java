import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.jar.Attributes.Name;

public class HW_5 {
    public static void main(String[] args) {

        HashMap<String, String> map = new HashMap<>();

        map.merge("Ivan", "123", (o, n) -> o == null ? n : o + " " + n);
        map.merge("Alex", "777", (o, n) -> o == null ? n : o + " " + n);
        map.merge("Anton", "753", (o, n) -> o == null ? n : o + " " + n);
        map.merge("Sergey", "789", (o, n) -> o == null ? n : o + " " + n);

        ArrayList<String> list = new ArrayList<>();
        for (String s : map.keySet()) {
            list.add(s);
        }
        Collections.sort(list, (o1, o2) -> map.get(o2).split(" ").length - map.get(o1).split(" ").length);
        System.out.println(list);
    }
}
