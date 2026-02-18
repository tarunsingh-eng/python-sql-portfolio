def permuteStrings(A, B):
        if len(A) == len(B):
            k = 0 
            for i in A:
                Yes = 0
                for j in B: 
                    if i == j: 
                        Yes = 1
                        break
                    else:
                       pass 
                if Yes==1:
                    k +=1
                else:
                    break
            if k == len(A):
                return 1
            else:
                return 0 
        else:
            return 0

print(permuteStrings("bajd","abdj"))