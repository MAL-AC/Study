package MalyshevAA;

public abstract class Pets extends Animal {

    public Pets(String name, String birthDate) {
        super(name,birthDate);
    }
//    @Override
//    public String getType(){
//        return "PackAnimal Camel";
//    }
@Override
public String getClas() {
    return "Pet ";
}
}
