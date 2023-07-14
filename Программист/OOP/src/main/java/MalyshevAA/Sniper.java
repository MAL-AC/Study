package MalyshevAA;

import java.util.ArrayList;

public class Sniper extends ClassShooters{
    public Sniper(String name, int x, int y) {
        super(name, 12, 100, 100, 300, 5, x, y);
    }

    @Override
    public String getType(){
        return "Sniper";
    }
}

