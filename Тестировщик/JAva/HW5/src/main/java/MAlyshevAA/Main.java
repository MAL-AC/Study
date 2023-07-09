package MAlyshevAA;

import java.util.*;

public class Main {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Добро пожаловать на домашнюю работу № 5: Телефонный справочник.");
        HashMap<String, List<Integer>> phoneBook = new HashMap<>();
        while (true) {
            System.out.println("add - добавить контакт, get - найти контакт, ex - выйти.");
            System.out.println("Введите команду: ");
            String choice = scanner.nextLine().toUpperCase();
            if (choice.equals("ADD")) {
                System.out.println("Введите фамилию и телефон через пробел");
                String contact = scanner.nextLine().toUpperCase();
                String[] cont = contact.split(" ");
                if (phoneBook.containsKey(cont[0])) {
                    List<Integer> list = phoneBook.get(cont[0]);
                    list.add(Integer.parseInt(cont[1]));
                } else {
                    ArrayList<Integer> arrayList = new ArrayList<>();
                    arrayList.add(Integer.parseInt(cont[1]));
                    phoneBook.put(cont[0], arrayList);
                }
            } else if (choice.equals("GET")) {
                System.out.println("Введите фамилию контакта");
                String name = scanner.nextLine().toUpperCase();
                if (phoneBook.isEmpty()){
                    System.out.println("Телефонный справочник пуст.");
                }
                else if (phoneBook.containsKey(name)) {
                    for (Integer no : phoneBook.get(name)) {
                        System.out.println(no);
                    }
                }
                else System.out.println("Такой фамилии нет.");
            } else if (choice.equals("EX")) {
                System.out.println("Вы вышли из телефонного справочника.");
                break;
            }
            else System.out.println("Неверная команда.");
        }
    }
}

