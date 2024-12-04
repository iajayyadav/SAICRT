#include<stdio.h>
void leapYear(int a){
    if(a%400==0){
        printf("Leap Year");
    }
    else if(a%4==0 && a%100!=0){
        printf("Leap Year");
    }
    else{
        printf("Not Leap Year");
    }
}
int main(){
    int a;
    printf("Enter the year: ");
    scanf("%d",&a);
    leapYear(a);
    return 0;
}