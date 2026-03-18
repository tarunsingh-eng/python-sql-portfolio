import numpy

def arrays(arr):
    a = numpy.array(arr);
    b = []
    for i in reversed(a):
        b.append(i); 
    c = numpy.array(b, float);
    return c;
    # complete this function
    # use numpy.array

arr = [1, 2, 3, 4, -8, -10]
result = arrays(arr)
print(result)
print([f"{x:.1f}" for x in result])