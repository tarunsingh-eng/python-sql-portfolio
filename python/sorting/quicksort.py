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
        start_list = A
        if start_list is not None:
            squares = [x*x for x in start_list]
    
        low = 0
        high = len(squares) - 1 
        quicksort(squares,low,high)
        print("Sorted:", squares)

solve([ -855, -847, -747, -708, -701, -667, -666, -618, -609, -536, -533, -509, -500, -396, -336, -297, -284, -229, -173, -173, -132, -38, -5, 35, 141, 169, 281, 322, 358, 421, 436, 447, 478, 538, 547, 644, 667, 673, 705, 711, 718, 724, 726, 811, 869, 894, 895, 902, 912, 942, 961 ])

        



    
