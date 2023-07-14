package MalyshevAA;

import java.util.ArrayList;

public class Peasant extends ClassSuppurt{
    public Peasant(String name, int x, int y) {
        super(name, 0, 10, 10, 5, x, y);
    }

    @Override
    public void step(ArrayList<Unit> units, ArrayList<Unit> team) {

    }

    public String getType(){
        return "Peasant";
    }
}
