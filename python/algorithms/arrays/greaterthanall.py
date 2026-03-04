def solve( A):
    g = 0
    for y in range(0,len(A)): 
        L=0
        for k in range(0,y):
            if A[y]>A[k]:
                L +=1
                print (L,y-1)
        if y-1 == L: 
            g +=1
    return g

print(solve([ 1, 1, 2, 2 ]))