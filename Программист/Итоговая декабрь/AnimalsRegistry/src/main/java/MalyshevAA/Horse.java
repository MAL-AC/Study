package MalyshevAA;

import java.util.List;

class Horse extends PackAnimals {
    public Horse(String name, String birthDate) {
        super(name, birthDate);
    }
    @Override
    public String getType(){
        return "Horse ";
    }
}