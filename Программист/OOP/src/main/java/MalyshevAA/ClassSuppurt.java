package MalyshevAA;

public abstract class ClassSuppurt extends Unit{
    public int delivery;
    public ClassSuppurt(String name, int physicalAttack, int physicalDefense,
                        int magicDefense, int health, int speed, int delivery) {
        super(name, physicalAttack, physicalDefense, magicDefense, health, speed);
        this.delivery = delivery;
    }

    public int getDelivery() {
        return delivery;
    }
}
