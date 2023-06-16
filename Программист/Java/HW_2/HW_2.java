

public class HW_2 {
    public static void main(String[] args) {
    
    StringBuilder str = new StringBuilder("{\"name\":\"Ivanov\", \"country\":\"Russia\", \"city\":\"Moscow\", \"age\":\"null\"}");
    str = str.replace(0,2,"");
    str = str.replace(4,7," = ");
    str = str.replace(13,17,", ");
    str = str.replace(22,25," = ");
    str = str.replace(31,35,", ");
    str = str.replace(37,40," = ");
    str = str.replace(46,str.length(),"");

    System.out.println(str);
    
    }

    
}