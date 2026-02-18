def titleToNumber( A):
    B = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Multi = len(A)
    result = 0
    j = 0

    if Multi == 1:
        return B.index(A) + 1

    for i in A:
        result = result * 26 + (ord(i) - ord('A') + 1)
        print( (ord(i)))
        print(ord('A') + 1)
    return result
          
print(titleToNumber("AAT"))
            