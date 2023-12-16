package MalyshevAA;

import java.util.List;

class Donkey extends PackAnimals {
    public Donkey(String name, String birthDate) {
        super(name, birthDate);
    }
    @Override
    public String getType(){
        return "Donkey ";
    }
}