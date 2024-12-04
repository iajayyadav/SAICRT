#include <stdio.h>
int sum(int a)
{
    int n = a, b, sum = 0;
    while (a != 0)
    {
        b = a % 10;
        sum += b;
        a /= 10;
    }
    return sum;
}
int main()
{
    int n, ans;
    scanf("%d", &n);
    ans = sum(n);
    printf("%d", ans);
    return 0;
}