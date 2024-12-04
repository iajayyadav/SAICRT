#include<stdio.h>
int greatest(int a,int b,int c){
    if (a>=b&&a>=c)
    {
        return a;
    }
    else if (b>=a&&b>=c)
    {
        return b;
    }
    else if (c>=b&&c>=a)
    {
        return c;
    }
}
int main(){
    int a,b,c,ans;
    scanf("%d%d%d",&a,&b,&c);
    ans=greatest(a,b,c);
    printf("%d",ans);
    return 0;

}