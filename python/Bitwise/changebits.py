def solve(A):
    B = '{0:08b}'.format(A).lstrip('0')[::-1]
   
    return B


            
print(solve(5))
