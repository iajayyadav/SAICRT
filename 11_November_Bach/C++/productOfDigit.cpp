#include<iostream>
using namespace std;
int product(int a){
    int prod=1,b;
    while(a!=0){
        b=a%10;
        prod=prod*b;
        a=a/10;
    }
    return prod;
}
int main(){
    int n;
    cin>>n;
    int ans=product(n);
    cout<<ans;
    return 0;
}