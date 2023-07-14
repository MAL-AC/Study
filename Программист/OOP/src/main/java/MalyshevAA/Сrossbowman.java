package MalyshevAA;

import java.util.ArrayList;

public class Сrossbowman extends ClassShooters {
    public Сrossbowman(String name, int x, int y) {
        super(name, 10, 100, 100, 8, 5, x, y);
    }

    @Override
    public String getType(){
        return "Crossbowman";
    }
}