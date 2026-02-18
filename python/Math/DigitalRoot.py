
def solve(A):
    if A < 10:
        return A
    while A >=10:
        for i in str(A):
            A = []
            A.append(i)
        print(A)
      #  A = sum(A)
    return A

print(solve(54324))