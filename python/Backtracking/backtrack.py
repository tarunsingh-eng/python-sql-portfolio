A = [9,2,3,4,5,6]
B = []
C = []
print("-------------")
for l in range(len(A)): 
    print("Appending B")
    print("l = ", l)
    B.append(A[l])
    C = B
    for n in C:
        print(n)
        if len(C)>=2:
            print("C is now large enough")
            print("l = ", l)
            print("C =", C[l])
            print("B =", B[l])
            if C[l] == B[l]:
                print("I am here")
            else:
                C = B
                print("I am in else")