#include<stdio.h>
int main(){
    int marks;
    printf("Enter marks: ");
    scanf("%d",&marks);
    if (marks<101)
    {
       printf("Invalid Input");
    }
    else if (marks>90)
    {
        printf("Grade: A+");
    }
    else if (marks>80)
    {
        printf("Grade: A");
    }
    else if (marks>70)
    {
        printf("Grade: B+");
    }
    else if (marks>60)
    {
        printf("Grade: B");
    }
    else if (marks>33)
    {
        printf("Grade: C");
    }
    else if (marks>0)
    {
        printf("Grade: Fail");
    }
    else 
    {
        printf("Invalid Input");
    }
    
    return 0;
}