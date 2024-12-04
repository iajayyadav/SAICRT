#include<stdio.h>
int factorial(int a){
    int fact=1;
    while(a!=0){
        fact*=a;
        a--;
    }
    return fact;
}


void strong(int a){
    int sum=0,b, n=a;
    while (a!=0)
    {
        b=a%10;
        sum = sum+factorial(b);
        a=a/10;
    }
    if (sum==n )
    {
        printf("Strong number");
    }
    else{
        printf("Not strong number");
    }
    
}
int main(){
    int a;
    scanf("%d",&a);
    strong(a);
    
    return 0;
}