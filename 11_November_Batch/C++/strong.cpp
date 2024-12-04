#include <iostream>
using namespace std;
int factorial(int a)
{
    int fact = 1;
    while (a != 0)
    {
        fact *= a;
        a--;
    }
    return fact;
}
void strong(int a)
{
    int sum = 0, b, n = a;
    while (a != 0)
    {
        b = a % 10;
        sum = sum + factorial(b);
        a = a / 10;
    }
    if (sum == n)
    {
        cout << "Strong number";
    }
    else
    {
        cout << "Not strong number";
    }
}
int main()
{
    int a;
    cin >> a;
    strong(a);
    return 0;
}