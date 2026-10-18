package java_practice;

class Sclass{
    int i=10;
    public Sclass(int _i){
        i=20;
    }
    public void print(){
        System.out.println(i);
    }
}

public class test1 {
    int i ;
    public static void main(String[] args){
        int i=30;
        Sclass obj =new Sclass(i);
        obj.print();
    }
}
