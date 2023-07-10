package MalyshevAA;

public class Coordinates {
    int x, y;

    public Coordinates() {
        this.x = x;
        this.y = y;
    }

    public Coordinates(int x, int y) {
    }

    public double countDistance(Coordinates coordinates) {
        int dx = coordinates.x - x;
        int dy = coordinates.y - y;
        return Math.sqrt(Math.pow(dx, 2) + Math.pow(dy, 2));
    }

}