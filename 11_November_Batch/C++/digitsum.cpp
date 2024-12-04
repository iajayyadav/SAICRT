#include <iostream>
using namespace std;
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
    cin>>n;
    ans = sum(n);
    cout<<ans;
    return 0;
}