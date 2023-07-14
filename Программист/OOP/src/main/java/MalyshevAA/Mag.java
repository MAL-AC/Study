package MalyshevAA;

import java.util.ArrayList;

public class Mag extends ClassMagic {
    public Mag(String name, int x, int y) {
        super(name, 10, 100, 100, 3, x,y);
    }


    @Override
    public String getType(){
        return "Mag";
    }
}

