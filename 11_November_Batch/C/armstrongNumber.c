#include <stdio.h>
#include <math.h>
int isAmstrong(int n)
{
    int count = 0, a = n, b;
    float sum = 0;
    while (n != 0)
    {
        count++;
        n /= 10;
    }
    n = a;
    while (n != 0)
    {
        b = n % 10;
        sum += pow(b, count);
        n /= 10;
    }
    if (sum == a)
    {
        return 1;
    }
    return 0;
}

int main()
{
    int a;
    scanf("%d", &a);
    int ans = isAmstrong(a);
    if (ans == 0)
    {
        printf("Not Armstrong");
    }
    else
    {
        printf("Armstrong");
    }
    return 0;
}
