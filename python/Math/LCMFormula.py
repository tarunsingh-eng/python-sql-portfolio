def GCF(A, B, n):
    for i in range (n, 1 , -1):
        if A%i == 0 and B%i == 0:
            return i
    return 1
    
def solve(A, B):
    Mul = A*B
    if A<B:
        return Mul // GCF(A,B,A)
    elif B<A:
        return Mul // GCF(A,B,B)
    else:
        return A

print(solve(11,6))