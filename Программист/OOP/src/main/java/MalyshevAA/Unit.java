package MalyshevAA;

import java.util.ArrayList;
import java.util.Random;

public abstract class Unit implements Interface {
    private String name;
    private int damage;
    private int maxHp;
    private int hp;
    private int speed;
    Coordinates coordinates;

    public Unit(String name, int damage, int maxHp, int hp, int speed, int x, int y) {
        this.name = name;
        this.damage = damage;
        this.maxHp = maxHp;
        this.hp = hp;
        this.speed = speed;
        coordinates = new Coordinates(x,y);

    }

    @Override
    public String getInfo() {
        return String.format("%s %s hp:%d",getType(), name, hp);
    }

    public Unit nearest(ArrayList<Unit> units) {
        double nearestDistance = Double.MAX_VALUE;
        Unit nearestEnemy = null;
        for (int i = 0; i < units.size(); i++) {
            if(coordinates.countDistance(units.get(i).coordinates) < nearestDistance) {
                nearestEnemy = units.get(i);
                nearestDistance = coordinates.countDistance(units.get(i).coordinates);
            }
        }
        return nearestEnemy;
    }
    public void HP_damage(int damage) {
        hp -= damage;
        if (hp < 0) hp = 0;
        if (hp > maxHp) hp = maxHp;
    }
    public int getHp() {
        return hp;
    }

    public int getDamage() {
        return damage;
    }

    public static String setName() {
        return (Names.values()[new Random().nextInt(Names.values().length)].toString());
    }

    public String getName() {
        return name;
    }
    public String getType(){
        return "";
    }

    public int getSpeed() {
        return speed;
    }
}