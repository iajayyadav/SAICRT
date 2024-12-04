def frequency(s):
    d={}
    for i in s:
        d[i]=0
    for i in s:
        d[i]=d[i]+1
    d=sorted(d.items(),key=lambda x:x[1],reverse=True)
    d=dict(d)
    for k,v in d.items():
        print(k," occured",v," times")
        
arr=list(map(int,input("Enter numbers: ").split()))
frequency(arr)

    

    
    