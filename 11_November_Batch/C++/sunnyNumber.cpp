#include<iostream>
#include<cmath>
using namespace std;
int main(){
    int n,a,y;
    float x;
    cin>>n;
    a=n+1;
    x=sqrt(a);
    y= (int)x;
    if (x==y)
    {
        cout<<"Sunny Number"; 
    }
    else{
        cout<<"Not a sunny number";
    }
    
    return 0;
}