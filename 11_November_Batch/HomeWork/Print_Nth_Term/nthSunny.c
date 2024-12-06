#include <stdio.h>
#include <math.h>
int isSunny(int n)
{
    int a;
    float x;
    a=n+1;
    x=sqrt(a);
    if (x==(int)x)
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
        if (isSunny(x) == 1)
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