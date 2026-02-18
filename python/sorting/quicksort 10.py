    # @param A : list of integers
    # @return a list of integers
    # Strategy 
    # 1st - Square
    # 2nd - Quick sort
    # User recrusion if possible
def partition(array, low, high):
    pivot = array [high] # always take the right most
    i = low - 1 # greater element pointer 
    
    for j in range(low, high): 
        if array [j] <= pivot:
            #swap with element at i 
            i = i + 1 

            (array[i], array[j]) = (array[j], array[i])

    # swaping the pivot to partition location
    (array[i+1], array[high]) = (array[high], array[i+1])
    return i + 1

def quicksort(array,low,high):
    if low < high:
        pi = partition(array, low , high)
        quicksort(array, low, pi-1)
        quicksort(array, pi+1, high)

def solve(A):
        low = 0
        high = len(A) - 1 
        quicksort(A,low,high)
        print(A)


print(solve([ 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1  ]))

        



    
