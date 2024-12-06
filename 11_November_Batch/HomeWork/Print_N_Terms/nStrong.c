#include <stdio.h>
#include <math.h>
int factorial(int a){
    int fact=1;
    while(a!=0){
        fact*=a;
        a--;
    }
    return fact;
}


int isStrong(int a){
    int sum=0,b, n=a;
    while (a!=0)
    {
        b=a%10;
        sum = sum+factorial(b);
        a=a/10;
    }
    if (sum==n )
    {
        return 1;
    }
    else{
        return 0;
    }
    
}

int main()
{
    int a, ans, count = 0, x = 1, temp;
    scanf("%d", &a);
    while (1)
    {
        if (isStrong(x) == 1)
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