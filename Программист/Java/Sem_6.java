import java.util.ArrayList;
import java.util.HashMap;

public class Sem_6 {
    public static void main(String[] args) {
        SetImitation setImitation = new SetImitation();
        System.out.println(setImitation.add(9));
        System.out.println(setImitation.add(9));
        System.out.println(setImitation.add(2));
    

    }
}

class SetImitation<E> {
    private HashMap<E, Object> list = new HashMap();
    private final Object OBJECT = new Object();
    public boolean add(E num) {
        return list.put(num, OBJECT) == null;
    }
}
