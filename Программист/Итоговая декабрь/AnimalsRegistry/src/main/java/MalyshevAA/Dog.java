package MalyshevAA;

public class Dog extends Pets{
    public Dog(String name, String birthDate) {
        super(name, birthDate);
    }
    @Override
    public String getType(){
        return "Dog ";
    }
}
