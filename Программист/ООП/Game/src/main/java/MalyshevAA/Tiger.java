package MalyshevAA;

public class Tiger extends Cat {

    public float speed;
    public boolean dangerous;

    public Tiger(String name) {
        super(name);
        this.setAge(3);
    }

    @Override
    public boolean setAge(int age) {
        if (age < 0 || age > 45) {
            super.setAge(0);
            return false;
        }
        setAge(age);
        return true;
    }
    @Override
    public String toString(){
        return name;
    }
}
