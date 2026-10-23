import java.util.Scanner;

public class palindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String text  = sc.next();
        
        boolean ispalindrome=true;
        int left=0;
        int right=text.length()-1;

        while(left<right){
            if (text.charAt(left)!=text.charAt(right)) {
                ispalindrome=false;
            }
            left++;
            right--;


        }

        System.err.println(ispalindrome);

        
        sc.close();

    }
}
