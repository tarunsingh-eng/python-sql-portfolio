def gcd( A, B, C):
    i = 2
    g = 0
    while A%i != 0 and B%i !=0 or i<C:
       # print("in while", i, "<", C , A%i,B%i)
        if A%i == 0 and B%i == 0:
            g = i
        i += 1
    if A%C == 0 and B%C == 0:
       # print("C is answer", i , A%C , B%C)
       return C
    elif i==C and (A%C != 0 or B%C != 0) and g!=0:
       # print("1 is answer", i , A%C , B%C)
        return g
    else:
        return 1

def runner(A,B):
    if A ==0 or B ==0:
        if A>B:
            return A 
        else:
            return B
    elif A>B:
        return gcd(A,B,B)
    elif B>A:
        return gcd(A,B,A)
    else:
        return A

print(runner(0,4))