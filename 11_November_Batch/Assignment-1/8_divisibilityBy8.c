#include<stdio.h>
int divisible(int a){
     if (a%8==0)
     {
        return 1;
     }
     return 0;
     
}
int main(){
    int n,ans;
    scanf("%d",&n);
    ans=divisible(n);
    if (ans==1)
    {
        printf("Divisible by 8");
    }
    else{
        printf("Not divisible by 8");
    }
    return 0;
}