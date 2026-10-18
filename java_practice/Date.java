package java_practice;
//import java.util.*;

//import java.util.Scanner;

public class Date{
    private int day,month,year ;

    public Date(int d,int m,int y){
        day = d ;
        month=m;
        year=y ; 
    }
    
    public Date(int d,int m){
        this(d, m, 2021);    // using this() , it is called chaining operator,rather than writing like above (defining everything we just write this() keyword hahha)
    }

    public Date(Date d){
        this.day=d.day ;
        this.month=d.month ;
        this.year=d.year;
    }   
    
    public void setDate(int d,int m, int y){
        this.day=d ;
        this.month=m;
        this.year=y ; 
    }

    public int getDay() { return day;}
    public int getMonth() {return month ;}
    public int getYear() {return year;}

}


        
    

