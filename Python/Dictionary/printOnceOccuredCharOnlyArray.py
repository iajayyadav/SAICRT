def frequency(arr):
    d={}
    for i in arr:
        d[i]=0
    for i in arr:
        d[i]=d[i]+1
    for k in d.keys():
        if(d[k]==1):
            print(k,end=" ")
            
arr=list(map(int,input("Enter numbers: ").split()))
frequency(arr)