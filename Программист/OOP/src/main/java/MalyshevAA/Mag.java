package MalyshevAA;

import java.util.ArrayList;
import java.util.Comparator;

public class Mag extends ClassMagic {
    private int heal;
    public Mag(String name, int x, int y) {
        super(name, 10, 100, 100, 3, x,y);
        this.heal = -10;
    }

    public int getHeal() {
        return heal;
    }

    @Override
    public void step(ArrayList<Unit> units, ArrayList<Unit> team) {
        if (getState() == "alive") {
            float min_XP = Integer.MAX_VALUE;
            int index = 0;
            for (int i = 0; i < team.size(); i++) {
                if ((float) (team.get(i).getHp() / getMaxHp()) < min_XP) {
                    min_XP = (float) (team.get(i).getHp() / getMaxHp());
                    index = i;
                }
                team.get(index).HP_damage(getHeal());
//            team.sort(Comparator.comparing(Unit::getHp));
//            team.get(0).HP_damage(getHeal());
            }
        }
    }
//    float min_XP = Integer.MAX_VALUE;
//    int index = 0;
//            for (int i = 0; i < team.size(); i++) {
//        if ((float) (team.get(i).hp / max_hp) < min_XP) {
//            min_XP = (float) (team.get(i).hp / max_hp);
//            index = i;
//        }
//    }
//            team.get(index).HP_damage(this.damage);
//}
//    }

    @Override
    public String getType(){
        return "Mag";
    }
}

