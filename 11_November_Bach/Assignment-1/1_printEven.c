#include<stdio.h>
int main(){
    printf("All even numbers from 1 to 100: \n");
    int i =0;
    while(i<=100)
    {   if(i%2==0){
        printf("%d\n",i);
        }
        i++;
    }
    
    
    return 0;
}