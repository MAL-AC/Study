package MalyshevAA;

public class Cat extends Pets{
    public Cat(String name, String birthDate) {
        super(name, birthDate);
    }
    @Override
    public String getType(){
        return "Cat ";
    }
}
