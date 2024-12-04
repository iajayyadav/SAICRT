import java.util.*; 
public class Pattern{
    public static void hollow_rectangle(int row,int col){
        for (int i=1;i<=row;i++){
            for (int j=1;j<=col;j++){
                if(i==1||i==row||j==1||j==col){
                System.out.print("*");
                }
                else{
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter rows: ");
        int a = sc.nextInt();
        System.out.print("Enter cols: ");
        int b = sc.nextInt();
        hollow_rectangle(a,b);

    }

}