package MalyshevAA;

import java.util.ArrayList;
import java.util.Random;

public abstract class ClassMagic extends Unit {
    public ClassMagic(String name, int damage, int maxHp, int hp, int speed, int x, int y) {
        super(name, damage, maxHp, hp, speed, x, y);
    }
    @Override
    public void step(ArrayList<Unit> units, ArrayList<Unit> team) {
        if (getState() == "dead") return;
    }
}



