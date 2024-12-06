#include <stdio.h>
#include <math.h>
int isPalindrome(int n){
    int a=n,sum=0,b;
    while (n!=0)
    {
        b=n%10;
        sum=(sum*10)+b;
        n/=10;
    }
    if (a==sum)
    {
        return 1;
    }
    else{
        return 0;
    }
    
}

int main()
{
    int a, ans, count = 0, x = 1, temp;
    scanf("%d", &a);
    while (1)
    {
        if (isPalindrome(x) == 1)
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