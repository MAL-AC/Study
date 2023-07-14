package MalyshevAA;

import java.util.ArrayList;

public class Robber extends ClassInfantry {
    public Robber(String name, int x, int y) {
        super(name, 12, 100, 100, 5, x, y);
    }


    @Override
    public String getType(){
        return "Robber";
    }
}