#include <stdio.h>
void fibonacci(int n) {
    if (n == 1) {
        printf("0\n");
    } else if (n == 2) {
        printf("0\n");
        printf("1\n");
    } else {
        printf("0\n");
        printf("1\n");
        n = n - 2; 
        int a = 0, b = 1, c;
        while (n!=0) {
            c = a + b;
            printf("%d\n", c);
            a = b;
            b = c;
            n--;
        }
    }
}

int main() {
    int n;
    printf("Enter the number of terms: ");
    scanf("%d", &n);
    fibonacci(n);
    return 0;
}

