#include<stdio.h>
int product(int a){
    int prod=1,b;
    while(a!=0){
        b=a%10;
        prod=prod*b;
        a=a/10;
    }
    return prod;
}
int main(){
    int n;
    scanf("%d",&n);
    int ans=product(n);
    printf("%d",ans);
    return 0;
}