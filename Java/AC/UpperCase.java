public class UpperCase {
    public static void main(String args[]) {
        String str = "hello! I am here ANd you Are";
        int n = str.length();
        if ((int) str.charAt(0) >= 97) {
            System.out.print((char) (((int) (str.charAt(0))) - 32));
        }
        for (int i = 1; i < n; i++) {
            if ((int) str.charAt(i - 1) == 32) {
                if ((int) str.charAt(i) >= 97) {
                    System.out.print((char) (((int) (str.charAt(i))) - 32));
                } else {
                    System.out.print(str.charAt(i));
                }
            } else {
                System.out.print(str.charAt(i));
            }

        }

    }
}