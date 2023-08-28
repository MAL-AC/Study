package MalyshevAA;

import java.util.Arrays;

public class Program {

    public static void main(String[] args) {


        LinkedList<Employee> employeeLinkedList = new LinkedList<>();
        employeeLinkedList.addFirst(new Employee("34523453245", 21));
        employeeLinkedList.addFirst(new Employee("AAAAAA", 33));
        employeeLinkedList.addFirst(new Employee("DDDD", 34));
        employeeLinkedList.addFirst(new Employee("AAAAAA", 44));
        employeeLinkedList.addFirst(new Employee("EEEEE", 51));
        employeeLinkedList.addFirst(new Employee("MMMMMM", 33));
        employeeLinkedList.addFirst(new Employee("AAAAAA", 32));

        System.out.println(employeeLinkedList);
        System.out.println();
        employeeLinkedList.reverse();
        System.out.println("Развернутый односвязный список: ");
        System.out.println(employeeLinkedList);

    }

}
