def LCM(A, B, n):
    i = 1
    #print((n*i)%A)
    #print((n*i)%B)
    while (n*i)%A != 0 or (n*i)%B != 0:
        print("in while")
        i +=1
    return n*i
        
def solve(A, B):
    if A<B:
        return LCM(A,B,A)
    elif B<A:
        return LCM(A,B,B) 
    else:
        return A

print(solve(9,18))