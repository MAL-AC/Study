package MalyshevAA;

import java.util.ArrayList;

public abstract class ClassSuppurt extends Unit{
    public ClassSuppurt(String name, int damage, int maxHp, int hp, int speed, int x, int y) {
        super(name, damage, maxHp, hp, speed, x, y);
        this.standby = true;
    }
        public boolean getStandBy(){
        return standby;
    };
    @Override
    public void step(ArrayList<Unit> units, ArrayList<Unit> team) {
        if (getState() == "dead") return;
    }

}
