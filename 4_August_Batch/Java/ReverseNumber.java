import java.util.*;
public class ReverseNumber{

    public static int reverse(int a){
        int sum=0;
        while(a!=0){
            int b=a%10;
            sum=(sum*10)+b;
            a/=10;
        }
        return sum;
    }
    public static void main(String args[]){
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter a number: ");
        int a = sc.nextInt();
        int x= reverse(a);
        System.out.println(x);

    }
}