import java.util.*;
public class Factorial
{
    public static void main(String args[])
    {   
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int a = sc.nextInt();
        int fact=1;
        while(a!=0){
            fact=fact*a;
            a--;
        }
        System.out.println(fact);
        
    }
}