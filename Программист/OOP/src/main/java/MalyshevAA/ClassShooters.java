package MalyshevAA;

public abstract class ClassShooters extends Unit {
    public int shoots;
    public ClassShooters(String name, int physicalAttack, int physicalDefense,
                         int magicDefense, int health, int speed, int shoots) {
        super(name, physicalAttack, physicalDefense, magicDefense, health, speed);
        this.shoots = shoots;
    }

    public int getShoots() {
        return shoots;
    }
}
