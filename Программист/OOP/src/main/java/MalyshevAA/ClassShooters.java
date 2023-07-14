package MalyshevAA;

import java.util.ArrayList;
import java.util.List;

public abstract class ClassShooters extends Unit {
    private int shoots;

    public ClassShooters(String name, int damage, int maxHp, int hp, int speed, int shoots, int x, int y) {
        super(name, damage, maxHp, hp, speed, x, y);
        this.shoots = shoots;
    }

    public int doShootDamage() {
        return getDamage();
    }


    @Override
    public void step(ArrayList<Unit> units, ArrayList<Unit> team) {
        if (getState() == "dead" || this.shoots == 0) return;
        for (Unit unit : team) {
            if (unit.getType().equals("Peasant") && unit.getState() == "alive"&& unit.standby==true ) {
                if (unit.getHp() > 0) {
                    shoots++;
                    unit.standby = false;
                    break;
                }
            }
        }
            nearest(units).HP_damage(doShootDamage());
            shoots -= 1;
            return;
    }

    @Override
    public String getInfo() {
        return String.format("%s %s hp:%d shoots:%d", getType(), getName(), getHp(), shoots);
    }
}

