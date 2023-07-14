package MalyshevAA;

import java.util.ArrayList;

public class Monk extends ClassMagic {
    public Monk(String name, int x, int y) {
        super(name, 9, 100, 100, 6, x, y);
    }

    @Override
    public void step(ArrayList<Unit> units, ArrayList<Unit> team) {

    }
    @Override
    public String getType(){
        return "Monk";
    }
}
