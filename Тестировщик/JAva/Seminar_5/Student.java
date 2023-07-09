package ru.geekbrains.lesson5;

public class Student {

    String name;
    String surName;
    Double rating;

    public Student(){

    }


    /**
     * Позволяет создать новый объект и проинициализировать состояние будущего объекта
     * @param name Имя студента
     * @param surName Фамилия студента
     * @param rating Средний балл студента (его рейтинг)
     */
    public Student(String name, String surName, Double rating){

        this.name = name;
        this.surName = surName;
        this.rating = rating;
    }

    @Override
    public String toString() {
        return surName + " " + name;
    }
}
