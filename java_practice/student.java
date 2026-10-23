public class student {

    private String name;
    private int age;
    private double cgpa;

    public student(String name,int age,double cgpa){
        this.name=name;
        this.age=age;
        this.cgpa=cgpa;
    }

    public void displayInfo(){
        System.out.println("name : "+name);
        System.out.println("age : "+age);
        System.out.println("cgpa : "+cgpa);
    }

}
  class people {
    public static void main(String[] args){
        student s1 = new student("mukul",19,8.09);
        student s2 = new student("sudhanshu", 18, 9.0);
        s1.displayInfo();
        s2.displayInfo();


    }
    
}


