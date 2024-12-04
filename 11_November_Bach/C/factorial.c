#include<stdio.h>
int factorial(int a){
    int fact=1;
    while(a!=0){
        fact*=a;
        a--;
    }
    return fact;
}
int main(){
    int a , ans;
    scanf("%d",&a);
    ans = factorial(a);
    printf("%d",ans);
    return 0;
}