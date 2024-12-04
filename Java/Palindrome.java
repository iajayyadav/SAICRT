import java.util.*;
public class Palindrome{
    public static boolean isPalindrome(int a){
        int n=a,sum=0;
        while(a!=0){
            int b=a%10;
            sum=(sum*10)+b;
            a/=10;
        }
        if (n==sum){
            return true;
        }
        return false;
    }
    public static void main(String args[]){
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter the number: ");
        int a = sc.nextInt();
        System.out.println(isPalindrome(a));

    }
}