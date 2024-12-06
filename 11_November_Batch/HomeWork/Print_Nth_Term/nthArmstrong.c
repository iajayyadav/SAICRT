#include <stdio.h>
#include <math.h>
int isAmstrong(int n)
{
    int count =0,sum=0,a=n,b;
    while (n!=0)
    {
        count++;
        n/=10;
    }
    n=a;
    while (n!=0)
    {   
        b= n%10;
        sum=sum+pow(b,count);
        n/=10;
    }
    if (sum==a)
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
        if (isAmstrong(x) == 1)
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