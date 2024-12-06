#include <stdio.h>
int arraysum(int n, int arr[])
{
    int sum = 0, i;
    for (i = 0; i < n; i++)
    {
        sum = sum + arr[i];
    }
    return sum;
}
int main()
{
    int n, ans;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    ans = arraysum(n, arr);

    printf("Sum: %d ", ans);

    return 0;
}