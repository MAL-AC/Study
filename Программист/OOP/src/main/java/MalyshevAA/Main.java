package MalyshevAA;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Random;
import java.util.jar.Attributes;

import static java.lang.Character.getName;
import static java.lang.Character.getType;

public class Main {
    public static void main(String[] args) {

        ArrayList<Unit> team1 = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            int val = new Random().nextInt(7);
            switch (val) {
                case 0 -> team1.add(new Mag("Mag: "+Unit.setName(),0, val +1));
                case 1 -> team1.add(new Monk("Monk: "+Unit.setName(),0, val +1));
                case 2 -> team1.add(new Peasant("Peasant: "+Unit.setName(),0, val +1));
                case 3 -> team1.add(new Robber("Robber: "+Unit.setName(),0, val +1));
                case 4 -> team1.add(new Sniper("Sniper: "+Unit.setName(),0, val +1));
                case 5 -> team1.add(new Spearman("Spearman: "+Unit.setName(),0, val +1));
                case 6 -> team1.add(new Сrossbowman("Сrossbowman: "+Unit.setName(),0, val +1));
            }
        }
        ArrayList<Unit> team2 = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            int val = new Random().nextInt(7);
            switch (val) {
                case 0 -> team2.add(new Mag(Unit.setName(),10, val +1));
                case 1 -> team2.add(new Monk(Unit.setName(),10, val +1));
                case 2 -> team2.add(new Peasant(Unit.setName(),10, val +1));
                case 3 -> team2.add(new Robber(Unit.setName(),10, val +1));
                case 4 -> team2.add(new Sniper(Unit.setName(),10, val +1));
                case 5 -> team2.add(new Spearman(Unit.setName(),10, val +1));
                case 6 -> team2.add(new Сrossbowman(Unit.setName(),10, val +1));
            }
        }

        System.out.println("Team1: ");
        team1.forEach(n-> System.out.println(n.getInfo()));
        System.out.println("\nTeam2: ");
        team2.forEach(n-> System.out.println(n.getInfo()));

        ArrayList<Unit> allTeam = new ArrayList<>();
        allTeam.addAll(team1);
        allTeam.addAll(team2);
        allTeam.sort(Comparator.comparing(Unit::getSpeed));
        Collections.reverse(allTeam);
        for (Unit unit:allTeam) {
            System.out.println(unit.getSpeed());
        }



        allTeam.forEach(n-> n.step(team2, team1));
        allTeam.forEach(n-> n.step(team1, team2));

        System.out.println("\nTeam1 урон: ");
        team1.forEach(n-> System.out.println(n.getInfo()));

        System.out.println("\nTeam2 урон: ");
        team2.forEach(n-> System.out.println(n.getInfo()));
    }
}