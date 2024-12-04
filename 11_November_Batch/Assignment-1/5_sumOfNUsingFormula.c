#include<stdio.h>
int main(){
    int n,sum;
    scanf("%d",&n);
    printf("Sum of %d natural numbers is:  ",n);
    sum = n*(n+1)/2;
    printf("%d",sum);
    
    
    return 0;
}