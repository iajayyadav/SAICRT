#include<stdio.h>
int autom(int n){
    int sq =n*n;
    while (n!=0)
    {
        if (n%10!=sq%10)
        {
            return 0;
        }
        n=n/10;
        sq=sq/10;
        
    }
    
    return 1;
}
int main(){
    int a,ans;
    scanf("%d",&a);
    ans=autom(a);
    if (ans==1){
        printf("Automorphic");
    }
    else{
        printf("Not Automorphic");
    }

    return 0;
}