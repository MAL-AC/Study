package MalyshevAA;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class ToyShop {
    private List<Toys> toys;

    public ToyShop() {
        toys = new ArrayList<>();
    }

    public void addToy(Toys toy) {
        toys.add(toy);
    }

    public void setToyWeight(int id, double weight) {
        for (Toys toy : toys) {
            if (toy.getId() == id) {
                toy.setWeight(weight);
                break;
            }
        }
    }

    public void drawToys() {
        if (toys.isEmpty()) {
            System.out.println("Магазин пуст");
            return;
        }
        double totalWeight = 0;
        for (Toys toy : toys) {
            totalWeight += toy.getWeight();
        }

        Random random = new Random();
        double randomNumber = random.nextDouble() * totalWeight;

        double currentWeight = 0;
        Toys choseToy = null;

        for (Toys toy : toys) {
            currentWeight += toy.getWeight();
            if (randomNumber <= currentWeight) {
                choseToy = toy;
                break;
            }
        }
        if (choseToy != null) {
            System.out.println("Вы выйграли игрушку: " + choseToy.getName());
            if (choseToy.getQuantity() > 0) {
                choseToy.setQuantity(choseToy.getQuantity() - 1);
            } else System.out.println("Такая игрушка закончилась.");
        } else System.out.println("Нифига не выиграли");

    }

    public void saveToFile(String filename) {
        try {
            File logFile = new File(filename);
            FileWriter fileWriter = new FileWriter(logFile);
            for (Toys toy : toys) {
                System.out.println(toy.getId() + toy.getName() + toy.getQuantity() + toy.getWeight() + "\n");
                fileWriter.append(toy.getId() + ", " + toy.getName() + ", " + toy.getQuantity() + ", " + toy.getWeight() + "\n");
            }
            System.out.println("Сохранено");

            fileWriter.close();
        } catch (Exception e) {
            System.out.println("При записи файла что то пошло не так...");
        }
    }

    public void showToys() {
        for (Toys toy : toys) {
            System.out.println("Id: " + toy.getId() + ", Name: " + toy.getName() + ", Quantity: " + toy.getQuantity() + ", Weight: " + toy.getWeight());
        }
    }
    public int setId(){
        int maxId = 0;
        for (Toys toy: toys) {
            if(toy.getId()>maxId){
                maxId = toy.getId();
            }
        }
        return maxId+1;
    }

}




