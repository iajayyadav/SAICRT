#include<stdio.h>
#include<math.h>

int main(){
    int n,a,y;
    float x;
    scanf("%d",&n);
    a=n+1;
    x=sqrt(a);
    y= (int)x;
    if (x==y)
    {
        printf("Sunny Number"); 
    }
    else{
        printf("Not a sunny number");
    }
    
    return 0;
}