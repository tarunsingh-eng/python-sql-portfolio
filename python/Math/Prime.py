def isPrime(A):
    n = 2 
    import math
    B=math.sqrt(A)
    if A <= 1:
        return False
    else:
        while n <= B:
            if A%n==0:
                print(A/n)
                return False
            n +=1 
        return True

print(isPrime(39601))