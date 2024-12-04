#include<iostream>
using namespace std;
int factorial(int a){
    int fact=1;
    while(a!=0){
        fact*=a;
        a--;
    }
    return fact;
}
int main(){
    int a , ans;
    cin>>a;
    ans = factorial(a);
    cout<<ans;
    return 0;
}