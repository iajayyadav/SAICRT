#include<stdio.h>
int lcm(int a,int b){
    if(a==b){
        return a;
    }
    int max;
    if (a>b){
        max=a;
    }
    else{
        max=b;
    }
    int i=max;
    while (1)
    {
        if (max%a==0&&max%b==0)
        {
            return max;
        }
        max=max+i;
        
    }
    
}
int main(){
    int a,b,ans;
    scanf("%d%d",&a,&b);
    ans=lcm(a,b);
    printf("%d",ans);
    return 0;
}
