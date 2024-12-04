#include<stdio.h>
int main(){
    int i =1,sum=0,n;
    scanf("%d",&n);
    printf("Sum of %d natural numbers is:  ",n);
    while(i<=n)
    {   
        sum=sum+i;
        i++;
    }
    printf("%d",sum);
    
    
    return 0;
}