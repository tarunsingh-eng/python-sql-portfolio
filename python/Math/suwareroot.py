def sqrt(A):
        B = 0
        if A == 1:
            print(1)
        if A == 0:
            print(0)       
        while B <= A:
            if int(B*B) <= A and int((B+1)*(B+1))>A:
                print("Answer: ",int(B))
                break
            if int((B+1)*(B+1)) == A:
                print("Answer: ",int(B+1))
                break
            else:    
                B += 2
                print(B)


sqrt(70)