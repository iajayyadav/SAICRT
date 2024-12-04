#include<iostream>
using namespace std;
void palindrome(int n){
    int a=n,sum=0,b;
    while (n!=0)
    {
        b=n%10;
        sum=(sum*10)+b;
        n/=10;
    }
    if (a==sum)
    {
        cout<<"Palindrome";
    }
    else{
        cout<<"Not palindrome";
    }
    
}
int main(){
    int a;
    cin>>a;
    palindrome(a);
    return 0;
}