package ru.geekbrains.lesson2;

public class SearchUtils {

    public static void a(int x){

    }

    public static void a(int x, int y){

    }

    public static void a(int x, int y, int z){

    }

    public static int binarySearch(int[] array, int value){
        if (array == null)
            return -1;
        return binarySearch(array, value, 0, array.length - 1);
    }

    private static int binarySearch(int[] array, int value, int min, int max){

        if (max < min)
            return -1;

        int middle = (min + max) / 2;

        if (array[middle] == value){
            return middle;
        }
        else if (array[middle] < value)
        {
            return binarySearch(array, value, middle + 1, max);
        }
        else {
            return binarySearch(array, value, min, middle - 1);
        }

    }

}
