
def intersect( A, B):
    newlist = []
    temp = 0 
    for x in A:
        for y in B:
            if x==y and y != temp:
                mark = 1 
                temp = x
                newlist.append(x) 
            elif y == temp:
                temp = 0  
                pass 
    return newlist
     
print(intersect([1,2,3,3,20, 20, 20, 20, 4,5,6],[3,20, 3,5]))