def solve( A):
        B = []
        Pushed = 0
        Popped = 0
        for n in range(0,len(A)):
            if A[n] == '(':
                print("pushing")
                B.append(A[n])
                Pushed += 1
            elif A[n] == ')' and len(B) !=0:
                print("poping")
                Popped += 1
                B.pop()
        if len(B) == 0 and len(A) == Pushed+Popped:
            return 1
        else:
            return 0
        
print(solve(")(("))