package MalyshevAA;

import java.util.ArrayList;
import java.util.Random;

import static java.lang.Character.getName;

public class Main {
    public static void main(String[] args) {
//        Mag mag1 = new Mag("Elven");
//        Monk monk1 = new Monk("Don");
//        Peasant peasant1 = new Peasant("Holop");
//        Robber robber1 = new Robber("Karabas");
//        Spearman spearman1 = new Spearman("Born");
//        Sniper sniper1 = new Sniper("Gun");
//        Сrossbowman crossbowman1 = new Сrossbowman("Kris");
//
//        System.out.println(peasant1.getDelivery());
        ArrayList<Unit> team = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            int val = new Random().nextInt(6);
            switch (val) {
                case 0 -> team.add(new Mag(Names.values()[ new Random().nextInt( Names.values().length ) ].toString()));
                case 1 -> team.add(new Monk(Names.values()[ new Random().nextInt( Names.values().length ) ].toString()));
                case 2 -> team.add(new Peasant(Names.values()[ new Random().nextInt( Names.values().length ) ].toString()));
                case 3 -> team.add(new Robber(Names.values()[ new Random().nextInt( Names.values().length ) ].toString()));
                case 4 -> team.add(new Sniper(Names.values()[ new Random().nextInt( Names.values().length ) ].toString()));
                case 5 -> team.add(new Spearman(Names.values()[ new Random().nextInt( Names.values().length ) ].toString()));
                case 6 -> team.add(new Сrossbowman(Names.values()[ new Random().nextInt( Names.values().length ) ].toString()));
            }

        }
        for (int i = 0; i < team.size()-1; i++)
            System.out.println(team.get(i).getInfo());


    }
}