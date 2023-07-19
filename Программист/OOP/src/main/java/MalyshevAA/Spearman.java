package MalyshevAA;


public class Spearman extends ClassInfantry {


    public Spearman(String name, int x, int y) {
        super(name, 7, 2,100, 100, 10,1,1, x, y);
    }


//    }
    @Override
    public String getType(){
        return "Spearman";
    }
}
