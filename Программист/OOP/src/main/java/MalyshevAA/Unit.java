package MalyshevAA;

public abstract class Unit {
    private String name;

    private int physicalAttack;
    private int physicalDefense;
    private int magicDefense;
    private int health;
    private int speed;

    public Unit(String name, int physicalAttack, int physicalDefense,
                int magicDefense, int health, int speed) {
        this.name = name;
        this.physicalAttack = physicalAttack;
        this.physicalDefense = physicalDefense;
        this.magicDefense = magicDefense;
        this.health = health;
        this.speed = speed;

    }

    public int getHealth() {
        return health;
    }

    public String getName() {
        return name;
    }

    public int getPhysicalAttack() {
        return physicalAttack;
    }

    public int getMagicDefense() {
        return magicDefense;
    }

    public int getPhysicalDefense() {
        return physicalDefense;
    }

    public int getSpeed() {
        return speed;
    }
}
