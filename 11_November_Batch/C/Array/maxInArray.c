#include <stdio.h>
int arrayMax(int n, int arr[])
{
    int max = arr[0], i;
    for (i = 0; i < n; i++)
    {
        if (arr[i]>max)
        {
            max=arr[i];
        }
        
    }
    return max;
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
    ans = arrayMax(n, arr);

    printf("Max: %d ", ans);

    return 0;
}