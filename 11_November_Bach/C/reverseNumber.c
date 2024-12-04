#include<stdio.h>
int reverse(int a){
    int sum=0,b;
    while(a!=0){
       b=a%10;
       sum=(sum*10)+b;
       a=a/10;
    }
    return sum;
}
int main(){
    int a , ans;
    scanf("%d",&a);
    ans = reverse(a);
    printf("%d",ans);
    return 0;
}