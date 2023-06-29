package MalyshevAA;

import java.util.Random;

public abstract class ClassMagic extends Unit {
    public int magicAttack;

    public ClassMagic(String name, int physicalAttack, int physicalDefense,int magicDefense, int health, int speed, int magicAttack) {
        super(name, physicalAttack, physicalDefense, magicDefense, health, speed);
        this.magicAttack = magicAttack;
    }

    public int getMagicAttack() {
        return magicAttack;
    }
}



