def fib(n):
    print("-------top---------")
    if (n <= 1):
        print("return n becuase n<=1:", n)
        print("-------if loop---------")
        return n
    print("-------before recursive x = fib (n-1)---------", n)
    x = fib(n - 1)
    print("-------After recursive x = fib (n-1)---------", n)
    print("x = fib(n - 1) = ", x)
    print("-------before recursive y = fib (n-2)---------", n)
    y = fib(n - 2)
    print("-------After recursive y = fib (n-2)---------", n)
    print("y = fib(n - 2) = ", y)
    print("x + y = ", x, "+",y, "=", x+y)
    print("-------Returning x + y ---------")
    return x + y
 

 
# Function Call
print("Function Call", fib(9))
    

