#include<iostream>
using namespace std;
void swap(int a,int b,int c){
    a=a+b+c;
    b=a-b-c;
    c=a-b-c;
    a=a-b-c;
    cout<<a<<" "<<b<<" "<<c;
}
int main(){
    int a ,b,c;
    cin>>a>>b>>c;
    swap(a,b,c);
    return 0;
}