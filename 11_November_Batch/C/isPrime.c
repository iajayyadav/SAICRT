#include <stdio.h>
#include <math.h>
int prime(int n)
{
    if (n <= 1)
    {
        return 0;
    }
    int x = sqrt(n);
    int i = 2;
    while (i <= x)
    {
        if (n % i == 0)
        {
            return 0;
        }
        i++;
    }
    return 1;
}
int main(){
    int a;
    scanf("%d",&a);
    int ans = prime(a);
    if (ans==0)
    {
        printf("Not Prime");
    }
    else{
        printf("Prime");
    }
    return 0;
}