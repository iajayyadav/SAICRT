def reverse(arr,start,end):
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
def fun(arr,n,k):
    if(k>n):
        k=k%n
    reverse(arr,0,n-1)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    print(arr)
n=int(input("Enter size: "))
arr=list(map(int,input("Enter elements: ").split()))
k=int(input("Enter rotation: "))
fun(arr,n,k)
