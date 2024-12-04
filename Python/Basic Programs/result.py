n= int(input("Enter the marks: "))
if n>90 and n>101 :
    print("A")
elif n>70 and n<91 :
    print("B")
elif n>60 and n<71 :
    print("C")
elif n>34 and n<61 :
    print("D")
elif n<33 :
    print("Fail")
else:
    print("Invalid")