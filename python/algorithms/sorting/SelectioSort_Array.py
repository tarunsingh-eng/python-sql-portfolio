
def SelectionSort(A):
    for i in range (0, len(A)):
        # assume i as the minimum
        mid_ind = i
        for j in range (i+1, len(A)):
        # Compare if i is actuall minimum
            if A [mid_ind] > A [j]:
        # Note the new minimum element     
                mid_ind = j
        #Swap minimum element with i pointer in loop
        A[i], A[mid_ind] = A[mid_ind] , A [i]
    return(A)

# Driver Code
print(SelectionSort([10,11,34,1,0,5]))

