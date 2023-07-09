package ru.geekbrains.lesson5;

import java.util.Comparator;

public class RatingComparator implements Comparator<Double> {

    // -1
    @Override
    public int compare(Double o1, Double o2) {
        return Double.compare(o2, o1);
    }

}
