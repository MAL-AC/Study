package MalyshevAA;

import java.util.Comparator;
import java.util.Iterator;

/**
 * Связный список
 * @param <T>
 */
public class LinkedList<T> implements Iterable<T> {

    /**
     * Указатель на первый элемент связного списка
     */
    public Node head;

    @Override
    public Iterator<T> iterator() {
        return null;
    }

    public class LinkedListIterator implements Iterator<T>{

        @Override
        public boolean hasNext() {
            return false;
        }

        @Override
        public T next() {
            return null;
        }
    }

    /**
     * Узел связного списка
     */
    public class Node{

        /**
         * Ссылка на следующий узел
         */
        public Node next;

        /**
         * Значение узла
         */
        public T value;

    }

    /**
     * Добавление нового элемента в начало связного списка
     * @param value значение
     */
    public void addFirst(T value){
        Node node = new Node();
        node.value = value;
        if (head != null){
            node.next = head;
        }
        head = node;
    }

    /***
     * Метод разворота списка
     */
    public void reverse(){
        Node currentNode = head;
        Node prevNode = null;

        while (currentNode != null){
            Node next = currentNode.next;
            currentNode.next = prevNode;

            prevNode = currentNode;
            currentNode = next;
        }

        head = prevNode;
    }

    @Override
    public String toString() {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append('[');
        Node node = head;
        while (node != null){
            stringBuilder.append(node.value);
            node = node.next;
            if (node != null)
                stringBuilder.append('\n');
        }
        stringBuilder.append(']');
        return stringBuilder.toString();
    }
}
