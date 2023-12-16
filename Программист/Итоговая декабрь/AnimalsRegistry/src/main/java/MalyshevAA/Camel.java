package MalyshevAA;

class Camel extends PackAnimals {
    public Camel(String name, String birthDate) {
        super(name, birthDate);
    }
    @Override
    public String getType(){
        return "Camel ";
    }
}