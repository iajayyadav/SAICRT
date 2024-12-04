// import util.java.*;
public class PairsArray{
    public static void reverse(int arr[]){
        int start=0,end=(arr.length)-1;
        while(start<end){
            int temp = arr[start];
            arr[start]=arr[end];
            arr[end]=temp;
            start++;
            end--;
        }
    }

    public static void main(String args[]){
        int arr[] = {2,4,6,8,10};


        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }

        // reverse(arr);
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
System.out.println();
        for (int i=0;i<arr.length;i++){
            for (int j=i+1;j<arr.length;j++){
                System.out.print("("+arr[i]+",");
                System.out.print(arr[j]+")");
            }
            System.out.println();
        }
    }
}