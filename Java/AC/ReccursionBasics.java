public class ReccursionBasics {
    public static boolean isSorted(int arr[], int i){
        if (i==arr.length-1) {
            return true;
        }
        if (arr[i]>arr[i+1]) {
            return false;
        }
        return isSorted(arr, i+1);
    }
    public static int nthFibonacci(int n){
        if (n==1) {
            return 1;
        }
        if (n==0) {
            return 0;
        }
        return nthFibonacci(n-1) + nthFibonacci(n-2);
    }
    public static int firstOccurence(int arr[], int key , int i){
        if (key==arr[i]) {
            return i;
        }
        if (i==arr.length-1) {
            return -1;
        }
        return firstOccurence(arr, key,i+1);
    }
    public static int lastOccurence(int arr[], int key , int i){
        if (key==arr[i]) {
            return i;
        }
        if (i==arr.length-1) {
            return -1;
        }
        return lastOccurence(arr, key,i+1);
    }
    
    public static void main(String[] args) {
        int arr[]={1,2,5,6,7,8};
        // System.out.println(nthFibonacci(6));
        // System.out.println(isSorted(arr, 0));
        System.out.println(firstOccurence(arr, 9,0));
        
    }
}
