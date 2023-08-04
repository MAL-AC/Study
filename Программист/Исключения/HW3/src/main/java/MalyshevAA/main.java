package MalyshevAA;


import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.*;

public class main {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws FileNotExist {
        String[] info;
        File file = new File("src/main/java/MalyshevAA/Users.txt");

        while (true) {
            try {
                info = prompt("Введите через пробел: ФИО, дату рождения, номер телефона и пол (f или m): ");
                checkAmount(info);
                for (int i = 0; i < info.length; i++) {
                    checkFormat(info, i);
                }
                ArrayList<String> people = new ArrayList<>(Arrays.asList(info));
                writeFile(people, file);
            } catch (RuntimeException e) {
                System.out.println();
            }
        }
    }

    public static String[] prompt(String msg) {
        System.out.println(msg);
        return scanner.nextLine().split(" ");
    }

    public static void checkFormat(String[] info, int i) {
        switch (i) {
            case 0:
                if (checkString(info[0]))
                    throw new StringException(-1);
            case 1:
                if (checkString(info[1]))
                    throw new StringException(-1);
            case 2:
                if (checkString(info[2]))
                    throw new StringException(-1);
            case 3:
                if (!dateValidator(info[3])) throw new StringException(-3);
            case 4:
                if (!checkString(info[4]))
                    throw new StringException(-2);
            case 5:
                if (!info[5].equals("f") && !info[5].equals("m")) throw new StringException(-4);
        }
    }

    public static boolean checkString(String line) {
        try {
            Integer.valueOf(line);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    public static void checkAmount(String[] info) {
        if (info.length < 6) throw new AmountException(-1);
        if (info.length > 6) throw new AmountException(-3);
    }


    public static boolean dateValidator(String date) {
        SimpleDateFormat myFormat = new SimpleDateFormat("dd.MM.yyyy");
        myFormat.setLenient(false);
        try {
            myFormat.parse(date);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public static void writeFile(ArrayList<String> users, File file) {
        try (FileWriter fileWriter = new FileWriter(file, true)) {
            for (String s : users) {
                fileWriter.write("<" + s + ">");
            }
            fileWriter.append('\n');
            fileWriter.flush();
        } catch (
                IOException e) {
            throw new RuntimeException(e);
        }
    }
}

