#include <stdio.h>
#include <math.h>
int isAutomorphic(int n){
    int sq =n*n;
    while (n!=0)
    {
        if (n%10!=sq%10)
        {
            return 0;
        }
        n=n/10;
        sq=sq/10;
        
    }
    
    return 1;
}

int main()
{
    int a, ans, count = 0, x = 1, temp;
    scanf("%d", &a);
    while (1)
    {
        if (isAutomorphic(x) == 1)
        {
            count++;
            printf("%d ", x);

        }
        if (count == a)
        {
            
            break;
        }
        x++;
    }

    return 0;
}