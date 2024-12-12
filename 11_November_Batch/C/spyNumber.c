#include <stdio.h>
#include <math.h>
int isSpy(int n)
{
    int sum=0,prod=1,b;
    while (n!=0)
    {   
        b= n%10;
        sum=sum+b;
        prod=prod*b;
        n/=10;
    }
    if (sum==prod)
    {
        return 1;
    }
    return 0;
    
}

int main(){
    int a,ans;
    scanf("%d",&a);
    ans=isSpy(a);
    if (ans==1)
    {
        printf("Spy Number");   
    }
    else{
        printf("Not Spy Number");
    }
    
    return 0;
}