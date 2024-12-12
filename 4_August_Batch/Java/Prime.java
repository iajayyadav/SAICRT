import java.util.*;
public class Prime{
    public static boolean isPrime(int n){
        if(n<2){
            return false;
        }
        int i=2;
        while(i*i<=n){
            if(n%i==0){
                return false;
            }
            i++;
        }
        return true;
    }
    public static void main(String args[]){
        System.out.print("Enter the number: ");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        System.out.println(isPrime(a));

    }
}