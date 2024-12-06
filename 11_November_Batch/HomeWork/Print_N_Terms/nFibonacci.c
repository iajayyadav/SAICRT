#include<stdio.h>
int isFibonacci(int n){
    if (n==0 || n==1)
    {
        return 1;
    }
    int a=0;
    int b=1;
    int c=a+b;
    while (1)
    {
        if (n==c)
        {
            return 1;
        }
        if (c>n)
        {
            return 0;
        }
        a=b;
        b=c;
        c=a+b;
        
        
    }
    
    
}

int main()
{
    int a, ans, count = 0, x = 1, temp;
    scanf("%d", &a);
    while (1)
    {
        if (isFibonacci(x) == 1)
        {
            count++;
             printf("%d ", x);

        }
        if (count == a)
        {
            
            break;
        }
        x++;
    }

    return 0;
}