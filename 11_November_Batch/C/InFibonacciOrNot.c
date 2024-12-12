#include<stdio.h>
int isFibonacci(int n){
    if (n==0 || n==1)
    {
        return 1;
    }
    int a=0;
    int b=1;
    int c=a+b;
    while (1)
    {
        if (n==c)
        {
            return 1;
        }
        if (c>n)
        {
            return 0;
        }
        a=b;
        b=c;
        c=a+b;
    }
    
}

int main(){
    int a,ans;
    scanf("%d",&a);
    ans=isFibonacci(a);
    if (ans==1)
    {
        printf("Fibonacci Number");   
    }
    else{
        printf("Not a Fibonacci Number");
    }
    
    return 0;
}
