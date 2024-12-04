#include<stdio.h>
int main(){
    int n,sum;
    scanf("%d",&n);
    printf("Sum of squares of %d natural numbers is:  ",n);
    sum = n*(n+1)*((2*n)+1)/6;
    printf("%d",sum);
    
    
    return 0;
}