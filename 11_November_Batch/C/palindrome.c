#include<stdio.h>
void palindrome(int n){
    int a=n,sum=0,b;
    while (n!=0)
    {
        b=n%10;
        sum=(sum*10)+b;
        n/=10;
    }
    if (a==sum)
    {
        printf("Palindrome");
    }
    else{
        printf("Not palindrome");
    }
    
}
int main(){
    int a;
    scanf("%d",&a);
    palindrome(a);
    return 0;
}