#include<iostream>
using namespace std;
void leapYear(int a){
    if(a%400==0){
        cout<<"Leap Year";
    }
    else if(a%4==0 && a%100!=0){
        cout<<"Leap Year";
    }
    else{
        cout<<"Not Leap Year";
    }
}
int main(){
    int a;
    cout<<"Enter the year: ";
    cin>>a;
    leapYear(a);
    return 0;
}