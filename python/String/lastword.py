def lengthOfLastWord( A):
        A =  A.rstrip()
        B = A.split(" ")
        B.reverse()
        return len(B[0])

print (lengthOfLastWord("Hello World"))