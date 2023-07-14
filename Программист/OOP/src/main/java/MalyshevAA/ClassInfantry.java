package MalyshevAA;

import java.util.ArrayList;

public abstract class ClassInfantry extends Unit {
    public ClassInfantry(String name, int damage, int maxHp, int hp, int speed, int x, int y) {
        super(name, damage, maxHp, hp, speed, x, y);
    }
    @Override
    public void step(ArrayList<Unit> units, ArrayList<Unit> team) {
        if (getState() == "dead") return;
    }

}

