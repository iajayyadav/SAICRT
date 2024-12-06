#include <stdio.h>
#include <math.h>
int isSpy(int n)
{
    int sum=0,prod=1,b;
    while (n!=0)
    {   
        b= n%10;
        sum=sum+b;
        prod=prod*b;
        n/=10;
    }
    if (sum==prod)
    {
        return 1;
    }
    return 0;
    
}

int main()
{
    int a, ans, count = 0, x = 1, temp;
    scanf("%d", &a);
    while (1)
    {
        if (isSpy(x) == 1)
        {
            count++;

        }
        if (count == a)
        {
            printf("%d", x);
            break;
        }
        x++;
    }

    return 0;
}