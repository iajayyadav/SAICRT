#include <stdio.h>
int arrayMin(int n, int arr[])
{
    int min = arr[0], i;
    for (i = 0; i < n; i++)
    {
        if (arr[i]<min)
        {
            min=arr[i];
        }
        
    }
    return min;
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
    ans = arrayMin(n, arr);

    printf("Min: %d ", ans);

    return 0;
}