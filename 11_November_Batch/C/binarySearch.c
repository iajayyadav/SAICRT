#include<stdio.h>
int binarySearch(int n, int arr[],int x){
    int st=0;
    int end=n-1;
    int mid =(st+end)/2;
    while(st<=end){
    if (arr[mid]==x){
        return mid;
    }
    else if(arr[mid]<x){
        st=mid+1;
        mid =(st+end)/2;

    }
    else{
        end=mid-1;
        mid =(st+end)/2;
    }
    }
    return -1;
}

int main(){
    int a,x;
    scanf("%d%d",&a,&x);
    int arr[a];
    

    return 0;
}