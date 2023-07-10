package MalyshevAA;

import java.util.ArrayList;

public abstract class ClassShooters extends Unit {
    private int shoots;

    public ClassShooters(String name, int damage, int maxHp, int hp, int speed, int shoots, int x, int y) {
        super(name, damage, maxHp, hp, speed, x, y);
        this.shoots = shoots;
    }


    @Override
    public void step(ArrayList<Unit> units, ArrayList<Unit> team) {
        if (getHp() == 0 || this.shoots == 0) return;
        Unit tmp = nearest(units);
        for (Unit unit : team) {
            if (unit.getClass().equals("class MalyshevAA.Spearman")) {
                shoots++;
                break;
            }
        }
        tmp.HP_damage(getDamage());
        shoots -= 1;
    }

    @Override
    public String getInfo() {
        return String.format("%s hp:%d shoots:%d", getName(), getHp(), shoots);
    }
}
