# Call by value
When the change is done in formal argument do not reflect in actual argument then this type of value passing
technique is called call by value.

# Formal argument:
Arguments of the called function are called formal argument.

# Actual argument:
Arguments of the calling function.

# pointer 
pointer is a variable that stores the address of another variable. It is declared using * symbol.

# derefrencing
derefrencing means to access the value of the variable pointed by a pointer using the pointer 

Ex: int main(){
    int a=5, *p;
    p=&a;
    printf("%d %d %d %d", a,&a,p,&p,*p);
    return 0;
    }

# properties of pointer

1. a pointer can point to only one variable at a time.
Ex: int main(){
    int a=5,b=7,*p;
    p=&a;
    printf("%d\n",*p);
    p=&b;
    printf("%d\n",*p);
    return 0;
}

2. Multiple pointers can point to a single variable at once.

Ex: int main(){
    int a=5,*p,*q,*r;
    p=&a;
    q=&a;
    r=&a;
    *p=10;
    printf("%d %d %d %d",a,*p,*q,*r);
    return 0;
    }

# Call by refrence
When the change done in formal arguments also reflects in the actual argument then
this type of value passing technique is called as call by refrence. It is always done using pointer.

