package MalyshevAA;

public class Hamster extends Pets{
    public Hamster(String name, String birthDate) {
        super(name, birthDate);
    }
    @Override
    public String getType(){
        return "Hamster ";
    }
}