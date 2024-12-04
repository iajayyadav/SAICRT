import java.util.*;
public class Fibonacci{
    public static void printFibonacci(int a){
        System.out.println("Fibonacci Series: ");
        if (a==1){
            System.out.println(0);
        }
        else if(a==2){
            System.out.println(0);
            System.out.println(1);
        }
        else{
            a=a-2;
            System.out.println(0);
            System.out.println(1);
            int n=0,m=1,o;
            while(a!=0){
            o=n+m;
            System.out.println(o);
            n=m;
            m=o;
            a--;
            }

        }
    }
    public static void main(String args[]){
        Scanner sc= new Scanner(System.in);
            System.out.print("Enter number of terms: ");
            int a = sc.nextInt();
            printFibonacci(a);

    }
}