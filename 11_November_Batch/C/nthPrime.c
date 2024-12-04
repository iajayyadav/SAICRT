#include <stdio.h>
#include <math.h>
int isPrime(int n)
{
    if (n <= 1)
    {
        return 0;
    }
    int i = 2;
    int j = sqrt(n);
    while (i <= j)
    {
        if (n % i == 0)
        {
            return 0;
        }
        i++;
    }
    return 1;
}

int main()
{
    int a, ans, count = 0, x = 2, temp;
    scanf("%d", &a);
    while (1)
    {
        if (isPrime(x) == 1)
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