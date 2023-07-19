package MalyshevAA;

import java.util.ArrayList;
import java.util.Random;

public abstract class ClassMagic extends Unit {
    public int mana;
    public ClassMagic(String name, int damage,int moveDistance, int maxHp, int hp, int speed,int mana, int x, int y) {
        super(name, damage,moveDistance, maxHp, hp, speed, x, y);
        this.mana = mana;
    }
    public int getMana() {
        return mana;
    }
    @Override
    public void step(ArrayList<Unit> units, ArrayList<Unit> team) {
        if (getState() == "dead") return;
    }
}



